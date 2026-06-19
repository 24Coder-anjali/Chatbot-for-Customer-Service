@echo off
cd /d "%~dp0"

set BUNDLED_PYTHON=%USERPROFILE%\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe
if exist "%BUNDLED_PYTHON%" (
    "%BUNDLED_PYTHON%" app.py
    goto :end
)

where python >nul 2>nul
if %errorlevel%==0 (
    python app.py
    goto :end
)

echo Python was not found. Please install Python 3 or run this project from an environment that includes Python.
pause

:end
