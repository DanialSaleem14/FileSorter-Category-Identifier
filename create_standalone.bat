@echo off
echo ========================================
echo   Creating Standalone Document Organizer
echo ========================================
echo.
echo This will create a portable version that works on any computer
echo without requiring Python or any other installations.
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python first, then run this script again.
    echo.
    pause
    exit /b 1
)

echo Python found. Creating standalone package...
echo.

REM Run the standalone creation script
python dependencies/create_standalone.py

echo.
echo ========================================
echo   Standalone Package Created!
echo ========================================
echo.
echo The standalone package has been created in:
echo "DocumentOrganizer_Standalone" folder
echo.
echo To use on any computer:
echo 1. Copy the entire "DocumentOrganizer_Standalone" folder
echo 2. Run "build_standalone.bat" (first time only)
echo 3. Run "DocumentOrganizer.bat" to use the organizer
echo.
echo No Python installation required on the target computer!
echo.
pause
