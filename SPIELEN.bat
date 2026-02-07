@echo off
title HOLLOWMERE

set "ROOT=%~dp0"

:: Try the built EXE first
if exist "%ROOT%HOLLOWMERE.exe" (
    start "" "%ROOT%HOLLOWMERE.exe"
    exit /b 0
)

:: Try portable Python
set "PYTHON_EXE=%ROOT%python_portable\python.exe"
if exist "%PYTHON_EXE%" (
    if exist "%ROOT%hollowmere.py" (
        "%PYTHON_EXE%" "%ROOT%hollowmere.py"
        exit /b 0
    )
)

:: Nothing found
echo.
echo  HOLLOWMERE.exe nicht gefunden.
echo  Bitte zuerst BUILD_EXE.bat ausfuehren!
echo.
pause
