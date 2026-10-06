# Lab 01 — The Broken Gate

## Briefing

You receive `broken-gate.exe`, a small Windows PE sample produced from the
source in this directory. Recover the local validation flow and explain why it
should not be trusted as an authorization boundary.

## Objectives

- establish a reproducible file identity;
- extract useful strings and imports;
- identify the validation function and its decision point;
- record evidence without changing the sample;
- propose a server-side verification design.

## Start

From the repository root:

```powershell
.\scripts\build.ps1
python .\tooling\inspect_sample.py .\samples\broken-gate.exe
```

Use a PE viewer or debugger of your choice to validate the observations. The
included source is available for comparison after the analysis.

## Expected questions

1. Which strings reveal the purpose of the sample?
2. Which imported API is used to obtain the local identity?
3. Where does the success/failure decision occur?
4. Why can a local decision be modified by a user who controls the process?
5. What would move the trust boundary to a service-side verifier?

The answer is in [`WRITEUP.md`](./WRITEUP.md), but read it after forming your
own hypothesis.
