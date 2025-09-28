@echo off
echo ========================================
echo   Document Organizer
echo ========================================
echo.
echo This will process files from the 'Unsorted' folder
echo and organize them into the 'Sorted' folder.
echo.
echo IMPORTANT: Place your files in the 'Unsorted' folder first!
echo.

REM Check if Unsorted folder exists
if not exist "Unsorted" (
    echo Creating 'Unsorted' folder...
    mkdir Unsorted
    echo.
    echo Please place your files in the 'Unsorted' folder and run this script again.
    echo.
    pause
    exit /b
)

REM Check if there are files in Unsorted folder
dir /b "Unsorted\*" >nul 2>&1
if errorlevel 1 (
    echo No files found in 'Unsorted' folder.
    echo Please place your files in the 'Unsorted' folder and run this script again.
    echo.
    pause
    exit /b
)

echo Files found in 'Unsorted' folder. Processing...
echo.

REM Run the organizer
python -m dependencies.organizer process "Unsorted" --output-base "Sorted"

echo.
echo ========================================
echo   Processing Complete!
echo ========================================
echo Check the 'Sorted' folder to see your organized files.
echo.
pause
