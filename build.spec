# PyInstaller spec for building GUI app
# Build with: pyinstaller build.spec

block_cipher = None

from PyInstaller.utils.hooks import collect_submodules

a = Analysis([
	'organizer\\gui.py',
],
	pathex=['.'],
	binaries=[],
	datas=[('data', 'data')],
	hiddenimports=collect_submodules('pptx') + collect_submodules('openpyxl'),
	hookspath=[],
	runtime_hooks=[],
	excludes=[],
	cipher=block_cipher,
	noarchive=False)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(
	pyz,
	a.scripts,
	a.binaries,
	a.zipfiles,
	a.datas,
	name='Dokument-Organizer',
	debug=False,
	bootloader_ignore_signals=False,
	strip=False,
	upx=True,
	console=False,
	icon=None)
