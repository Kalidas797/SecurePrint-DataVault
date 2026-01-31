import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QDesktopWidget
from PyQt5.QtCore import Qt

class SessionWindow(QMainWindow):
    def __init__(self, session_manager=None):
        super().__init__()
        self.session_manager = session_manager
        self.setWindowTitle("SecurePrint – Active Session")
        self.resize(500, 300)
        self.center()

        # Central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Labels
        self.label_status = QLabel("Session Active")
        self.label_status.setAlignment(Qt.AlignCenter)
        # Making the status label large/prominent
        font_status = self.label_status.font()
        font_status.setPointSize(16)
        font_status.setBold(True)
        self.label_status.setFont(font_status)

        self.label_timer = QLabel("Time Left: --:--")
        self.label_timer.setAlignment(Qt.AlignCenter)

        # Buttons
        self.btn_add = QPushButton("ADD FILE")
        self.btn_print = QPushButton("PRINT FILE")
        self.btn_end = QPushButton("END SESSION")

        # Connect signals
        self.btn_add.clicked.connect(self.add_file)
        self.btn_print.clicked.connect(self.print_file)
        self.btn_end.clicked.connect(self.end_session)

        # Add widgets to layout
        layout.addWidget(self.label_status)
        layout.addWidget(self.label_timer)
        layout.addSpacing(20)
        layout.addWidget(self.btn_add)
        layout.addWidget(self.btn_print)
        layout.addWidget(self.btn_end)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def add_file(self):
        pass

    def print_file(self):
        pass

    def end_session(self):
        if self.session_manager:
            self.session_manager.end_session()
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SessionWindow()
    window.show()
    sys.exit(app.exec_())
