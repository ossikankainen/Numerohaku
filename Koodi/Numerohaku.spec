# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['Numerohaku.py'],
             pathex=['C:\\Users\\ossik\\Documents\\Numerohaku\\Koodi'],
             binaries=[('chromedriver.exe', '.'), ('geckodriver.exe', '.')],
             datas=[('sukunimet_uusi_2000.csv', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Numerohaku',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
