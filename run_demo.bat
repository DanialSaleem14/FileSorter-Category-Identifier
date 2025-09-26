@echo off
echo ========================================
echo   Dokument-Organizer Demo
echo ========================================
echo.

echo Activating virtual environment...
call .venv\Scripts\activate.bat

echo.
echo Creating demo files...
python scripts\make_dummy_data.py

echo.
echo Running document organizer (auto-classify mode)...
python -m organizer process "UnsortedDemo" --output-base "SortedDemo"

echo.
echo ========================================
echo   Demo Complete!
echo ========================================
echo Check the 'SortedDemo' folder to see organized files.
echo.
pause
