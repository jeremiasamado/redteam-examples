$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $PSScriptRoot
$source = Join-Path $root "labs\01-broken-gate\src\broken_gate.c"
$outputDir = Join-Path $root "samples"
$output = Join-Path $outputDir "broken-gate.exe"

New-Item -ItemType Directory -Force -Path $outputDir | Out-Null

$gcc = Get-Command gcc -ErrorAction SilentlyContinue
if (-not $gcc) {
    throw "gcc was not found. Install MinGW-w64 or use the included source with a Windows C compiler."
}

& $gcc.Source $source -O0 -g0 -s -o $output -ladvapi32
if ($LASTEXITCODE -ne 0) {
    throw "The sample build failed."
}

Write-Host "Built $output"
