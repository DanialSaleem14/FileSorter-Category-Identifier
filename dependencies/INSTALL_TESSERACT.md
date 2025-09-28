# Tesseract OCR Installation Guide

For optimal image text recognition, install Tesseract OCR:

## Windows Installation

### Option 1: Direct Download (Recommended)
1. Download Tesseract from: https://github.com/UB-Mannheim/tesseract/wiki
2. Install the Windows installer
3. Add Tesseract to your PATH or set environment variable:
   ```cmd
   setx TESSERACT_PATH "C:\Program Files\Tesseract-OCR\tesseract.exe"
   ```

### Option 2: Using Chocolatey
```cmd
choco install tesseract
```

### Option 3: Using Scoop
```cmd
scoop install tesseract
```

## After Installation

1. Restart your command prompt/PowerShell
2. Test installation:
   ```cmd
   tesseract --version
   ```
3. Run the document organizer - it will now use full OCR capabilities

## Fallback System

If Tesseract is not installed, the system uses filename-based classification:
- Files with "certificate", "zertifikat" in name → Zertifikate
- Files with "invoice", "rechnung" in name → Rechnungen  
- Files with "reminder", "mahnung" in name → Mahnungen
- Other images → Fotos & Bilder

## Language Support

The system supports:
- German (deu) - Primary
- English (eng) - Secondary
- Combined (deu+eng) - Best results

## Troubleshooting

If OCR still doesn't work:
1. Check Tesseract is in PATH: `where tesseract`
2. Set TESSERACT_PATH environment variable
3. Restart the application
4. Check file permissions

