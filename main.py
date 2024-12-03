import sys
import os
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class WebViewer:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.web = QWebEngineView()
        
        # HTML 파일의 절대 경로 설정
        current_dir = os.path.dirname(os.path.abspath(__file__))
        html_path = os.path.join(current_dir, 'output', 'index.html')
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
