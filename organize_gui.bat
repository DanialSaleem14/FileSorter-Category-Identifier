@echo off
echo ========================================
echo   Document Organizer - GUI Mode
echo ========================================
echo.
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
