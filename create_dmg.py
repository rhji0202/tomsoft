import os
import subprocess

def create_dmg():
    # 앱 이름과 버전
    APP_NAME = "WebViewer"
    VERSION = "1.0"
    
    # DMG 생성에 필요한 경로들
    dist_path = "dist"
    app_path = os.path.join(dist_path, f"{APP_NAME}.app")
    dmg_path = os.path.join(dist_path, f"{APP_NAME}-{VERSION}.dmg")
    
    # Applications 폴더로의 심볼릭 링크 생성
    applications_link = os.path.join(dist_path, "Applications")
    if not os.path.exists(applications_link):
        os.symlink("/Applications", applications_link)
    
    # create-dmg 명령어 실행
    cmd = [
        "create-dmg",
        "--volname", f"{APP_NAME} Installer",
        "--window-pos", "200", "120",
        "--window-size", "800", "400",
        "--icon-size", "100",
        "--icon", f"{APP_NAME}.app", "200", "190",
        "--hide-extension", f"{APP_NAME}.app",
        "--app-drop-link", "600", "185",
        dmg_path,
        app_path
    ]
    
    subprocess.run(cmd)

if __name__ == "__main__":
    create_dmg() 