@echo off
echo ========================================
echo OCR Test - Document Organizer
echo ========================================
echo.
echo This script will test OCR functionality on your system.
echo.

REM Check if Python is available
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH!
    echo Please install Python from https://python.org
    pause
    exit /b 1
)

echo Python found! Testing OCR...
echo.

REM Test OCR functionality
python -c "
import sys
sys.path.insert(0, 'dependencies')
try:
    import pytesseract
    from PIL import Image
    import tempfile
    import os
    
    print('Testing Tesseract OCR installation...')
    
    # Create a test image with text
    img = Image.new('RGB', (200, 50), color='white')
    from PIL import ImageDraw, ImageFont
    draw = ImageDraw.Draw(img)
    
    # Try to use a default font
    try:
        font = ImageFont.load_default()
    except:
        font = None
    
    draw.text((10, 15), 'Test OCR Text', fill='black', font=font)
    
    # Save test image
    test_img_path = 'test_ocr_image.png'
    img.save(test_img_path)
    
    # Test OCR
    try:
        text = pytesseract.image_to_string(img, lang='eng')
        print(f'OCR Test Result: \"{text.strip()}\"')
        
        if 'test' in text.lower() and 'ocr' in text.lower():
            print('✅ OCR is working correctly!')
        else:
            print('⚠️ OCR is working but may have accuracy issues')
            
    except Exception as e:
        print(f'❌ OCR failed: {e}')
        print('This means Tesseract OCR is not properly installed')
        
    # Clean up
    if os.path.exists(test_img_path):
        os.remove(test_img_path)
        
    # Test language packs
    print('\\nTesting language packs...')
    try:
        langs = pytesseract.get_languages()
        print(f'Available languages: {langs}')
        
        if 'deu' in langs:
            print('✅ German language pack is available')
        else:
            print('⚠️ German language pack not found')
            
        if 'eng' in langs:
            print('✅ English language pack is available')
        else:
            print('⚠️ English language pack not found')
            
    except Exception as e:
        print(f'❌ Could not check language packs: {e}')
        
except ImportError as e:
    print(f'❌ Missing required packages: {e}')
    print('Please run install_dependencies.bat first')
except Exception as e:
    print(f'❌ Unexpected error: {e}')
"

echo.
echo ========================================
echo OCR Test Complete
echo ========================================
echo.
pause
