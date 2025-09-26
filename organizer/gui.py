import os
import threading
import tkinter as tk
from tkinter import filedialog, messagebox

from .__main__ import process_directory


class App(tk.Tk):
	def __init__(self) -> None:
		super().__init__()
		self.title("Intelligent Document Organizer")
		self.geometry("560x260")

		self.input_var = tk.StringVar()
		self.output_var = tk.StringVar()
		self.interactive_var = tk.BooleanVar(value=False)
		self.dry_run_var = tk.BooleanVar(value=False)

		self._build()

	def _build(self) -> None:
		pad = {"padx": 8, "pady": 6}

		row = 0
		tk = tk
		tk.Label(self, text="Unsortierter Eingangsordner:").grid(row=row, column=0, sticky="w", **pad)
		tk.Entry(self, textvariable=self.input_var, width=50).grid(row=row, column=1, **pad)
		tk.Button(self, text="Durchsuchen", command=self._choose_input).grid(row=row, column=2, **pad)

		row += 1
		tk.Label(self, text="Zielbasis für sortierte Dateien:").grid(row=row, column=0, sticky="w", **pad)
		tk.Entry(self, textvariable=self.output_var, width=50).grid(row=row, column=1, **pad)
		tk.Button(self, text="Durchsuchen", command=self._choose_output).grid(row=row, column=2, **pad)

		row += 1
		tk.Checkbutton(self, text="Interaktiv (lernen)", variable=self.interactive_var).grid(row=row, column=0, columnspan=2, sticky="w", **pad)

		row += 1
		tk.Checkbutton(self, text="Trockenlauf (nur analysieren)", variable=self.dry_run_var).grid(row=row, column=0, columnspan=2, sticky="w", **pad)

		row += 1
		tk.Button(self, text="Start", command=self._start).grid(row=row, column=0, **pad)
		tk.Button(self, text="Beenden", command=self.destroy).grid(row=row, column=1, sticky="w", **pad)

	def _choose_input(self) -> None:
		path = filedialog.askdirectory()
		if path:
			self.input_var.set(path)

	def _choose_output(self) -> None:
		path = filedialog.askdirectory()
		if path:
			self.output_var.set(path)

	def _start(self) -> None:
		inp = self.input_var.get().strip()
		if not inp:
			messagebox.showerror("Fehler", "Bitte Eingangsordner auswählen.")
			return
		if not os.path.isdir(inp):
			messagebox.showerror("Fehler", "Eingangsordner existiert nicht.")
			return
		out = self.output_var.get().strip() or None
		interactive = self.interactive_var.get()
		dry_run = self.dry_run_var.get()

		def run():
			try:
				process_directory(input_dir=inp, output_base=out, interactive=interactive, dry_run=dry_run)
				messagebox.showinfo("Fertig", "Verarbeitung abgeschlossen.")
			except Exception as e:
				messagebox.showerror("Fehler", str(e))

		threading.Thread(target=run, daemon=True).start()


def main() -> None:
	app = App()
	app.mainloop()


if __name__ == "__main__":
	main()
