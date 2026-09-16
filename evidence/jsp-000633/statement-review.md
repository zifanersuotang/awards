# JSP-000633 / Erdős 772：既有证明复放

这是 plby 已公开证明的归属保留复放，不是本任务的新数学证明。确切运行结果见 `replay-result.json` 与三个日志；不存在结果文件或没有 `success: true` 时不得声称重放完成。

## 来源与署名

- 固定源码：[plby/lean-proofs, Erdos772.lean](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos772.lean)。
- 本地 `Erdos772Existing.lean` 由固定提交的 `git show` 原始 blob 导出，保留 LF，字节完全一致。SHA-256 `c11e5d58be0b3e8a690fa5f790d59ff2a7eb6e4df63390f4aa68c04784a626de`。
- 原源码保留 Apache 2.0、Formal Conjectures Authors 版权行及原署名。非形式化作者：Noga Alon、Paul Erdős；形式化作者按原文件记录：Codex、GPT-5.6 Sol。本任务只做检查与归属登记准备。
- 版本：Lean 4.33.0；Mathlib `db584cd6d46c92f209a44c0f1c829460d327499d`。仅导入 `Mathlib`；没有自定义依赖模块和外部证书文件。Mathlib 本体与其包使用共享只读缓存，输出只写本目录。

## 登记范围与定义

[原题页面](https://www.erdosproblems.com/772)问固定两项表示数上界 k 时，保证的 Sidon 子集大小除以平方根是否趋于无穷，以及是否存在正指数改进。现有主定理 `Erdos772.erdos_772`（原文件 L1040）同时回答两问；L940 给出更强的 n^(2/3) 数量级下界。

直接量化有限集合的 `Erdos772.exists_sidon_finset_cubic`（L829）避免 H 的空类约定，提供：对于每个有限自然数集 A 和有序二项和表示数上界 k，存在 Sidon 子集 S，满足

\[
|A|^2 \le 4096(k+1)^3 |S|^3.
\]

这等价于常数 `1/(16(k+1))` 的 n^(2/3) 下界。`IsSidon id S` 允许重复加数，但只允许平凡的交换相等，即非平凡的 `x+x=y+z` 也被排除；比只计互异两加数的约定更强。

必须公开说明两个约定：

1. 原题现代页面的卷积是有序计数。源文件 `H k n` 将“最大保证大小”显式限制在 `r≤n`。当 k=1 且 n≥2 时不存在符合有序计数条件的 A，因而采用自然的空类值 H=n；不能把一个未限制 r 的空量词最大值说成自动存在。实际有限集合下界定理不受此边界约定影响。
2. [Alon–Erdős 1985 原文](https://web.math.princeton.edu/~nalon/PDFS/Publications2/An%20application%20of%20graph%20theory%20to%20additive%20number%20theory.pdf) p201 的式(4)与 p202 的概率删点证明使用互异加数、无序的表示数约定。已经下载全文并核对 p201–202。若无序互异表示数至多 k，则有序计数含对角项至多 2k+1，故上述定量命题可经固定常数替换应用；现有文件按现代卷积版本陈述，不声称形式化原文的所有定理（无限序列、分割等）。

## 可重复操作

`replay.py` 检查源码哈希，设置精确的 `LEAN_PATH`，依次：

1. 编译未修改的已有源码并生成 `Erdos772Existing.olean`。
2. 运行 `Audit772.lean`，打印主定理、直接有限集下界、实数幂下界的签名和公理依赖，以及关键定义。
3. 执行 `leanchecker Erdos772Existing`，只检查这个目标模块。

准备对应版本的 Lean 和 Mathlib，并确保 Mathlib 及其依赖缓存已经构建后，运行：

```text
python replay.py --toolchain /path/to/lean-4.33.0 --mathlib /path/to/mathlib
```

本地多人验证时将整个管线放入共享串行队列一次，避免嵌套锁和并行耗尽内存。`local-config.json` 只是私有机器配置，不应包含在公开材料中；正文 PDF 与页面图片也仅作本地文献核对，公开材料请保留原文链接。可公开文件为本 README、两个 `.lean` 文件、`replay.py`、`replay-result.json` 与三个日志。本文件记录证明范围与边界约定；提交结果由官方 Issue 记录。
