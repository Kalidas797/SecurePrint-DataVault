import os
import datetime

class AuditLogger:
    def __init__(self, session_id, log_dir="logs"):
        self.session_id = session_id
        self.log_dir = os.path.abspath(log_dir)
        self.log_file = os.path.join(self.log_dir, f"audit_{self.session_id}.txt")
        
        try:
            if not os.path.exists(self.log_dir):
                os.makedirs(self.log_dir)
        except OSError:
            pass

    def _write_log(self, event_type):
        timestamp = datetime.datetime.now().isoformat()
        try:
            with open(self.log_file, "a") as f:
                f.write(f"[{timestamp}] {event_type}\n")
        except OSError:
            pass

    def log_session_started(self):
        self._write_log("SESSION_STARTED")

    def log_file_added(self):
        self._write_log("FILE_ADDED")

    def log_file_printed(self):
        self._write_log("FILE_PRINTED")

    def log_file_destroyed(self):
        self._write_log("FILE_DESTROYED")

    def log_session_ended(self):
        self._write_log("SESSION_ENDED")
