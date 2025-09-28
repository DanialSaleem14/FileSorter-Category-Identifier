@echo off
echo Setting up portable Tesseract OCR...

REM Download Tesseract portable version
echo Downloading Tesseract OCR...
powershell -Command "& {Invoke-WebRequest -Uri 'https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.4.0.20240606.exe' -OutFile 'tesseract_installer.exe'}"

REM Extract Tesseract
echo Extracting Tesseract...
tesseract_installer.exe /S /D=%~dp0tesseract

REM Clean up installer
del tesseract_installer.exe

echo Tesseract setup complete!
