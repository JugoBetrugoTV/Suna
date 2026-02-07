@echo off
title HOLLOWMERE - EXE Builder

set "ROOT=%~dp0"
set "PYTHON_DIR=%ROOT%python_portable"
set "PYTHON_EXE=%PYTHON_DIR%\python.exe"
set "PYTHON_ZIP=%ROOT%_python_dl.zip"
set "PYTHON_URL=https://www.python.org/ftp/python/3.12.8/python-3.12.8-embed-amd64.zip"
set "GET_PIP_URL=https://bootstrap.pypa.io/get-pip.py"

echo.
echo  ================================================
echo   HOLLOWMERE - EXE Builder (Pygame)
echo  ================================================
echo.
echo  Dieses Script erstellt HOLLOWMERE.exe fuer dich.
echo  Beim ersten Mal werden ca. 80 MB heruntergeladen.
echo.

:: ---- Remove old Python 3.11 if present (had DLL issues) ----
if exist "%PYTHON_DIR%\python311._pth" (
    echo  Alte Python-Version gefunden, aktualisiere...
    rmdir /s /q "%PYTHON_DIR%" >nul 2>&1
)

:: ---- Step 1: Portable Python 3.12 ----
if exist "%PYTHON_EXE%" goto has_python

echo  [1/5] Lade Portable Python 3.12 herunter...
powershell -NoProfile -ExecutionPolicy Bypass -Command "$ProgressPreference='SilentlyContinue'; [Net.ServicePointManager]::SecurityProtocol=[Net.SecurityProtocolType]::Tls12; Invoke-WebRequest -Uri '%PYTHON_URL%' -OutFile '%PYTHON_ZIP%' -UseBasicParsing"

if not exist "%PYTHON_ZIP%" (
    echo  FEHLER: Download fehlgeschlagen. Pruefe deine Internetverbindung.
    pause
    exit /b 1
)

echo  Entpacke...
powershell -NoProfile -ExecutionPolicy Bypass -Command "Expand-Archive -Path '%PYTHON_ZIP%' -DestinationPath '%PYTHON_DIR%' -Force"
del "%PYTHON_ZIP%" >nul 2>&1

:: Fix the ._pth file so pip/packages work
echo python312.zip> "%PYTHON_DIR%\python312._pth"
echo .>> "%PYTHON_DIR%\python312._pth"
echo Lib\site-packages>> "%PYTHON_DIR%\python312._pth"
echo import site>> "%PYTHON_DIR%\python312._pth"

echo  Python 3.12 bereit.

:has_python

:: ---- Step 2: Install pip ----
if exist "%PYTHON_DIR%\Scripts\pip.exe" goto has_pip

echo  [2/5] Installiere pip...
powershell -NoProfile -ExecutionPolicy Bypass -Command "$ProgressPreference='SilentlyContinue'; [Net.ServicePointManager]::SecurityProtocol=[Net.SecurityProtocolType]::Tls12; Invoke-WebRequest -Uri '%GET_PIP_URL%' -OutFile '%ROOT%_get_pip.py' -UseBasicParsing"

"%PYTHON_EXE%" "%ROOT%_get_pip.py" --no-warn-script-location >nul 2>&1
del "%ROOT%_get_pip.py" >nul 2>&1

if not exist "%PYTHON_DIR%\Scripts\pip.exe" (
    echo  FEHLER: pip Installation fehlgeschlagen.
    pause
    exit /b 1
)
echo  pip bereit.

:has_pip

:: ---- Step 3: Install Pygame ----
echo  [3/5] Installiere Pygame...
"%PYTHON_DIR%\Scripts\pip.exe" install pygame --quiet --no-warn-script-location 2>nul

:: ---- Step 4: Install PyInstaller ----
echo  [4/5] Installiere PyInstaller...
"%PYTHON_DIR%\Scripts\pip.exe" install pyinstaller --quiet --no-warn-script-location 2>nul

:: ---- Step 5: Build EXE ----
echo  [5/5] Baue HOLLOWMERE.exe...
echo.

"%PYTHON_DIR%\Scripts\pyinstaller.exe" --onefile --noconsole --name HOLLOWMERE --hidden-import pygame --clean --noconfirm "%ROOT%hollowmere.py" 2>nul

if exist "%ROOT%dist\HOLLOWMERE.exe" (
    copy "%ROOT%dist\HOLLOWMERE.exe" "%ROOT%HOLLOWMERE.exe" >nul
    echo.
    echo  ================================================
    echo   FERTIG!
    echo  ================================================
    echo.
    echo   HOLLOWMERE.exe wurde erstellt.
    echo   Du findest sie hier: %ROOT%HOLLOWMERE.exe
    echo.
    echo   Einfach doppelklicken zum Spielen!
    echo.

    :: Aufraeumen
    rmdir /s /q "%ROOT%dist" >nul 2>&1
    rmdir /s /q "%ROOT%build" >nul 2>&1
    del "%ROOT%HOLLOWMERE.spec" >nul 2>&1
) else (
    echo.
    echo  FEHLER beim Bauen der EXE.
    echo  Pruefe ob hollowmere.py vorhanden ist.
    echo.
)

echo.
pause
