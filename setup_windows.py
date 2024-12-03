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
        '--onefile',  # 단일 실행 파일로 생성
        '--windowed',
        '--name=WebViewer_Setup',
        '--add-data=output;output',  # Windows는 세미콜론(;) 사용
        '--hidden-import=PyQt5.QtWebEngineWidgets',
        '--hidden-import=PyQt5.QtWebEngine',
        '--hidden-import=PyQt5.QtWebEngineCore',
        '--icon=app.ico',  # Windows 아이콘
        '--clean',
        '--noconfirm',
        '--exclude-module=Qt3D',
        '--exclude-module=QtGamepad',
        '--exclude-module=QtBodymovin',
        '--uac-admin',  # 관리자 권한 요청
    ]
    run(opts) 