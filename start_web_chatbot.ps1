Set-Location -LiteralPath $PSScriptRoot

$bundledPython = Join-Path $env:USERPROFILE ".cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"

if (Test-Path -LiteralPath $bundledPython) {
    & $bundledPython app.py
    exit
}

$pythonCommand = Get-Command python -ErrorAction SilentlyContinue
if ($pythonCommand) {
    & python app.py
    exit
}

Write-Host "Python was not found. Please install Python 3 or run this project from an environment that includes Python."
Read-Host "Press Enter to close"
