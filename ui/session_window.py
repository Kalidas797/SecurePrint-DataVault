import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QDesktopWidget, QFileDialog, QMessageBox
from PyQt5.QtCore import Qt, QTimer, QTime
from core.encryption import encrypt_file, decrypt_file, generate_key
from core.print_manager import print_pdf
from core.temp_manager import create_temp_file, cleanup_temp_dir
from core.secure_delete import secure_delete_file

class SessionWindow(QMainWindow):
    def __init__(self, session_manager=None):
        super().__init__()
        self.session_manager = session_manager
        # Generate a session-specific encryption key
        self.key = generate_key()
        
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

        self.label_timer = QLabel("Time Left: 15:00")
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

        # Session Timer (15 minutes = 900 seconds)
        self.time_left = 900 
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000) # Update every second

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def update_timer(self):
        self.time_left -= 1
        
        # Format time as MM:SS
        minutes = self.time_left // 60
        seconds = self.time_left % 60
        self.label_timer.setText(f"Time Left: {minutes:02d}:{seconds:02d}")

        if self.time_left <= 0:
            self.timer.stop()
            self.end_session()

    def add_file(self):
        pass

    def print_file(self):
        if not self.session_manager:
            return

        # 1. Select a PDF file from the session directory
        # Start looking in the session path
        file_path, _ = QFileDialog.getOpenFileName(
            self, 
            "Select Encrypted File", 
            self.session_manager.session_path, 
            "All Files (*.*)"
        )
        
        if not file_path:
            return

        # 2. Decrypt it to a temp directory
        temp_file = create_temp_file(self.session_manager.session_path, "print_mem_file.pdf")
        if not temp_file:
            QMessageBox.warning(self, "Error", "Failed to create temporary file.")
            return

        decrypt_file(file_path, temp_file, self.key)

        # 3. Send the decrypted file to print_pdf()
        print_pdf(temp_file)

        # 4. Wait for the user to finish printing
        QMessageBox.information(
            self, 
            "Printing in Progress", 
            "Please wait for the printing dialog to appear.\n\nOnce printing is complete, click OK to securely delete the file."
        )

        # 5. Securely delete the original encrypted file
        secure_delete_file(file_path)

        # 6. Clean up temp files
        # temp_file is inside the _temp directory, so we clean up the parent of the file
        cleanup_temp_dir(os.path.dirname(temp_file))

    def end_session(self):
        # Stop timer if it's running
        if hasattr(self, 'timer') and self.timer.isActive():
            self.timer.stop()
            
        if self.session_manager:
            self.session_manager.end_session()
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SessionWindow()
    window.show()
    sys.exit(app.exec_())
