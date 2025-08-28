# -*- mode: python ; coding: utf-8 -*-

# pip3 install --upgrade pip pyinstaller
# pyinstaller pyproject_as_one_exec.spec

block_cipher = None

a = Analysis(
    ['image_grid_mark/main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('image_grid_mark/assets/ico.png', 'image_grid_mark/assets')
    ],
    hiddenimports=[
        'PIL',
        'PIL._tkinter_finder',
        'PIL._tkinter_finder',
        'PIL.Image',
        'PIL.ImageTk'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='image_grid_mark',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    icon='image_grid_mark/assets/ico.png',
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
