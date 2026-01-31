import os
import shutil

def create_temp_file(session_path, filename):
    try:
        temp_dir = os.path.join(session_path, "_temp")
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)
        
        file_path = os.path.join(temp_dir, filename)
        # Create an empty file to ensure it exists
        with open(file_path, 'w'):
            pass
            
        return file_path
    except OSError:
        return None

def cleanup_temp_dir(temp_dir):
    try:
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
    except OSError:
        pass
