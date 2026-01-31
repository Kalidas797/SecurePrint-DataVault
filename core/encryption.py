from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_file(input_path, output_path, key):
    try:
        f = Fernet(key)
        with open(input_path, 'rb') as file:
            file_data = file.read()
        
        encrypted_data = f.encrypt(file_data)
        
        with open(output_path, 'wb') as file:
            file.write(encrypted_data)
    except Exception:
        pass

def decrypt_file(input_path, output_path, key):
    try:
        f = Fernet(key)
        with open(input_path, 'rb') as file:
            encrypted_data = file.read()
        
        decrypted_data = f.decrypt(encrypted_data)
        
        with open(output_path, 'wb') as file:
            file.write(decrypted_data)
    except Exception:
        pass
