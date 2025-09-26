import os
import shutil
import time
from typing import Tuple


def _safe_filename(path: str) -> str:
	base, name = os.path.split(path)
	stem, ext = os.path.splitext(name)
	candidate = name
	counter = 1
	while os.path.exists(os.path.join(base, candidate)):
		candidate = f"{stem} ({counter}){ext}"
		counter += 1
	return os.path.join(base, candidate)


def ensure_category_dir(base_dir: str, category: str) -> str:
	# Sanitize folder name for Windows
	safe_name = category.replace("/", "_").replace("\\", "_").replace(":", "_").replace("*", "_").replace("?", "_").replace("\"", "_").replace("<", "_").replace(">", "_").replace("|", "_")
	path = os.path.join(base_dir, safe_name)
	os.makedirs(path, exist_ok=True)
	return path


def move_to_category(file_path: str, base_dir: str, category: str) -> str:
	dest_dir = ensure_category_dir(base_dir, category)
	filename = os.path.basename(file_path)
	target_path = os.path.join(dest_dir, filename)
	if os.path.exists(target_path):
		target_path = _safe_filename(target_path)
	
	# Try to move with retry for file locks
	max_retries = 3
	for attempt in range(max_retries):
		try:
			# First try to copy, then remove original
			shutil.copy2(file_path, target_path)
			# Verify copy was successful
			if os.path.exists(target_path) and os.path.getsize(target_path) == os.path.getsize(file_path):
				try:
					os.remove(file_path)
					print(f"[green]Moved:[/] {os.path.basename(file_path)}")
				except PermissionError:
					print(f"[yellow]Copied (original locked):[/] {os.path.basename(file_path)}")
				return target_path
			else:
				raise Exception("Copy verification failed")
		except (PermissionError, OSError) as e:
			if attempt < max_retries - 1:
				print(f"[yellow]File locked, retrying in 1 second... (attempt {attempt + 1}/{max_retries})[/]")
				time.sleep(1)
			else:
				# Final fallback: just copy and leave original
				try:
					shutil.copy2(file_path, target_path)
					print(f"[yellow]Copied (could not move):[/] {os.path.basename(file_path)}")
					return target_path
				except Exception as final_e:
					print(f"[red]Failed to process file: {file_path} - {final_e}[/]")
					raise final_e
		except Exception as e:
			print(f"[red]Error processing file: {e}[/]")
			raise e
