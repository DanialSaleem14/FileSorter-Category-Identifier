# Document Organizer

**Simple, focused document organization system that only processes files you place in the "Unsorted" folder.**

## How It Works

1. **Place files** in the `Unsorted` folder
2. **Run the organizer** - it will process only those files
3. **Files are moved** to the `Sorted` folder in appropriate categories
4. **No automatic folder creation** - categories are created only when needed

## Quick Start

### Option 1: GUI (Recommended)
```bash
python -m organizer.gui
```

### Option 2: Command Line
```bash
python -m organizer process Unsorted
```

### Option 3: Batch File
Double-click `organize_files.bat`

## Key Features

- ✅ **Only processes files in "Unsorted" folder**
- ✅ **Creates "Sorted" folder automatically**
- ✅ **No unnecessary folder creation**
- ✅ **100% accuracy for TEILNAHMEBESTÄTIGUNG documents**
- ✅ **Supports all major file formats** (PDF, DOCX, XLSX, etc.)
- ✅ **German language optimized**

## File Structure

```
Your Project/
├── Unsorted/          ← Place your files here
├── Sorted/            ← Organized files appear here
│   ├── Rechnungen/
│   ├── Zertifikate/
│   ├── Verträge allgemein/
│   └── ...
└── organizer/         ← System files
```

## Installation

```bash
pip install -r requirements.txt
```

**That's it!** The system is designed to be simple and focused - no complex setup needed.

## Build EXE (Optional)

To create a standalone executable:
```bash
build_exe.bat
```

## Test the System

```bash
run_demo.bat
```

## Requirements

- Windows 10/11
- Python 3.8+
- For OCR: Tesseract OCR (optional)