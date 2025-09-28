# 🔧 Client Troubleshooting Guide

## 🚨 **Common Issues and Solutions**

### **Issue 1: Images Going to "Fotos & Bilder" Instead of Proper Categories**

**Problem**: Images with text content (like invoices, certificates) are being moved to "Fotos & Bilder" instead of their correct categories.

**Solution**:
1. **Run `install_dependencies.bat`** - This installs Tesseract OCR
2. **Run `test_ocr.bat`** - This tests if OCR is working properly
3. **If OCR test fails**, run `install_tesseract_manual.bat`

**What's Fixed**:
- ✅ Improved OCR accuracy with better image preprocessing
- ✅ Added fuzzy matching to handle OCR errors
- ✅ Better language detection (German + English)
- ✅ Multiple OCR configurations for better results

### **Issue 2: "ModuleNotFoundError: No module named 'click'"**

**Problem**: Python packages are not installed.

**Solution**:
1. **Run `install_dependencies.bat`** (one-time setup)
2. **Wait for installation to complete**
3. **Try running the organizer again**

### **Issue 3: OCR Not Working / No Text Extracted**

**Problem**: Tesseract OCR is not installed or not working.

**Solutions**:
1. **Automatic**: Run `install_dependencies.bat`
2. **Manual**: Run `install_tesseract_manual.bat`
3. **Manual Download**: 
   - Go to: https://github.com/UB-Mannheim/tesseract/wiki
   - Download Windows installer
   - Install to: `C:\Program Files\Tesseract-OCR\`
   - **IMPORTANT**: Select German language pack during installation

### **Issue 4: Files Not Being Classified Correctly**

**Problem**: Documents are going to wrong categories or "Unknown".

**Solutions**:
1. **Check OCR**: Run `test_ocr.bat` to verify OCR is working
2. **Add Custom Keywords**: Use GUI to add keywords for your documents
3. **Check File Names**: Use descriptive filenames (e.g., "rechnung_2024.pdf")

## 🛠️ **Diagnostic Tools**

### **1. OCR Test**
```bash
test_ocr.bat
```
- Tests if Tesseract OCR is installed
- Tests if OCR can read text from images
- Shows available language packs

### **2. Dependency Check**
```bash
install_dependencies.bat
```
- Installs all required Python packages
- Installs Tesseract OCR (if possible)
- Tests OCR functionality

### **3. Manual Tesseract Install**
```bash
install_tesseract_manual.bat
```
- Downloads Tesseract installer automatically
- Guides through installation process
- Tests installation

## 📋 **Step-by-Step Client Setup**

### **For New Clients:**
1. **Install Python** from https://python.org
   - ✅ Check "Add Python to PATH" during installation
2. **Run `install_dependencies.bat`**
   - Wait for all packages to install
   - Wait for Tesseract OCR to install
3. **Run `test_ocr.bat`** to verify everything works
4. **Ready to use!** Run `organize_gui.bat`

### **For Existing Clients with Issues:**
1. **Run `install_dependencies.bat`** again
2. **Run `test_ocr.bat`** to check OCR
3. **If OCR fails**, run `install_tesseract_manual.bat`
4. **Test with a few files** to verify everything works

## 🎯 **What's Been Fixed**

### **OCR Improvements:**
- ✅ Better image preprocessing (resizing, quality improvement)
- ✅ Multiple OCR configurations for better accuracy
- ✅ German + English language support
- ✅ Better error handling and debugging

### **Classification Improvements:**
- ✅ Fuzzy matching for OCR errors (e.g., "echnung" → "rechnung")
- ✅ Better keyword prioritization
- ✅ Improved filename-based fallback
- ✅ Removed conflicting test categories

### **Installation Improvements:**
- ✅ Automatic Tesseract OCR installation
- ✅ Better error messages and guidance
- ✅ Multiple installation methods
- ✅ Comprehensive testing tools

## 🚀 **Expected Results**

After proper setup, you should see:
- ✅ Images with text are classified by content, not just as "Fotos & Bilder"
- ✅ Invoices go to "Rechnungen"
- ✅ Certificates go to "Zertifikate"
- ✅ Contracts go to "Verträge"
- ✅ OCR works on German and English text
- ✅ Fuzzy matching handles OCR errors

## 📞 **Still Having Issues?**

1. **Check the logs** - Look for error messages in the console
2. **Run diagnostic tools** - Use `test_ocr.bat` and `install_dependencies.bat`
3. **Check file permissions** - Make sure you can write to the Sorted folder
4. **Try with different files** - Test with various document types
5. **Contact support** - Provide error messages and system details

---
**Your Document Organizer should now work perfectly with full OCR support! 🎉**
