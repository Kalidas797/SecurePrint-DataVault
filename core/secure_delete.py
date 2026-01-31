import os
import shutil

def secure_delete_file(file_path, passes=3):
    try:
        if not os.path.isfile(file_path):
            return

        file_size = os.path.getsize(file_path)
        
        # Open file once per pass to overwrite
        for _ in range(passes):
            with open(file_path, "wb") as f:
                # Write in chunks to handle large files efficiently
                remaining = file_size
                chunk_size = 65536  # 64KB
                while remaining > 0:
                    write_size = min(remaining, chunk_size)
                    f.write(os.urandom(write_size))
                    remaining -= write_size
                
                f.flush()
                os.fsync(f.fileno())
        
        os.remove(file_path)
    except OSError:
        pass

def secure_delete_directory(directory_path):
    try:
        if not os.path.exists(directory_path):
            return

        # Walk bottom-up to delete files before directories
        for root, dirs, files in os.walk(directory_path, topdown=False):
            for file in files:
                file_path = os.path.join(root, file)
                secure_delete_file(file_path)
            
            for dir_name in dirs:
                dir_path = os.path.join(root, dir_name)
                try:
                    os.rmdir(dir_path)
                except OSError:
                    pass
        
        # Finally remove the root directory itself
        os.rmdir(directory_path)
    except OSError:
        pass
