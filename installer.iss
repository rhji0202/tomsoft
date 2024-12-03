[Setup]
AppName=Web Viewer
AppVersion=1.0
DefaultDirName={pf}\Web Viewer
DefaultGroupName=Web Viewer
OutputDir=Output
OutputBaseFilename=WebViewerSetup

[Files]
Source: "build\exe.win-amd64-3.8\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs

[Icons]
Name: "{group}\Web Viewer"; Filename: "{app}\main.exe"
Name: "{commondesktop}\Web Viewer"; Filename: "{app}\main.exe" 