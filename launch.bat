@echo off

REM Kill any existing mkdocs server processes to prevent cache issues
echo ========================================
echo Cleaning up existing processes...
echo ========================================
taskkill /F /IM python.exe /FI "WINDOWTITLE eq *mkdocs*" 2>nul
taskkill /F /FI "IMAGENAME eq python.exe" /FI "WINDOWTITLE eq *watch_docs*" 2>nul
timeout /t 2 /nobreak >nul

if exist C:\TMP\IGOOR\docs\docs rmdir /s /q C:\TMP\IGOOR\docs\docs
mkdir C:\TMP\IGOOR\docs\docs
xcopy C:\TMP\IGOOR\OBSIDIAN\IGOOR_VAULT\DOCS C:\TMP\IGOOR\docs\docs /E /I /Y

REM Generate navigation based on folder structure
echo ========================================
echo Generating navigation...
echo ========================================
python generate_nav.py
if errorlevel 1 (
    echo ERROR: Failed to generate navigation
    pause
    exit /b 1
)
echo.

cd C:\TMP\IGOOR\docs
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

REM Start development server (English by default)
echo ========================================
echo Starting development server...
echo ========================================
echo To serve French instead, run: mkdocs serve -f config/fr/mkdocs.yml
echo.
start "" chrome http://127.0.0.1:8000/
start /B python watch_docs.py
mkdocs serve -f config/en/mkdocs.yml

pause
