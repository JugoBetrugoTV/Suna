@echo off
chcp 65001 >nul 2>&1
title HOLLOWMERE

:: ============================================================
::  HOLLOWMERE - Spielstarter
::  Laedt automatisch Portable Python herunter (einmalig).
::  Kein Installieren noetig. Einfach doppelklicken.
:: ============================================================

set "GAME_DIR=%~dp0game"
set "PYTHON_DIR=%~dp0python_portable"
set "PYTHON_EXE=%PYTHON_DIR%\python.exe"
set "PYTHON_ZIP=%~dp0python_portable.zip"
set "PYTHON_URL=https://www.python.org/ftp/python/3.11.9/python-3.11.9-embed-amd64.zip"

:: Prüfe ob Portable Python schon da ist
if exist "%PYTHON_EXE%" goto :run_game

echo.
echo  ════════════════════════════════════════════════════
echo   HOLLOWMERE - Erster Start
echo  ════════════════════════════════════════════════════
echo.
echo   Portable Python wird heruntergeladen (einmalig, ~15 MB).
echo   Nichts wird installiert. Alles bleibt in diesem Ordner.
echo.
echo   Bitte warten...
echo.

:: Download mit PowerShell
powershell -NoProfile -ExecutionPolicy Bypass -Command ^
    "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; " ^
    "try { " ^
    "  $ProgressPreference = 'SilentlyContinue'; " ^
    "  Invoke-WebRequest -Uri '%PYTHON_URL%' -OutFile '%PYTHON_ZIP%' -UseBasicParsing; " ^
    "  Write-Host '  Download abgeschlossen.' " ^
    "} catch { " ^
    "  Write-Host '  FEHLER beim Download: ' + $_.Exception.Message; " ^
    "  exit 1 " ^
    "}"

if %ERRORLEVEL% neq 0 (
    echo.
    echo   Download fehlgeschlagen. Bitte Internetverbindung pruefen.
    echo   Alternativ: Python manuell installieren von python.org
    pause
    exit /b 1
)

:: Entpacken
echo   Entpacke Python...
powershell -NoProfile -ExecutionPolicy Bypass -Command ^
    "Expand-Archive -Path '%PYTHON_ZIP%' -DestinationPath '%PYTHON_DIR%' -Force"

if %ERRORLEVEL% neq 0 (
    echo   FEHLER beim Entpacken.
    pause
    exit /b 1
)

:: ZIP aufräumen
del "%PYTHON_ZIP%" >nul 2>&1

:: Python-Pfad konfigurieren (damit imports funktionieren)
:: Die ._pth Datei muss angepasst werden für relative imports
for %%f in ("%PYTHON_DIR%\python*._pth") do (
    echo python311.zip> "%%f"
    echo .>> "%%f"
    echo import site>> "%%f"
)

echo   Fertig! Python ist bereit.
echo.

:run_game
:: ============================================================
::  Spiel starten
:: ============================================================
echo.
echo  ════════════════════════════════════════════════════
echo   Starte HOLLOWMERE...
echo  ════════════════════════════════════════════════════
echo.

"%PYTHON_EXE%" "%GAME_DIR%\main.py"

if %ERRORLEVEL% neq 0 (
    echo.
    echo   Ein Fehler ist aufgetreten.
    echo   Bitte stelle sicher, dass der 'game' Ordner vorhanden ist.
    echo.
    pause
)
