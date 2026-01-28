@echo off

REM Kill any existing mkdocs server processes to prevent cache issues
echo ========================================
echo Cleaning up existing processes...
echo ========================================
taskkill /F /IM python.exe /FI "WINDOWTITLE eq *mkdocs*" 2>nul
taskkill /F /FI "IMAGENAME eq python.exe" /FI "WINDOWTITLE eq *watch_docs*" 2>nul
timeout /t 2 /nobreak >nul

REM Generate navigation based on current docs structure
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

rmdir /s /q site

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

echo ========================================
echo Build complete!
echo ========================================
echo.
echo To test locally:
echo   - English: mkdocs serve -f config/en/mkdocs.yml
echo   - French:  mkdocs serve -f config/fr/mkdocs.yml
echo.

pause