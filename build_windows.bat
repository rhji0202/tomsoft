@echo off
echo Building WebViewer for Windows...

REM PyInstaller로 실행 파일 생성
python setup_windows.py

REM Inno Setup으로 설치 프로그램 생성
"C:\Program Files (x86)\Inno Setup 6\ISCC.exe" installer_windows.iss

echo Build complete!
pause 