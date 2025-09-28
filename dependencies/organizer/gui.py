import os
import threading
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import json

from .__main__ import process_directory
from .classifier import _load_categories, _save_categories


class App(tk.Tk):
	def __init__(self) -> None:
		super().__init__()
		self.title("Intelligent Document Organizer")
		self.geometry("700x400")

		# Default to Unsorted folder in current directory
		current_dir = os.getcwd()
		unsorted_path = os.path.join(current_dir, "Unsorted")
		
		self.input_var = tk.StringVar(value=unsorted_path)
		self.output_var = tk.StringVar(value="")  # Will auto-set to "Sorted"
		self.interactive_var = tk.BooleanVar(value=False)
		self.dry_run_var = tk.BooleanVar(value=False)
		self.custom_folder_var = tk.StringVar(value="")

		self._build()

	def _build(self) -> None:
		pad = {"padx": 8, "pady": 6}

		row = 0
		# Title
		tk.Label(self, text="Document Organizer", font=("Arial", 14, "bold")).grid(row=row, column=0, columnspan=4, pady=10)
		
		row += 1
		# Instructions
		tk.Label(self, text="1. Place files in 'Unsorted' folder\n2. Click 'Process Files' to organize them\n3. Files will be moved to 'Sorted' folder", 
				justify="left", font=("Arial", 9)).grid(row=row, column=0, columnspan=4, sticky="w", **pad)

		row += 1
		tk.Label(self, text="Unsorted Folder:", font=("Arial", 10, "bold")).grid(row=row, column=0, sticky="w", **pad)
		tk.Entry(self, textvariable=self.input_var, width=50).grid(row=row, column=1, **pad)
		tk.Button(self, text="Browse", command=self._choose_input).grid(row=row, column=2, **pad)

		row += 1
		tk.Label(self, text="Output Folder:", font=("Arial", 10, "bold")).grid(row=row, column=0, sticky="w", **pad)
		tk.Entry(self, textvariable=self.output_var, width=50, state="readonly").grid(row=row, column=1, **pad)
		tk.Label(self, text="(Auto: 'Sorted' folder)", font=("Arial", 8)).grid(row=row, column=2, sticky="w", **pad)

		# Custom Folder Section
		row += 1
		tk.Label(self, text="", font=("Arial", 1)).grid(row=row, column=0, columnspan=4)  # Spacer
		
		row += 1
		tk.Label(self, text="Add Custom Folder:", font=("Arial", 10, "bold")).grid(row=row, column=0, sticky="w", **pad)
		tk.Entry(self, textvariable=self.custom_folder_var, width=40).grid(row=row, column=1, **pad)
		tk.Button(self, text="Add Folder", command=self._add_custom_folder, bg="blue", fg="white").grid(row=row, column=2, **pad)
		tk.Button(self, text="View Categories", command=self._view_categories, bg="orange", fg="white").grid(row=row, column=3, **pad)

		row += 1
		tk.Checkbutton(self, text="Interactive Mode (learn from corrections)", variable=self.interactive_var).grid(row=row, column=0, columnspan=2, sticky="w", **pad)

		row += 1
		tk.Checkbutton(self, text="Dry Run (analyze only, don't move files)", variable=self.dry_run_var).grid(row=row, column=0, columnspan=2, sticky="w", **pad)

		row += 1
		tk.Button(self, text="Process Files", command=self._start, bg="green", fg="white", font=("Arial", 10, "bold")).grid(row=row, column=0, **pad)
		tk.Button(self, text="Exit", command=self.destroy, bg="red", fg="white").grid(row=row, column=1, sticky="w", **pad)

	def _choose_input(self) -> None:
		path = filedialog.askdirectory()
		if path:
			self.input_var.set(path)

	def _choose_output(self) -> None:
		# Output is auto-set, but allow manual override
		path = filedialog.askdirectory()
		if path:
			self.output_var.set(path)

	def _add_custom_folder(self) -> None:
		folder_name = self.custom_folder_var.get().strip()
		if not folder_name:
			messagebox.showwarning("Warning", "Please enter a folder name.")
			return
		
		try:
			# Load current categories
			categories = _load_categories()
			
			# Check if folder already exists
			if folder_name in categories:
				messagebox.showwarning("Warning", f"Folder '{folder_name}' already exists.")
				return
			
			# Add new folder (before "Unknown")
			if "Unknown" in categories:
				unknown_index = categories.index("Unknown")
				categories.insert(unknown_index, folder_name)
			else:
				categories.append(folder_name)
			
			# Save updated categories
			_save_categories(categories)
			
			# Automatically add category name as keyword
			from .classifier import add_custom_keywords
			base_keywords = [folder_name.lower()]
			add_custom_keywords(folder_name, base_keywords)
			
			# Clear input field
			self.custom_folder_var.set("")
			
			messagebox.showinfo("Success", f"Custom folder '{folder_name}' added successfully!\n\nKeywords: {', '.join(base_keywords)}")
			
		except Exception as e:
			messagebox.showerror("Error", f"Failed to add custom folder: {str(e)}")

	def _view_categories(self) -> None:
		try:
			categories = _load_categories()
			
			# Create a new window to display categories
			category_window = tk.Toplevel(self)
			category_window.title("Manage Categories")
			category_window.geometry("600x500")
			category_window.grab_set()  # Make it modal
			
			# Main frame
			main_frame = tk.Frame(category_window)
			main_frame.pack(fill="both", expand=True, padx=10, pady=10)
			
			# Title
			tk.Label(main_frame, text="Current Categories:", font=("Arial", 12, "bold")).pack(anchor="w", pady=(0, 10))
			
			# Create frame for listbox and scrollbar
			list_frame = tk.Frame(main_frame)
			list_frame.pack(fill="both", expand=True, pady=(0, 10))
			
			# Listbox for categories
			listbox = tk.Listbox(list_frame, selectmode=tk.SINGLE, height=15)
			scrollbar = tk.Scrollbar(list_frame, orient="vertical", command=listbox.yview)
			listbox.configure(yscrollcommand=scrollbar.set)
			
			# Insert categories
			for i, category in enumerate(categories, 1):
				listbox.insert(tk.END, f"{i:2d}. {category}")
			
			listbox.pack(side="left", fill="both", expand=True)
			scrollbar.pack(side="right", fill="y")
			
			# Button frame
			button_frame = tk.Frame(main_frame)
			button_frame.pack(fill="x", pady=(10, 0))
			
			# Delete button
			def delete_selected():
				selection = listbox.curselection()
				if not selection:
					messagebox.showwarning("Warning", "Please select a category to delete.")
					return
				
				selected_index = selection[0]
				category_to_delete = categories[selected_index]
				
				# Confirm deletion
				if messagebox.askyesno("Confirm Delete", 
					f"Are you sure you want to delete the category '{category_to_delete}'?\n\nThis action cannot be undone."):
					
					try:
						# Remove from categories list
						categories.pop(selected_index)
						
						# Save updated categories
						_save_categories(categories)
						
						# Refresh the listbox
						listbox.delete(0, tk.END)
						for i, category in enumerate(categories, 1):
							listbox.insert(tk.END, f"{i:2d}. {category}")
						
						messagebox.showinfo("Success", f"Category '{category_to_delete}' deleted successfully!")
						
					except Exception as e:
						messagebox.showerror("Error", f"Failed to delete category: {str(e)}")
			
			# Add new category button
			def add_new_category():
				new_category = simpledialog.askstring("Add Category", "Enter new category name:")
				if new_category and new_category.strip():
					new_category = new_category.strip()
					
					if new_category in categories:
						messagebox.showwarning("Warning", f"Category '{new_category}' already exists.")
						return
					
					try:
						# Add new category (before "Unknown")
						if "Unknown" in categories:
							unknown_index = categories.index("Unknown")
							categories.insert(unknown_index, new_category)
						else:
							categories.append(new_category)
						
						# Save updated categories
						_save_categories(categories)
						
						# Automatically add category name as keyword
						from .classifier import add_custom_keywords
						base_keywords = [new_category.lower()]
						
						# Ask for additional keywords
						keywords_text = simpledialog.askstring("Add Keywords", 
							f"Enter additional keywords for '{new_category}' (comma-separated):\n\nNote: '{new_category}' is automatically added as a keyword.\n\nExample: keyword1, keyword2, keyword3\n\nLeave empty to use only category name as keyword.")
						
						if keywords_text and keywords_text.strip():
							additional_keywords = [kw.strip() for kw in keywords_text.split(",") if kw.strip()]
							base_keywords.extend(additional_keywords)
						
						# Save keywords
						add_custom_keywords(new_category, base_keywords)
						
						# Refresh the listbox
						listbox.delete(0, tk.END)
						for i, category in enumerate(categories, 1):
							listbox.insert(tk.END, f"{i:2d}. {category}")
						
						messagebox.showinfo("Success", f"Category '{new_category}' added successfully!\n\nKeywords: {', '.join(base_keywords)}")
						
					except Exception as e:
						messagebox.showerror("Error", f"Failed to add category: {str(e)}")
			
			# Buttons
			tk.Button(button_frame, text="Delete Selected", command=delete_selected, 
					 bg="red", fg="white", font=("Arial", 10, "bold")).pack(side="left", padx=(0, 10))
			tk.Button(button_frame, text="Add New Category", command=add_new_category, 
					 bg="green", fg="white", font=("Arial", 10, "bold")).pack(side="left", padx=(0, 10))
			tk.Button(button_frame, text="Close", command=category_window.destroy, 
					 bg="gray", fg="white", font=("Arial", 10, "bold")).pack(side="right")
			
		except Exception as e:
			messagebox.showerror("Error", f"Failed to load categories: {str(e)}")

	def _start(self) -> None:
		inp = self.input_var.get().strip()
		if not inp:
			messagebox.showerror("Error", "Please select an input folder.")
			return
		if not os.path.isdir(inp):
			messagebox.showerror("Error", "Input folder does not exist.")
			return
		
		# Auto-set output to "Sorted" folder next to input
		out = self.output_var.get().strip() or None
		if not out:
			parent_dir = os.path.dirname(inp)
			out = os.path.join(parent_dir, "Sorted")
			self.output_var.set(out)
		
		interactive = self.interactive_var.get()
		dry_run = self.dry_run_var.get()

		def run():
			try:
				process_directory(input_dir=inp, output_base=out, interactive=interactive, dry_run=dry_run)
				messagebox.showinfo("Complete", "File processing completed successfully!")
			except Exception as e:
				messagebox.showerror("Error", f"Processing failed: {str(e)}")

		threading.Thread(target=run, daemon=True).start()


def main() -> None:
	app = App()
	app.mainloop()


if __name__ == "__main__":
	main()