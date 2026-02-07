@echo off
title HOLLOWMERE - EXE Builder

set "ROOT=%~dp0"
set "PYTHON_DIR=%ROOT%python_portable"
set "PYTHON_EXE=%PYTHON_DIR%\python.exe"
set "PYTHON_ZIP=%ROOT%_python_dl.zip"
set "PYTHON_URL=https://www.python.org/ftp/python/3.11.9/python-3.11.9-embed-amd64.zip"
set "GET_PIP_URL=https://bootstrap.pypa.io/get-pip.py"

echo.
echo  ================================================
echo   HOLLOWMERE - EXE Builder
echo  ================================================
echo.
echo  Dieses Script erstellt HOLLOWMERE.exe fuer dich.
echo  Beim ersten Mal werden ca. 50 MB heruntergeladen.
echo.

:: ---- Step 1: Portable Python ----
if exist "%PYTHON_EXE%" goto has_python

echo  [1/4] Lade Portable Python herunter...
powershell -NoProfile -ExecutionPolicy Bypass -Command "$ProgressPreference='SilentlyContinue'; [Net.ServicePointManager]::SecurityProtocol=[Net.SecurityProtocolType]::Tls12; Invoke-WebRequest -Uri '%PYTHON_URL%' -OutFile '%PYTHON_ZIP%' -UseBasicParsing"

if not exist "%PYTHON_ZIP%" (
    echo  FEHLER: Download fehlgeschlagen.
    pause
    exit /b 1
)

echo  Entpacke...
powershell -NoProfile -ExecutionPolicy Bypass -Command "Expand-Archive -Path '%PYTHON_ZIP%' -DestinationPath '%PYTHON_DIR%' -Force"
del "%PYTHON_ZIP%" >nul 2>&1

:: Fix the ._pth file so pip/packages work
echo python311.zip> "%PYTHON_DIR%\python311._pth"
echo .>> "%PYTHON_DIR%\python311._pth"
echo Lib\site-packages>> "%PYTHON_DIR%\python311._pth"
echo import site>> "%PYTHON_DIR%\python311._pth"

echo  Python bereit.

:has_python

:: ---- Step 2: Install pip ----
if exist "%PYTHON_DIR%\Scripts\pip.exe" goto has_pip

echo  [2/4] Installiere pip...
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

:: ---- Step 3: Install PyInstaller ----
echo  [3/4] Installiere PyInstaller...
"%PYTHON_DIR%\Scripts\pip.exe" install pyinstaller --quiet --no-warn-script-location 2>nul

:: ---- Step 4: Build EXE ----
echo  [4/4] Baue HOLLOWMERE.exe...
echo.

"%PYTHON_DIR%\Scripts\pyinstaller.exe" --onefile --noconsole --name HOLLOWMERE --add-data "%ROOT%HOLLOWMERE.html;." --icon=NUL --clean --noconfirm "%ROOT%launcher.py" 2>nul

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
    echo  Versuche es erneut oder oeffne HOLLOWMERE.html direkt im Browser.
)

echo.
pause
