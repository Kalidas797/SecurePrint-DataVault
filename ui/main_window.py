import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QDesktopWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
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
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
