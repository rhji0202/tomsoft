import sys
import os
import shutil
from PyQt5.QtWidgets import (QApplication, QWizard, QWizardPage, QLabel, 
                            QVBoxLayout, QLineEdit, QPushButton, QFileDialog,
                            QProgressBar)
from PyQt5.QtCore import Qt, QThread, pyqtSignal

class InstallThread(QThread):
    progress = pyqtSignal(int)
    finished = pyqtSignal()
    error = pyqtSignal(str)

    def __init__(self, source_dir, install_path):
        super().__init__()
        self.source_dir = source_dir
        self.install_path = install_path

    def run(self):
        try:
            # 설치 디렉토리 생성
            os.makedirs(self.install_path, exist_ok=True)

            # 파일 복사
            total_files = sum([len(files) for _, _, files in os.walk(self.source_dir)])
            copied_files = 0

            for root, _, files in os.walk(self.source_dir):
                for file in files:
                    src_path = os.path.join(root, file)
                    rel_path = os.path.relpath(src_path, self.source_dir)
                    dst_path = os.path.join(self.install_path, rel_path)
                    
                    # 대상 디렉토리 생성
                    os.makedirs(os.path.dirname(dst_path), exist_ok=True)
                    
                    # 파일 복사
                    shutil.copy2(src_path, dst_path)
                    
                    copied_files += 1
                    progress = int((copied_files / total_files) * 100)
                    self.progress.emit(progress)

            # 바로가기 생성
            self.create_shortcut()
            self.finished.emit()

        except Exception as e:
            self.error.emit(str(e))

    def create_shortcut(self):
        # Windows의 경우 바로가기 생성
        if sys.platform == 'win32':
            import winshell
            from win32com.client import Dispatch
            
            desktop = winshell.desktop()
            path = os.path.join(desktop, "WebViewer.lnk")
            target = os.path.join(self.install_path, "WebViewer.exe")
            
            shell = Dispatch('WScript.Shell')
            shortcut = shell.CreateShortCut(path)
            shortcut.Targetpath = target
            shortcut.save()

class WelcomePage(QWizardPage):
    def __init__(self):
        super().__init__()
        self.setTitle('WebViewer 설치 프로그램')
        
        layout = QVBoxLayout()
        label = QLabel('이 마법사는 WebViewer 프로그램을 설치합니다.')
        layout.addWidget(label)
        self.setLayout(layout)

class InstallLocationPage(QWizardPage):
    def __init__(self):
        super().__init__()
        self.setTitle('설치 위치 선택')
        
        layout = QVBoxLayout()
        
        self.path_edit = QLineEdit()
        default_path = os.path.expanduser("~/WebViewer")
        self.path_edit.setText(default_path)
        
        browse_btn = QPushButton('찾아보기...')
        browse_btn.clicked.connect(self.browse_location)
        
        layout.addWidget(QLabel('설치 위치를 선택하세요:'))
        layout.addWidget(self.path_edit)
        layout.addWidget(browse_btn)
        
        self.setLayout(layout)

    def browse_location(self):
        path = QFileDialog.getExistingDirectory(self, '설치 위치 선택')
        if path:
            self.path_edit.setText(path)

class InstallProgressPage(QWizardPage):
    def __init__(self):
        super().__init__()
        self.setTitle('설치 진행 중')
        
        layout = QVBoxLayout()
        self.progress_bar = QProgressBar()
        self.status_label = QLabel('설치를 ��비하고 있습니다...')
        
        layout.addWidget(self.status_label)
        layout.addWidget(self.progress_bar)
        
        self.setLayout(layout)

    def initializePage(self):
        install_path = self.wizard().page(1).path_edit.getText()
        self.install_thread = InstallThread('dist', install_path)
        self.install_thread.progress.connect(self.update_progress)
        self.install_thread.finished.connect(self.installation_finished)
        self.install_thread.error.connect(self.installation_error)
        self.install_thread.start()

    def update_progress(self, value):
        self.progress_bar.setValue(value)
        self.status_label.setText(f'설치 진행 중... {value}%')

    def installation_finished(self):
        self.status_label.setText('설치가 완료되었습니다!')
        self.wizard().next()

    def installation_error(self, error_msg):
        self.status_label.setText(f'오류 발생: {error_msg}')

class CompletionPage(QWizardPage):
    def __init__(self):
        super().__init__()
        self.setTitle('설치 완료')
        
        layout = QVBoxLayout()
        label = QLabel('WebViewer가 성공적으로 설치되었습니다.')
        layout.addWidget(label)
        self.setLayout(layout)

class InstallerWizard(QWizard):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('WebViewer 설치')
        self.setWizardStyle(QWizard.ModernStyle)
        
        self.addPage(WelcomePage())
        self.addPage(InstallLocationPage())
        self.addPage(InstallProgressPage())
        self.addPage(CompletionPage())
        
        self.setMinimumSize(600, 400)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    wizard = InstallerWizard()
    wizard.show()
    sys.exit(app.exec_()) 