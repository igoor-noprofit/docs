@echo off
setlocal

REM Paths resolved relative to this script (repo root) so the workflow works
REM regardless of where the repo is checked out on disk.
set "REPO=%~dp0"
set "DOCS_DIR=%~dp0docs"
set "VAULT=%~dp0..\IGOOR_VAULT\DOCS"

REM Kill any existing mkdocs server processes to prevent cache issues
echo ========================================
echo Cleaning up existing processes...
echo ========================================
taskkill /F /IM python.exe /FI "WINDOWTITLE eq *mkdocs*" 2>nul
taskkill /F /FI "IMAGENAME eq python.exe" /FI "WINDOWTITLE eq *watch_docs*" 2>nul
timeout /t 2 /nobreak >nul

if exist "%DOCS_DIR%" rmdir /s /q "%DOCS_DIR%"
mkdir "%DOCS_DIR%"
xcopy "%VAULT%" "%DOCS_DIR%" /E /I /Y

cd /d "%REPO%"
call venv\Scripts\activate

REM Build English documentation
echo ========================================
echo Building English documentation...
echo ========================================
mkdocs build -f config/en/mkdocs.yml
if errorlevel 1 (
    echo ERROR: Failed to build English documentation
    pause
    exit /b 1
)
echo.

REM Build French documentation
echo ========================================
echo Building French documentation...
echo ========================================
mkdocs build -f config/fr/mkdocs.yml
if errorlevel 1 (
    echo ERROR: Failed to build French documentation
    pause
    exit /b 1
)
echo.

REM Start development server (French by default)
echo ========================================
echo Starting development server...
echo ========================================
echo To serve English instead, run: mkdocs serve -f config/en/mkdocs.yml
echo.
start "" chrome http://127.0.0.1:8000/
start /B python watch_docs.py
mkdocs serve -f config/fr/mkdocs.yml

pause
