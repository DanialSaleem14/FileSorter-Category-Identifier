#!/usr/bin/env python3
"""
Script to create a portable version of the document organizer
that works without requiring any installations on the client computer.
"""

import os
import sys
import shutil
import subprocess
import zipfile
from pathlib import Path

def create_portable_package():
    """Create a portable package with all dependencies"""
    
    print("Creating portable document organizer package...")
    
    # Create portable directory
    portable_dir = Path("../DocumentOrganizer_Portable")
    if portable_dir.exists():
        shutil.rmtree(portable_dir)
    portable_dir.mkdir()
    
    # Copy main files
    files_to_copy = [
        "organizer",
        "data", 
        "requirements.txt",
        "build_exe.bat",
        "build.spec"
    ]
    
    for item in files_to_copy:
        src = Path(item)
        if src.exists():
            if src.is_dir():
                shutil.copytree(src, portable_dir / item)
            else:
                shutil.copy2(src, portable_dir / item)
    
    # Create portable batch files
    create_portable_batch_files(portable_dir)
    
    # Create requirements for portable version
    create_portable_requirements(portable_dir)
    
    # Create portable spec file
    create_portable_spec(portable_dir)
    
    print(f"Portable package created in: {portable_dir}")
    print("Next steps:")
    print("1. Run 'build_portable.bat' to create the executable")
    print("2. Copy the entire folder to any client computer")
    print("3. Run 'DocumentOrganizer.exe' - no installation required!")

def create_portable_batch_files(portable_dir):
    """Create batch files for portable version"""
    
    # Main executable batch file
    main_bat = portable_dir / "DocumentOrganizer.bat"
    with open(main_bat, 'w') as f:
        f.write("""@echo off
echo Starting Document Organizer...
cd /d "%~dp0"
if exist "DocumentOrganizer.exe" (
    DocumentOrganizer.exe
) else (
    echo Building executable...
    call build_portable.bat
    if exist "DocumentOrganizer.exe" (
        DocumentOrganizer.exe
    ) else (
        echo Error: Could not create executable
        pause
    )
)
""")
    
    # Build portable executable
    build_bat = portable_dir / "build_portable.bat"
    with open(build_bat, 'w') as f:
        f.write("""@echo off
echo Building portable Document Organizer executable...
cd /d "%~dp0"

REM Install required packages
pip install -r requirements.txt --target ./libs --upgrade

REM Build executable with PyInstaller
pyinstaller --onefile --windowed --name DocumentOrganizer --add-data "data;data" --add-data "organizer;organizer" --hidden-import pytesseract --hidden-import cv2 --hidden-import PIL --hidden-import pdfminer --hidden-import pypdf --hidden-import docx --hidden-import pptx --hidden-import openpyxl --hidden-import chardet --hidden-import rapidfuzz --hidden-import rich --hidden-import click organizer/gui.py

REM Copy executable to main directory
if exist "dist\\DocumentOrganizer.exe" (
    copy "dist\\DocumentOrganizer.exe" "DocumentOrganizer.exe"
    echo Executable created successfully!
) else (
    echo Error: Failed to create executable
)

pause
""")
    
    # Organize files batch (portable version)
    organize_bat = portable_dir / "organize_files.bat"
    with open(organize_bat, 'w') as f:
        f.write("""@echo off
echo Organizing files...
cd /d "%~dp0"
if exist "DocumentOrganizer.exe" (
    DocumentOrganizer.exe --mode organize
) else (
    echo Please run build_portable.bat first to create the executable
    pause
)
""")
    
    # GUI batch (portable version)
    gui_bat = portable_dir / "organize_gui.bat"
    with open(gui_bat, 'w') as f:
        f.write("""@echo off
echo Starting Document Organizer GUI...
cd /d "%~dp0"
if exist "DocumentOrganizer.exe" (
    DocumentOrganizer.exe --mode gui
) else (
    echo Please run build_portable.bat first to create the executable
    pause
)
""")

def create_portable_requirements(portable_dir):
    """Create requirements file for portable version"""
    requirements = portable_dir / "requirements.txt"
    with open(requirements, 'w') as f:
        f.write("""# Core dependencies
pytesseract>=0.3.10
opencv-python>=4.8.0
Pillow>=10.0.0
pdfminer.six>=20221105
pypdf>=3.15.0
python-docx>=0.8.11
python-pptx>=0.6.21
openpyxl>=3.1.0
chardet>=5.2.0
rapidfuzz>=3.2.0
rich>=13.0.0
click>=8.1.0

# PyInstaller for creating executable
pyinstaller>=5.13.0

# Additional dependencies
numpy>=1.24.0
""")

def create_portable_spec(portable_dir):
    """Create PyInstaller spec file for portable version"""
    spec_content = """# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['organizer/gui.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('data', 'data'),
        ('organizer', 'organizer'),
    ],
    hiddenimports=[
        'pytesseract',
        'cv2',
        'PIL',
        'pdfminer',
        'pypdf',
        'docx',
        'pptx',
        'openpyxl',
        'chardet',
        'rapidfuzz',
        'rich',
        'click',
        'numpy',
        'tkinter',
        'tkinter.filedialog',
        'tkinter.messagebox',
        'tkinter.simpledialog',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='DocumentOrganizer',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,
)
"""
    
    spec_file = portable_dir / "DocumentOrganizer.spec"
    with open(spec_file, 'w') as f:
        f.write(spec_content)

if __name__ == "__main__":
    create_portable_package()
