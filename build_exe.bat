@echo off
echo ========================================
echo   Dokument-Organizer EXE Builder
echo ========================================
echo.

echo Activating virtual environment...
call .venv\Scripts\activate.bat

echo.
echo Installing PyInstaller if needed...
pip install pyinstaller

echo.
echo Building executable...
pyinstaller build.spec

echo.
echo ========================================
echo   Build Complete!
echo ========================================
echo The executable is located at:
echo   dist\Dokument-Organizer.exe
echo.
echo You can now distribute this EXE to your client.
echo.
pause
