"""Check an exact local proof closure, releasing an optional shared mutex per stage.

The coordinator itself must NOT be run inside the shared mutex. On this host,
pass --serial-runner to the trusted shared run_lean_serial.py. No stage is parallel.
"""
from pathlib import Path
import argparse,datetime,hashlib,json,os,re,subprocess,sys,time

def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def save(path,data):path.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def main():
    ap=argparse.ArgumentParser()
    for name in ['packet','lean-bin','mathlib']:ap.add_argument('--'+name,type=Path,required=True)
    ap.add_argument('--output',type=Path,default=Path('verified-run'))
    ap.add_argument('--serial-runner',type=Path)
    ap.add_argument('--stage',choices=['compile','audit','checker'])
    ap.add_argument('--name')
    args=ap.parse_args();root=args.packet.resolve();out=(root/args.output).resolve()
    out.relative_to(root);out.mkdir(parents=True,exist_ok=True)
    lib=args.mathlib.resolve();bin=args.lean_bin.resolve();source=root/'source'
    meta=json.loads((root/'inputs.json').read_text(encoding='utf-8'))
    suffix='.exe' if os.name=='nt' else ''
    lean=bin/('lean'+suffix);checker=bin/('leanchecker'+suffix)
    version=subprocess.check_output([str(lean),'--version'],text=True).strip()
    assert 'version 4.33.0,' in version
    rev=subprocess.check_output(['git','-C',str(lib),'rev-parse','HEAD'],text=True).strip()
    assert rev=='db584cd6d46c92f209a44c0f1c829460d327499d'
    allhash={r['path']:r['sha256'] for r in meta['ordered_modules']}
    allhash[meta['harness_module']+'.lean']=meta['harness_sha256']
    for path,expected in allhash.items():assert sha(source/path)==expected,'Changed source '+path
    fingerprint=hashlib.sha256(json.dumps({'source':allhash,'target':meta['main_theorem'],'version':version,'mathlib':rev},sort_keys=True).encode()).hexdigest()
    oleans=out/'lib';oleans.mkdir(exist_ok=True)
    paths=[oleans,lib/'.lake/build/lib/lean']+sorted(p for p in (lib/'.lake/packages').glob('*/.lake/build/lib/lean') if p.is_dir())
    assert paths[1].is_dir()
    env=dict(os.environ,LEAN_PATH=os.pathsep.join(map(str,paths)),LEAN_NUM_THREADS='1')
    def label(stage,name):return stage+'-'+name.replace('.','_')
    def clean(text):
        for path,alias in [(root,'<packet>'),(bin,'<lean-bin>'),(lib,'<mathlib>')]:text=text.replace(str(path),alias)
        return text
    if args.stage:
        assert args.name
        stage=args.stage;name=args.name;tag=label(stage,name)
        if stage=='compile':assert name in [r['module'] for r in meta['ordered_modules']]
        if stage=='audit':assert name==meta['harness_module']
        if stage=='checker':assert name in {r['module'].split('.')[0] for r in meta['ordered_modules']}
        output=oleans/(name.replace('.','/')+'.olean') if stage!='checker' else None
        if output:output.parent.mkdir(parents=True,exist_ok=True)
        command=[str(checker),'--verbose',name] if stage=='checker' else [str(lean),'-j1','-M4096','-o',str(output),'./'+name.replace('.','/')+'.lean']
        started=time.monotonic();result=subprocess.run(command,cwd=source,env=env,capture_output=True,text=True,encoding='utf-8',errors='replace')
        text=clean(result.stdout+result.stderr);log=out/(tag+'.log');log.write_text(text,encoding='utf-8')
        record={'stage':stage,'name':name,'fingerprint':fingerprint,'command':[Path(command[0]).name]+[clean(x) for x in command[1:]],
            'exit_code':result.returncode,'seconds':round(time.monotonic()-started,3),'log':log.name,'log_sha256':sha(log),'LEAN_NUM_THREADS':'1'}
        if output and output.exists():record.update(olean=output.relative_to(out).as_posix(),olean_sha256=sha(output))
        if stage=='audit' and result.returncode==0:
            matches=re.findall(r"'([^']+)' depends on axioms: \[([^\]]*)\]",text)
            audited={}
            for target in meta.get('audit_targets',[meta['main_theorem']]):
                selected=[a for n,a in matches if n==target]
                assert len(selected)==1,'Missing exact target axiom report: '+target
                axioms=sorted(set(selected[0].replace(' ','').split(','))-{''})
                assert set(axioms)<={'propext','Classical.choice','Quot.sound'},'Unallowed target axioms: '+target
                audited[target]=axioms
            record['audited_targets']=audited
            record['target_axioms']=audited[meta['main_theorem']]
        if stage=='checker':record['replayed_modules']=re.findall(r'^replaying (\S+)$',text,re.M)
        save(out/(tag+'.json'),record)
        print(f'{meta["jsp"]} {tag} exit={result.returncode}',flush=True)
        return result.returncode
    reportpath=out/'verification.json'
    if reportpath.exists():
        prior=json.loads(reportpath.read_text(encoding='utf-8'))
        if prior.get('success'):raise RuntimeError('Preserve successful run; choose another output only for an explicitly justified rerun')
    modules=[r['module'] for r in meta['ordered_modules']]
    selectors=sorted({m.split('.')[0] for m in modules})
    stages=[('compile',m) for m in modules]+[('audit',meta['harness_module'])]+[('checker',p) for p in selectors]
    report={'jsp':meta['jsp'],'erdos':meta['erdos'],'lean_version':version,'mathlib_commit':rev,'source_commit':meta['source_commit'],
        'source_sha256':allhash,'main_theorem':meta['main_theorem'],'fingerprint':fingerprint,'started_utc':now(),
        'success':False,'steps':[],'network_isolation':False,'LEAN_NUM_THREADS':'1','imported_mathlib_cache_used':True,
        'expected_replayed_modules':sorted(modules),'checker_selectors':selectors,
        'checker_scope':'Same Lean kernel. Replay of the entire compiled local source closure, checked against actual verbose module names; imported pinned Mathlib caches are trusted, not freshly replayed. No independently implemented checker.'}
    save(reportpath,report)
    for stage,name in stages:
        tag=label(stage,name);stepfile=out/(tag+'.json');record=None
        if stepfile.exists():
            old=json.loads(stepfile.read_text(encoding='utf-8'))
            if old['exit_code']==0 and old['fingerprint']==fingerprint and sha(out/old['log'])==old['log_sha256']:
                if stage=='checker' or ((out/old['olean']).exists() and sha(out/old['olean'])==old['olean_sha256']):record=old
        if record is None:
            cmd=[sys.executable,str(Path(__file__).resolve()),'--packet',str(root),'--lean-bin',str(bin),'--mathlib',str(lib),
                 '--output',str(args.output),'--stage',stage,'--name',name]
            if args.serial_runner:
                cmd=[sys.executable,str(args.serial_runner.resolve()),'--tag',f'batch3-E{meta["erdos"]}-{tag}','--cwd',str(root),'--']+cmd
            child=subprocess.Popen(cmd,cwd=root)
            save(out/'active-stage.json',{'stage':stage,'name':name,'wrapper_or_child_pid':child.pid,'shared_mutex_used':bool(args.serial_runner)})
            rc=child.wait()
            if stepfile.exists():record=json.loads(stepfile.read_text(encoding='utf-8'))
            if rc or record is None:
                report.update(failed_stage=tag,stage_exit_code=rc,finished_utc=now());save(reportpath,report)
                return rc or 1
        report['steps'].append(record);save(reportpath,report)
    actual=[m for r in report['steps'] if r['stage']=='checker' for m in r['replayed_modules']]
    assert sorted(actual)==sorted(modules),'Actual replay module set does not equal the pinned compiled local closure'
    report['actual_replayed_modules']=sorted(actual)
    report['target_axioms']=next(r['target_axioms'] for r in report['steps'] if r['stage']=='audit')
    report['audited_targets']=next(r['audited_targets'] for r in report['steps'] if r['stage']=='audit')
    for path,expected in allhash.items():assert sha(source/path)==expected
    report.update(success=True,finished_utc=now());save(reportpath,report)
    print(f'PASS {meta["jsp"]}: {len(modules)} exact local proof modules compiled and replayed',flush=True)
    return 0
if __name__=='__main__':raise SystemExit(main())
