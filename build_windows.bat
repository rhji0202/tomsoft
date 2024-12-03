@echo off
echo Building WebViewer for Windows...

REM PyInstaller
python setup_windows.py

REM Inno Setup
"C:\Program Files (x86)\Inno Setup 6\ISCC.exe" installer_windows.iss

echo Build complete!
pause 