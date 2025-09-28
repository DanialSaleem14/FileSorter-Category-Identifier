import os
from typing import Optional
import click
from rich import print

from .extractors import extract_text_from_file
from .classifier import classify_text, learn
from .organize import move_to_category


def _detect_category_from_extension(path: str) -> Optional[str]:
	ext = os.path.splitext(path)[1].lower()
	if ext in {".ppt", ".pptx"}:
		return "Präsentationen"
	if ext in {".xlsx", ".xls", ".csv"}:
		return "Spreadsheets"
	if ext in {".png", ".jpg", ".jpeg", ".tif", ".tiff"}:
		return "Fotos & Bilder"
	if ext in {".mp3", ".wav", ".mp4", ".mkv"}:
		return "Musik & Videos"
	return None


def process_directory(input_dir: str, output_base: Optional[str] = None, interactive: bool = False, dry_run: bool = False) -> None:
	"""Core processing function used by CLI and GUI.

	- input_dir: folder containing unsorted files
	- output_base: destination base folder for sorted files (created if missing)
	- interactive: prompt for category confirmation and learn corrections
	- dry_run: analyze only, do not move files
	"""
	base = output_base or os.path.join(input_dir, "organized")
	os.makedirs(base, exist_ok=True)

	for root, _, files in os.walk(input_dir):
		# Skip the organized output itself
		if os.path.abspath(root).startswith(os.path.abspath(base)):
			continue
		for name in files:
			path = os.path.join(root, name)
			# Extract text then classify
			text = extract_text_from_file(path)
			pred = classify_text(text)
			
			# Special handling for images - try filename analysis if OCR failed
			if pred == "Unknown" and text.strip() == "":
				ext = os.path.splitext(path)[1].lower()
				if ext in {".png", ".jpg", ".jpeg", ".tif", ".tiff"}:
					# Try to classify based on filename patterns
					filename_lower = name.lower()
					if any(keyword in filename_lower for keyword in ["rechnung", "invoice", "bill"]):
						pred = "Rechnungen"
					elif any(keyword in filename_lower for keyword in ["zertifikat", "certificate", "zeugnis", "diploma"]):
						pred = "Zertifikate"
					elif any(keyword in filename_lower for keyword in ["vertrag", "contract", "agreement"]):
						pred = "Verträge"
					elif any(keyword in filename_lower for keyword in ["versicherung", "insurance"]):
						pred = "Versicherungen"
					elif any(keyword in filename_lower for keyword in ["ausweis", "pass", "passport", "id"]):
						pred = "Persönlich"
					elif any(keyword in filename_lower for keyword in ["screenshot", "screen", "bildschirm"]):
						pred = "Fotos & Bilder"
					else:
						# Default to extension-based classification for images
						ext_hint = _detect_category_from_extension(path)
						if ext_hint:
							pred = ext_hint
			elif pred == "Unknown":
				# For non-images, use extension hints
				ext_hint = _detect_category_from_extension(path)
				if ext_hint:
					pred = ext_hint

			chosen = pred
			if interactive:
				print(f"[cyan]File:[/] {path}")
				print(f"[yellow]Predicted:[/] {pred}")
				resp = click.prompt("Category (Enter to accept, or type new)", default=pred, show_default=True)
				chosen = resp.strip() or pred
				if chosen != pred:
					learn(text, chosen)
			else:
				# Auto-classify without user input
				print(f"[cyan]File:[/] {path}")
				print(f"[yellow]Auto-classified as:[/] {chosen}")

			print(f"[green]Category:[/] {chosen}")
			if not dry_run:
				try:
					moved = move_to_category(path, base, chosen)
					print(f"[blue]Moved to:[/] {moved}")
				except Exception as e:
					print(f"[red]Failed to process {os.path.basename(path)}: {e}[/]")
					continue


@click.group()
def cli() -> None:
	"""Intelligent Document Organizer."""


@cli.command()
@click.argument("input_dir", type=click.Path(exists=True, file_okay=False))
@click.option("--output-base", envvar="OUTPUT_BASE", default=None, help="Destination base folder for sorted files")
@click.option("--interactive", is_flag=True, help="Ask to confirm/override category and learn from corrections")
@click.option("--dry-run", is_flag=True, help="Analyze without moving files")
def process(input_dir: str, output_base: Optional[str], interactive: bool, dry_run: bool) -> None:
	"""Process all files in INPUT_DIR recursively and organize them."""
	process_directory(input_dir=input_dir, output_base=output_base, interactive=interactive, dry_run=dry_run)


if __name__ == "__main__":
	cli()
