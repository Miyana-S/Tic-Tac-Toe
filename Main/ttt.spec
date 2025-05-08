# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['ttt.py'],
    pathex=[],
    binaries=[],
    datas=[('Beach', 'Beach'), ('Forest', 'Forest'), ('Sounds', 'Sounds'), ('Star', 'Star'), ('draw-icon.png', '.'), ('icon2.png', '.'), ('icon2tab.ico', '.'), ('theop1.png', '.'), ('theop2.png', '.'), ('theop3.png', '.'), ('win-icon.png', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='ttt',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['icon2tab.ico'],
)
