<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Share+Tech+Mono&size=36&duration=3200&pause=1200&color=8A00C4&background=00000000&center=true&vCenter=true&width=850&height=80&lines=NE0SYNC;Red+Team+%7C+Offensive+Security;Reverse+Engineering;Quiet+craft.+Sharp+results.;%3C%2F%3E" alt="NE0SYNC — Red Team and Reverse Engineering">

<br>

<img src="https://readme-typing-svg.demolab.com?font=VT323&size=24&duration=2600&pause=1000&color=E4BCFF&background=00000000&center=true&vCenter=true&width=850&height=40&lines=%3E+recon+%2F+exploit+%2F+dissect;%3E+binaries+%2F+internals+%2F+research;%3E+break+%E2%86%92+understand+%E2%86%92+rebuild;Understand+what+lies+beneath." alt="Recon, exploit, dissect — binaries, internals, research">

[![Scope](https://img.shields.io/badge/scope-local%20labs-8a00c4?style=flat-square)](./SCOPE.md)
[![Focus](https://img.shields.io/badge/focus-reverse%20engineering-111111?style=flat-square)](./labs/01-broken-gate/WRITEUP.md)
[![Language](https://img.shields.io/badge/language-C%20%7C%20Python-5c2d91?style=flat-square)](./tooling/inspect_sample.py)

</div>

# NE0SYNC RE Labs

Small, reproducible offensive-security laboratories built to document how an operator
and reverse engineer move from an unknown sample to a defensible technical conclusion.

The first lab is **The Broken Gate**: a self-authored Windows PE sample with an
intentionally weak local validation flow. The target is safe, deterministic and
included for analysis — no third-party software, credentials or live targets.

## 60-second demo

```text
clone → build sample → inspect strings/imports → trace validation → read write-up
```

```powershell
git clone https://github.com/jeremiasamado/redteam-examples.git
cd redteam-examples
.\scripts\build.ps1
python .\tooling\inspect_sample.py .\samples\broken-gate.exe
```

The sample prints a deterministic training token when the intended validation
path is reached. The exercise is about recovering that path, not bypassing
commercial software.

## Repository map

```text
labs/01-broken-gate/
├─ README.md                 # briefing and objectives
├─ WRITEUP.md                # operator notebook and conclusions
└─ src/broken_gate.c         # self-authored sample source
scripts/build.ps1            # reproducible Windows build
tooling/inspect_sample.py    # hash, strings and PE header inspection
samples/.gitkeep             # generated binaries stay out of git
SCOPE.md                     # safety and authorization boundary
```

## Lab 01 — The Broken Gate

**Objective:** recover the validation flow of a small PE sample using static
analysis, then explain the design weakness and the correct engineering fix.

**Skills:** PE inspection, strings, imports, control-flow reasoning, debugger
assisted validation and concise technical reporting.

The lab deliberately separates four stages:

1. **Observe** — identify the file, hash and visible attack surface.
2. **Hypothesize** — connect strings and imported APIs to likely code paths.
3. **Validate** — confirm the flow against a binary built from the included source.
4. **Explain** — document evidence, impact and remediation in the write-up.

Start with [`labs/01-broken-gate/README.md`](./labs/01-broken-gate/README.md), then
read the [`operator notebook`](./labs/01-broken-gate/WRITEUP.md).

## Why this exists

This repository is a public portfolio of offensive tradecraft and reverse-engineering
thinking. Every sample is authored for this repository, runs locally and uses
synthetic data. The value is the chain of reasoning: **hypothesis → evidence →
conclusion**.

## License

Code is released under the MIT License. Lab samples and documentation are for
authorized local research and training only; see [`SCOPE.md`](./SCOPE.md).
