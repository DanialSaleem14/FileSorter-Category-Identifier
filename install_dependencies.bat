@echo off
echo ========================================
echo Document Organizer - Dependency Installer
echo ========================================
echo.
echo This script will install all required Python packages.
echo Please make sure Python is installed on your system.
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH!
    echo Please install Python from https://python.org
    echo Make sure to check "Add Python to PATH" during installation.
    pause
    exit /b 1
)

echo Python found! Installing dependencies...
echo.

REM Install required packages
echo Installing Python packages...
pip install -r dependencies/requirements.txt

if %errorlevel% neq 0 (
    echo.
    echo ERROR: Failed to install some packages!
    echo Please check your internet connection and try again.
    pause
    exit /b 1
)

echo.
echo ========================================
echo Installation completed successfully!
echo ========================================
echo.
echo You can now run the Document Organizer:
echo - Double-click organize_gui.bat for GUI mode
echo - Double-click organize_files.bat for command line mode
echo.
pause
