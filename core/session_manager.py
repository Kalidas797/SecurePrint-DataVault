import os
import shutil
import uuid

class SessionManager:
    def __init__(self, base_path="data/secure_sessions"):
        """
        Initialize the SessionManager.
        
        Args:
            base_path (str): The base directory for storing session folders. 
                             Defaults to "data/secure_sessions".
        """
        self.session_id = str(uuid.uuid4())
        # Ensure path is absolute for safety and clarity
        self.base_path = os.path.abspath(base_path)
        self.session_path = os.path.join(self.base_path, self.session_id)

    def start_session(self):
        """
        Start the session by creating the session directory.
        """
        try:
            if not os.path.exists(self.session_path):
                os.makedirs(self.session_path)
                print(f"Session started: {self.session_id}")
                print(f"Session directory created: {self.session_path}")
            else:
                print(f"Session directory already exists: {self.session_path}")
        except OSError as e:
            print(f"Error creating session directory: {e}")

    def end_session(self):
        """
        End the session by deleting the session directory and its contents.
        """
        try:
            if os.path.exists(self.session_path):
                shutil.rmtree(self.session_path)
                print(f"Session ended: {self.session_id}")
                print(f"Session directory deleted: {self.session_path}")
            else:
                print(f"Session directory not found: {self.session_path}")
        except OSError as e:
            print(f"Error deleting session directory: {e}")

if __name__ == "__main__":
    # Basic test
    print("Initializing Session Manager...")
    manager = SessionManager()
    
    print("Starting Session...")
    manager.start_session()
    
    input("Press Enter to end session and cleanup...")
    
    print("Ending Session...")
    manager.end_session()
