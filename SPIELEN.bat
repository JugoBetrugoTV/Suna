@echo off
title HOLLOWMERE

set "GAME_DIR=%~dp0game"
set "PYTHON_DIR=%~dp0python_portable"
set "PYTHON_EXE=%PYTHON_DIR%\python.exe"
set "PYTHON_ZIP=%~dp0_python_dl.zip"
set "PYTHON_URL=https://www.python.org/ftp/python/3.11.9/python-3.11.9-embed-amd64.zip"

if exist "%PYTHON_EXE%" goto run_game

echo.
echo  HOLLOWMERE - Erster Start
echo  --------------------------
echo.
echo  Portable Python wird heruntergeladen (einmalig, ca. 15 MB).
echo  Nichts wird auf deinem System installiert.
echo.
echo  Bitte warten...
echo.

powershell -NoProfile -ExecutionPolicy Bypass -Command "$ProgressPreference='SilentlyContinue'; [Net.ServicePointManager]::SecurityProtocol=[Net.SecurityProtocolType]::Tls12; Invoke-WebRequest -Uri '%PYTHON_URL%' -OutFile '%PYTHON_ZIP%' -UseBasicParsing"

if not exist "%PYTHON_ZIP%" (
    echo.
    echo  Download fehlgeschlagen. Bitte Internetverbindung pruefen.
    pause
    exit /b 1
)

echo  Download fertig. Entpacke...

powershell -NoProfile -ExecutionPolicy Bypass -Command "Expand-Archive -Path '%PYTHON_ZIP%' -DestinationPath '%PYTHON_DIR%' -Force"

if not exist "%PYTHON_EXE%" (
    echo  Entpacken fehlgeschlagen.
    pause
    exit /b 1
)

del "%PYTHON_ZIP%" >nul 2>&1

echo python311.zip> "%PYTHON_DIR%\python311._pth"
echo .>> "%PYTHON_DIR%\python311._pth"
echo import site>> "%PYTHON_DIR%\python311._pth"

echo  Fertig!
echo.

:run_game
echo  Starte HOLLOWMERE...
echo.

"%PYTHON_EXE%" "%GAME_DIR%\main.py"

if %ERRORLEVEL% neq 0 (
    echo.
    echo  Fehler beim Starten. Ist der 'game' Ordner vorhanden?
    pause
)
