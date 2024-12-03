import sys
import os
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class WebViewer:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.web = QWebEngineView()
        
        # PyInstaller로 패키징된 경우 프로그램이 설치된 경로를 찾음
        if hasattr(sys, '_MEIPASS'):  # PyInstaller로 패키징된 경우
            current_dir = os.path.dirname(sys.argv[0])  # 실행 파일 경로 (설치된 경로)
        else:
            current_dir = os.path.dirname(os.path.abspath(__file__))  # 개발 환경에서 실행 중

        # HTML 파일의 절대 경로 설정
        html_path = os.path.join(current_dir, 'output', 'index.html')

        # 경로가 올바른지 확인
        if not os.path.exists(html_path):
            print(f"Error: HTML file not found at {html_path}")
        else:
            print(f"Loading HTML file from: {html_path}")
        
        # 웹 페이지 로드
        self.web.setUrl(QUrl.fromLocalFile(html_path))
        
        # 창 크기 설정
        self.web.resize(1024, 768)
        self.web.setWindowTitle('Web Viewer')

    def run(self):
        self.web.show()
        sys.exit(self.app.exec_())

if __name__ == '__main__':
    viewer = WebViewer()
    viewer.run()
