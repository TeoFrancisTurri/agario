block_cipher = None

a = Analysis(
    ['client/main.py'],
    pathex=['.'],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=['server'],
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='agario-client',
    debug=False,
    strip=False,
    upx=False,
    console=False,
    cipher=block_cipher,
)
