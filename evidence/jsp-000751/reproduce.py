"""Sequential replay of one source-reviewed standalone proof packet.

Run the complete invocation under the shared compiler mutex. No subprocess
is concurrent. Source preparation is separate from observed verification.
"""
import argparse, datetime, hashlib, json, os, re, subprocess, time
from pathlib import Path

def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--packet',type=Path,required=True)
    ap.add_argument('--lean-bin',type=Path,required=True)
    ap.add_argument('--mathlib',type=Path,required=True)
    ap.add_argument('--output',type=Path,default=Path('verified-run'))
    args=ap.parse_args()
    root=args.packet.resolve(); binary=args.lean_bin.resolve(); lib=args.mathlib.resolve()
    inputs=json.loads((root/'inputs.json').read_text(encoding='utf-8'))
    for name,expected in inputs['source_sha256'].items():
        assert digest(root/name)==expected, 'Source changed: '+name
    suffix='.exe' if os.name=='nt' else ''
    lean=binary/('lean'+suffix); checker=binary/('leanchecker'+suffix)
    version=subprocess.check_output([str(lean),'--version'],text=True).strip()
    assert 'version 4.33.0,' in version
    rev=subprocess.check_output(['git','-C',str(lib),'rev-parse','HEAD'],text=True).strip()
    assert rev=='db584cd6d46c92f209a44c0f1c829460d327499d'
    out=(root/args.output).resolve();out.mkdir(parents=True,exist_ok=True)
    if (out/'verification.json').exists():
        prior=json.loads((out/'verification.json').read_text(encoding='utf-8'))
        if prior.get('success'): raise RuntimeError('Already verified; preserve successful evidence')
    paths=[out,lib/'.lake/build/lib/lean']
    paths+=sorted(p for p in (lib/'.lake/packages').glob('*/.lake/build/lib/lean') if p.is_dir())
    assert paths[1].is_dir()
    env=dict(os.environ,LEAN_PATH=os.pathsep.join(map(str,paths)))
    module=inputs['module'];audit=inputs['harness_module']
    commands=[('compile-source',[str(lean),'-j1','-M4096','-o',str(out/(module+'.olean')),'./'+module+'.lean']),
              ('compile-audit',[str(lean),'-j1','-M4096','-o',str(out/(audit+'.olean')),'./'+audit+'.lean']),
              ('leanchecker',[str(checker),'--verbose',module])]
    report={'jsp':inputs['jsp'],'erdos':inputs['erdos'],'lean_version':version,'mathlib_commit':rev,
            'source_commit':inputs['source_commit'],'source_sha256':inputs['source_sha256'],
            'main_theorem':inputs['main_theorem'],'started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'steps':[],'success':False,'network_isolation':False,'imported_mathlib_cache_used':True,
            'checker_scope':'Bundled same-kernel replay of the target module against pinned imported dependencies; not an independently implemented checker or fresh whole-dependency replay.'}
    def save(): (out/'verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    for name,command in commands:
        print('Starting '+inputs['jsp']+' '+name,flush=True)
        start=time.monotonic();result=subprocess.run(command,cwd=root,env=env,capture_output=True,
            text=True,encoding='utf-8',errors='replace')
        output=result.stdout+result.stderr
        for path,alias in [(root,'<packet>'),(binary,'<lean-bin>'),(lib,'<mathlib>')]:output=output.replace(str(path),alias)
        log=out/(name+'.log');log.write_text(output,encoding='utf-8')
        rendered=[Path(command[0]).name]+[s.replace(str(root),'<packet>') for s in command[1:]]
        report['steps'].append({'name':name,'command':rendered,'exit_code':result.returncode,
                               'seconds':round(time.monotonic()-start,3),'log':log.name,'log_sha256':digest(log)})
        save();print(name+' exit='+str(result.returncode),flush=True)
        if result.returncode:return result.returncode
        if name=='compile-audit':
            matches=re.findall(r"'([^']+)' depends on axioms: \[([^\]]*)\]",output)
            selected=[a for n,a in matches if n==inputs['main_theorem']]
            assert len(selected)==1,'Missing exact main-theorem axiom report'
            axioms=set(selected[0].replace(' ','').split(','))-{''}
            assert axioms<={'propext','Classical.choice','Quot.sound'},'Nonstandard axiom dependency'
            report['target_axioms']=sorted(axioms)
    for name,expected in inputs['source_sha256'].items(): assert digest(root/name)==expected
    report.update(success=True,finished_utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
    save();print('PASS '+inputs['jsp'],flush=True)
    return 0

if __name__=='__main__': raise SystemExit(main())
