### Intelligent Document Organizer (Windows)

This tool ingests mixed files (images, PDFs, DOCX, PPTX, XLSX, etc.), extracts text, classifies them (German categories), then moves each file into an appropriate folder. If a file cannot be classified, it is placed into `Unknown`. Interactive corrections are remembered.

### Quick start (GUI)
- Double-click with Python: `organizer/gui.py` (or run `python -m organizer.gui`)
- Choose input folder and optional output base, select options, click Start.

### Build a one-file EXE (no Python needed for end user)
- **Single-click build:** Double-click `build_exe.bat`
- **Manual build:**
```bash
. .venv/Scripts/Activate.ps1
pip install pyinstaller
pyinstaller build.spec
```
The EXE will be in `dist/Dokument-Organizer.exe`. Give this file to your client. They can double-click it.

### Test the system
- **Run demo:** Double-click `run_demo.bat` to create sample files and test the organizer

### Requirements
- Windows 10/11
- For OCR on images: Tesseract OCR `https://github.com/UB-Mannheim/tesseract/wiki`
  - Add to PATH or set `TESSERACT_PATH` in `.env`

### CLI (alternative)
```bash
python -m organizer process "C:\\path\\to\\incoming" --interactive
```

### Categories (German)
Configured in `data/categories.json` at first run. Keyword rules are in `organizer/classifier.py`.
