@echo off
echo ========================================
echo Manual Tesseract OCR Installation
echo ========================================
echo.
echo This script will help you install Tesseract OCR manually.
echo.

echo Step 1: Downloading Tesseract OCR...
echo.

REM Try to download using PowerShell
powershell -Command "& {[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; Invoke-WebRequest -Uri 'https://github.com/UB-Mannheim/tesseract/releases/download/v5.3.3.20231005/tesseract-ocr-w64-setup-5.3.3.20231005.exe' -OutFile 'tesseract-installer.exe'}" 2>nul

if exist tesseract-installer.exe (
    echo ✅ Download successful!
    echo.
    echo Step 2: Running Tesseract installer...
    echo.
    echo IMPORTANT: During installation, make sure to:
    echo 1. Install to default location: C:\Program Files\Tesseract-OCR\
    echo 2. Check "Additional language data" and select German
    echo 3. Check "Add to PATH" option
    echo.
    echo Starting installer...
    start /wait tesseract-installer.exe
    
    echo.
    echo Step 3: Cleaning up...
    del tesseract-installer.exe
    
    echo.
    echo Step 4: Testing installation...
    python -c "
import sys
sys.path.insert(0, 'dependencies')
try:
    import pytesseract
    from PIL import Image
    img = Image.new('RGB', (100, 30), color='white')
    text = pytesseract.image_to_string(img)
    print('✅ Tesseract OCR installed successfully!')
    print('You can now use the Document Organizer with full OCR support.')
except Exception as e:
    print(f'❌ Installation test failed: {e}')
    print('Please try running the installer again or install manually.')
"
    
) else (
    echo ❌ Download failed!
    echo.
    echo Please manually install Tesseract OCR:
    echo 1. Go to: https://github.com/UB-Mannheim/tesseract/wiki
    echo 2. Download the latest Windows installer
    echo 3. Run the installer and select German language pack
    echo 4. Install to: C:\Program Files\Tesseract-OCR\
    echo.
)

echo.
echo ========================================
echo Installation Complete
echo ========================================
echo.
pause
