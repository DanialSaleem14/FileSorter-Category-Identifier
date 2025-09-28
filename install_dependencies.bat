@echo off
echo ========================================
echo Document Organizer - Complete Setup
echo ========================================
echo.
echo This script will install all required dependencies including OCR.
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
echo Installing Tesseract OCR for image text recognition...
echo.

REM Check if Tesseract is already installed
python -c "import pytesseract; from PIL import Image; img = Image.new('RGB', (10, 10)); pytesseract.image_to_string(img)" >nul 2>&1
if %errorlevel% equ 0 (
    echo Tesseract OCR is already installed and working!
) else (
    echo Tesseract OCR not found, attempting installation...
    
    REM Try to install Tesseract using winget (Windows 10/11)
    winget install --id UB-Mannheim.TesseractOCR --accept-package-agreements --accept-source-agreements >nul 2>&1
    if %errorlevel% equ 0 (
        echo Tesseract OCR installed successfully via winget!
    ) else (
        echo winget not available, trying alternative installation...
        
        REM Try chocolatey if available
        choco install tesseract -y >nul 2>&1
        if %errorlevel% equ 0 (
            echo Tesseract OCR installed successfully via Chocolatey!
        ) else (
            echo.
            echo WARNING: Could not automatically install Tesseract OCR!
            echo.
            echo Please choose one of these options:
            echo 1. Run install_tesseract_manual.bat for automatic download and install
            echo 2. Manually install from: https://github.com/UB-Mannheim/tesseract/wiki
            echo.
            echo IMPORTANT: Make sure to install German language pack during installation!
            echo.
        )
    )
)

echo.
echo Testing OCR functionality...
python -c "import pytesseract; from PIL import Image; import tempfile; import os; img = Image.new('RGB', (100, 30), color='white'); img.save('test_ocr.png'); print('OCR Test:', pytesseract.image_to_string(img).strip() or 'OCR not working'); os.remove('test_ocr.png')" 2>nul

echo.
echo ========================================
echo Installation completed!
echo ========================================
echo.
echo You can now run the Document Organizer:
echo - Double-click organize_gui.bat for GUI mode
echo - Double-click organize_files.bat for command line mode
echo.
echo NOTE: If OCR is not working, please manually install Tesseract OCR
echo from: https://github.com/UB-Mannheim/tesseract/wiki
echo.
pause
