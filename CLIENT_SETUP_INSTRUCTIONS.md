# 🚀 Document Organizer - Client Setup Instructions

## ⚠️ **IMPORTANT: First Time Setup Required**

Before using the Document Organizer, you need to install the required Python packages on your system.

## 📋 **Prerequisites**

1. **Python 3.7 or higher** must be installed
   - Download from: https://python.org
   - ⚠️ **CRITICAL**: Check "Add Python to PATH" during installation
   - Verify installation: Open Command Prompt and type `python --version`

## 🔧 **Installation Steps**

### **Option 1: Automatic Installation (Recommended)**
1. **Double-click `install_dependencies.bat`**
2. Wait for installation to complete
3. You're ready to use the organizer!

### **Option 2: Manual Installation**
1. Open Command Prompt in the project folder
2. Run: `pip install -r dependencies/requirements.txt`
3. Wait for installation to complete

## 🎯 **Using the Document Organizer**

### **GUI Mode (Recommended)**
- **Double-click `organize_gui.bat`**
- Select your input folder
- Click "Process Files"
- Files will be organized automatically

### **Command Line Mode**
- **Double-click `organize_files.bat`**
- Follow the prompts
- Files will be processed automatically

## 📁 **Required Dependencies**

The following packages will be installed:
- `click` - Command line interface
- `pdfminer.six` - PDF text extraction
- `pytesseract` - OCR text recognition
- `Pillow` - Image processing
- `python-docx` - Word document processing
- `python-pptx` - PowerPoint processing
- `openpyxl` - Excel processing
- `pypdf` - PDF processing
- `rapidfuzz` - Text matching
- `chardet` - Text encoding detection
- `rich` - Enhanced console output
- `python-dotenv` - Environment variables

## 🆘 **Troubleshooting**

### **Error: "ModuleNotFoundError: No module named 'click'"**
- **Solution**: Run `install_dependencies.bat` first
- This error means Python packages are not installed

### **Error: "Python is not recognized"**
- **Solution**: Install Python from https://python.org
- Make sure to check "Add Python to PATH" during installation

### **Error: "pip is not recognized"**
- **Solution**: Python installation is incomplete
- Reinstall Python and check "Add Python to PATH"

## ✅ **Verification**

After installation, test the setup:
1. Double-click `organize_gui.bat`
2. If the GUI opens without errors, setup is complete!
3. If you see errors, run `install_dependencies.bat` again

## 📞 **Support**

If you encounter any issues:
1. Make sure Python is installed correctly
2. Run `install_dependencies.bat` as administrator
3. Check your internet connection
4. Contact support if problems persist

---
**Ready to organize your documents! 🎉**
