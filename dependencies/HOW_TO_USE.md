# 📁 Document Organizer - Complete Usage Guide

## 🚀 **How to Run the Document Organizer**

### **Method 1: GUI Mode (Recommended)**

1. **Double-click `organize_gui.bat`**
2. **The GUI will open with these features:**
   - **Input Folder**: Select your unsorted files folder (default: "Unsorted")
   - **Output Folder**: Where organized files will go (default: "Sorted")
   - **Add Custom Folder**: Add new category names
   - **View Categories**: See all available categories and manage them
   - **Interactive Mode**: Learn from your corrections
   - **Dry Run**: Test without moving files

3. **Click "Process Files"** to organize your documents

### **Method 2: Command Line Mode**

1. **Open Command Prompt** in the project folder
2. **Run this command:**
   ```bash
   python -m dependencies.organizer.__main__ process "Unsorted" --output-base "Sorted"
   ```

### **Method 3: Using Batch Files**

1. **Place files** in `Unsorted` folder
2. **Double-click `organize_files.bat`** for command line processing
3. **Double-click `organize_gui.bat`** for GUI processing

## 🎯 **Key Features**

### **✅ Smart Classification**
- **OCR Text Recognition**: Reads text from images and PDFs
- **36 German Categories**: Pre-configured for German documents
- **Intelligent Matching**: Uses keywords and content analysis

### **✅ Custom Folder Management**
- **Add Custom Folders**: Click "Add Folder" button
- **View All Categories**: Click "View Categories" button
- **Delete Categories**: Select and delete unwanted categories
- **Add Keywords**: When adding new categories, you can add keywords for better classification

### **✅ Interactive Learning**
- **Learn from Corrections**: Enable "Interactive Mode"
- **Improve Accuracy**: System learns from your corrections
- **Custom Keywords**: Add specific keywords for your documents

## 📋 **Available Categories**

- **Persönlich** - Personal documents
- **Ausweis / Reisepass** - ID documents
- **Führerschein** - Driver's license
- **Zeugnisse & Zertifikate** - Certificates and diplomas
- **Medizinische Unterlagen** - Medical documents
- **Impfpass / Gesundheitsnachweise** - Health certificates
- **Finanzen** - Financial documents
- **Bankunterlagen** - Bank documents
- **Rechnungen** - Invoices
- **Verträge** - Contracts
- **Versicherungen** - Insurance documents
- **Steuern** - Tax documents
- **Wohnen** - Housing documents
- **Mietverträge / Kaufvertrag** - Rental/purchase contracts
- **Nebenkostenabrechnungen** - Utility bills
- **Reparaturen / Handwerker** - Repairs and craftsmen
- **Möbel & Einrichtung** - Furniture and furnishings
- **Arbeit & Ausbildung** - Work and education
- **Arbeitsverträge** - Employment contracts
- **Lohnabrechnungen** - Payroll documents
- **Bewerbungen** - Job applications
- **Weiterbildung** - Further education
- **Fahrzeuge** - Vehicle documents
- **KFZ-Brief / Schein** - Vehicle registration
- **Rechnungen / Reparaturen / Inspektionen** - Vehicle invoices/repairs
- **Kaufverträge** - Purchase contracts
- **Familie & Freizeit** - Family and leisure
- **Kinderunterlagen** - Children's documents
- **Haustiere** - Pet documents
- **Urlaubsunterlagen** - Vacation documents
- **Vereinsmitgliedschaften** - Club memberships
- **Sonstiges** - Miscellaneous
- **Wichtige Korrespondenz** - Important correspondence
- **Garantien & Bedienungsanleitungen** - Warranties and manuals
- **Private Projekte** - Private projects

## 🔧 **How to Add Custom Categories**

1. **Open the GUI** (double-click `organize_gui.bat`)
2. **Click "View Categories"** button
3. **Click "Add New Category"** button
4. **Enter category name** (e.g., "Meine Kategorie")
5. **Enter keywords** (comma-separated, e.g., "keyword1, keyword2, keyword3")
6. **Click OK** - Category is now available for classification

## 📁 **File Organization Process**

1. **Place files** in the `Unsorted` folder
2. **Run the organizer** (GUI or command line)
3. **Files are analyzed** using OCR and text recognition
4. **Files are classified** into appropriate categories
5. **Files are moved** to `Sorted` folder in subfolders by category

## 🎉 **Ready to Use!**

The Document Organizer is now fully functional with:
- ✅ **Working GUI** with custom folder management
- ✅ **OCR Text Recognition** for images and PDFs
- ✅ **Smart Classification** with 36+ categories
- ✅ **Custom Categories** - add unlimited new categories
- ✅ **Interactive Learning** - improves over time
- ✅ **Easy to Use** - just double-click and go!

**Start organizing your documents now!** 🚀
