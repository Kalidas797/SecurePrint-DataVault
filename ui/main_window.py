import sys
import os

# Ensure the project root is in sys.path for imports to work correctly
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QDesktopWidget
from core.session_manager import SessionManager
from ui.session_window import SessionWindow
from core.secure_delete import secure_delete_directory

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Startup cleanup: securely delete any existing session folders
        sessions_path = os.path.join(project_root, "data", "secure_sessions")
        if os.path.exists(sessions_path):
            for item in os.listdir(sessions_path):
                path = os.path.join(sessions_path, item)
                if os.path.isdir(path):
                    secure_delete_directory(path)

        self.setWindowTitle("SecurePrint – DataVault")
        self.resize(400, 200)
        self.center()
        
        # Central widget setup
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        # Button
        self.start_button = QPushButton("START CUSTOMER SESSION")
        self.start_button.setMinimumHeight(60)  # Make it large
        
        # Connect signal
        self.start_button.clicked.connect(self.start_session)
        
        layout.addWidget(self.start_button)

    def center(self):
        # Logic to center the window on the screen
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def start_session(self):
        manager = SessionManager()
        if manager.start_session():
            self.session_window = SessionWindow(manager)
            self.session_window.show()
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
