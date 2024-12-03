from PyInstaller.__main__ import run
import shutil
import os

if __name__ == '__main__':
    # 기존 dist 폴더가 있다면 삭제
    if os.path.exists('dist'):
        shutil.rmtree('dist')
    
    # 기존 build 폴더가 있다면 삭제    
    if os.path.exists('build'):
        shutil.rmtree('build')

    opts = [
        'main.py',
        '--windowed',
        '--name=WebViewer',
        '--add-data=output:output',
        '--target-architecture=arm64',
        '--hidden-import=PyQt5.QtWebEngineWidgets',
        '--hidden-import=PyQt5.QtWebEngine',
        '--hidden-import=PyQt5.QtWebEngineCore',
        '--osx-bundle-identifier=com.yourcompany.webviewer',
        '--clean',
        '--noconfirm',
        '--exclude-module=Qt3D',
        '--exclude-module=QtGamepad',
        '--exclude-module=QtBodymovin'
    ]
    run(opts) 