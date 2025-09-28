# 📁 Intelligent Document Organizer

A powerful, intelligent document organization system that automatically categorizes and sorts files based on their content using OCR (Optical Character Recognition) and smart text analysis.

## 🚀 Features

### ✨ **Smart Classification**
- **OCR Text Recognition** - Reads text from images, PDFs, and documents
- **36+ German Categories** - Pre-configured for German document types
- **Intelligent Matching** - Uses keywords and content analysis
- **Multi-language Support** - German and English OCR

### 🎯 **Custom Category Management**
- **Add Custom Folders** - Create unlimited new categories
- **Delete Categories** - Remove unwanted categories
- **View All Categories** - Manage categories in a user-friendly interface
- **Add Keywords** - Specify keywords for better classification

### 🔧 **User Interface**
- **Modern GUI** - Easy-to-use graphical interface
- **Command Line** - Batch processing capabilities
- **Interactive Mode** - Learn from corrections
- **Dry Run Mode** - Test without moving files

### 📱 **Portable & Standalone**
- **Plug-and-Play** - Works on any Windows computer
- **No Installation Required** - Self-contained executable
- **Batch Files** - Easy one-click execution

## 🎯 **Available Categories**

### **Personal Documents**
- Persönlich, Ausweis / Reisepass, Führerschein
- Zeugnisse & Zertifikate, Medizinische Unterlagen
- Impfpass / Gesundheitsnachweise

### **Financial Documents**
- Finanzen, Bankunterlagen, Rechnungen
- Verträge, Versicherungen, Steuern

### **Housing & Living**
- Wohnen, Mietverträge / Kaufvertrag
- Nebenkostenabrechnungen, Reparaturen / Handwerker
- Möbel & Einrichtung

### **Work & Education**
- Arbeit & Ausbildung, Arbeitsverträge
- Lohnabrechnungen, Bewerbungen
- Zeugnisse / Zertifikate, Weiterbildung

### **Vehicles**
- Fahrzeuge, KFZ-Brief / Schein
- Versicherungen, Rechnungen / Reparaturen / Inspektionen
- Kaufverträge

### **Family & Leisure**
- Familie & Freizeit, Kinderunterlagen
- Haustiere, Urlaubsunterlagen
- Vereinsmitgliedschaften

### **Miscellaneous**
- Sonstiges, Wichtige Korrespondenz
- Garantien & Bedienungsanleitungen
- Private Projekte

## 🚀 **Quick Start**

### **Method 1: GUI Mode (Recommended)**
1. **Download** the project files
2. **Double-click** `organize_gui.bat`
3. **Place files** in the `Unsorted` folder
4. **Click "Process Files"** to organize
5. **Use "Add Custom Folder"** to add new categories

### **Method 2: Command Line**
```bash
python -m dependencies.organizer.__main__ process "Unsorted" --output-base "Sorted"
```

### **Method 3: Batch Files**
- **`organize_gui.bat`** - GUI mode
- **`organize_files.bat`** - Command line mode

## 📋 **Installation Requirements**

### **For Development:**
```bash
pip install -r dependencies/requirements.txt
```

### **For Standalone Use:**
- **Windows 10/11** (64-bit)
- **No additional software required** - Everything included!

## 🔧 **How It Works**

1. **Text Extraction** - OCR reads text from images and documents
2. **Content Analysis** - Analyzes text for keywords and patterns
3. **Smart Classification** - Matches content to appropriate categories
4. **File Organization** - Moves files to correct folders automatically
5. **Learning** - Interactive mode improves accuracy over time

## 📁 **Project Structure**

```
📁 Document Organizer/
├── 📁 dependencies/           # Source code and data
│   ├── 📁 organizer/         # Main application code
│   ├── 📁 data/             # Categories and learning data
│   └── 📁 scripts/          # Utility scripts
├── 📁 Sorted/               # Organized files (output)
├── 📁 Unsorted/             # Input files to organize
├── 📄 organize_gui.bat      # GUI launcher
├── 📄 organize_files.bat    # Command line launcher
└── 📄 create_standalone.bat # Build standalone executable
```

## 🎯 **Usage Examples**

### **Adding Custom Categories:**
1. Open GUI → Click "View Categories"
2. Click "Add New Category"
3. Enter category name (e.g., "Meine Kategorie")
4. Add keywords (e.g., "keyword1, keyword2, keyword3")
5. Click OK - Category is now available!

### **Processing Files:**
1. Place files in `Unsorted` folder
2. Run `organize_gui.bat`
3. Click "Process Files"
4. Files are automatically organized into categories

## 🔍 **Supported File Types**

- **Images:** PNG, JPG, JPEG, TIFF, BMP
- **Documents:** PDF, DOCX, DOC, TXT
- **Spreadsheets:** XLSX, XLS, CSV
- **Presentations:** PPTX, PPT
- **And more!**

## 🎉 **Key Benefits**

- ✅ **Automatic Organization** - No manual sorting required
- ✅ **OCR Technology** - Reads text from images
- ✅ **Custom Categories** - Add unlimited new categories
- ✅ **Smart Learning** - Improves accuracy over time
- ✅ **Portable** - Works on any Windows computer
- ✅ **User-Friendly** - Simple GUI interface
- ✅ **Batch Processing** - Handle large numbers of files

## 📚 **Documentation**

- **`HOW_TO_USE.md`** - Complete usage guide
- **`CLIENT_INSTRUCTIONS.md`** - Client deployment instructions
- **`FINAL_STATUS.md`** - Project status and features

## 🤝 **Contributing**

Feel free to contribute to this project by:
- Adding new document categories
- Improving OCR accuracy
- Enhancing the user interface
- Adding new file type support

## 📄 **License**

This project is open source and available under the MIT License.

## 🎯 **Ready to Organize!**

Your Document Organizer is now ready to intelligently sort and categorize all your documents automatically! 🚀

---

**GitHub Repository:** [FileSorter-Category-Identifier](https://github.com/DanialSaleem14/FileSorter-Category-Identifier)

**Created with ❤️ for efficient document management**
