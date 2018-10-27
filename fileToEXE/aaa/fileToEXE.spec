# -*- mode: python -*-

block_cipher = None


a = Analysis(['..\\fileToEXE.py'],
             pathex=['E:\\Python_Test\\aTest\\fileToEXE', 'E:\\Python_Test\\aTest\\fileToEXE\\aaa'],
             binaries=[],
             datas=[],
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
          name='fileToEXE',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True , icon='E:\\Python_Test\\aTest\\fileToEXE\\zanghuICO.ico')
