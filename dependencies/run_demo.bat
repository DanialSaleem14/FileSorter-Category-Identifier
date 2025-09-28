@echo off
echo ========================================
echo   Document Organizer - DEMO MODE
echo ========================================
echo.
echo WARNING: This creates sample files for testing purposes only!
echo The organizer will ONLY process files you place in 'Unsorted' folder.
echo.
echo This demo will:
echo 1. Create sample files in 'Unsorted' folder
echo 2. Process them with the organizer
echo 3. Show you how the system works
echo.
echo Press any key to continue or close this window to cancel...
pause >nul

echo.
echo Creating sample files in 'Unsorted' folder...
python scripts\make_dummy_data.py

echo.
echo Running document organizer...
python -m organizer process "Unsorted" --output-base "Sorted"

echo.
echo ========================================
echo   Demo Complete!
echo ========================================
echo Check the 'Sorted' folder to see organized files.
echo.
echo IMPORTANT: For normal use, place YOUR files in 'Unsorted' folder
echo and run 'organize_files.bat' instead of this demo.
echo.
pause
