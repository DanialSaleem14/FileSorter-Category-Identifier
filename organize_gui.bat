@echo off
echo ========================================
echo   Document Organizer - GUI Mode
echo ========================================
echo.

REM Check if dependencies are installed
python -c "import click" >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Required Python packages are not installed!
    echo.
    echo Please run install_dependencies.bat first to install all required packages.
    echo.
    echo This is a one-time setup required before using the organizer.
    echo.
    pause
    exit /b 1
)

echo Starting the graphical interface...
echo.
echo Instructions:
echo 1. Select 'Unsorted' folder as input
echo 2. Click 'Process Files' to organize
echo 3. Files will be moved to 'Sorted' folder
echo.

REM Check if Unsorted folder exists, create if not
if not exist "Unsorted" (
    echo Creating 'Unsorted' folder...
    mkdir Unsorted
    echo.
    echo 'Unsorted' folder created. Please place your files there.
    echo.
)

REM Run the GUI
python -m dependencies.organizer.gui

echo.
echo GUI closed.
pause
