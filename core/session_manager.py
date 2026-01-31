import os
import uuid
from core.secure_delete import secure_delete_directory

class SessionManager:
    def __init__(self, base_path="data/secure_sessions"):
        self.session_id = str(uuid.uuid4())
        self.base_path = os.path.abspath(base_path)
        self.session_path = os.path.join(self.base_path, self.session_id)

    def start_session(self):
        try:
            os.makedirs(self.session_path, exist_ok=True)
            return True
        except OSError:
            return False

    def end_session(self):
        try:
            secure_delete_directory(self.session_path)
            return True
        except OSError:
            return False
