from cryptography.fernet import Fernet


def cls(): # clears the console
    import os
    os.system('cls' if os.name=='nt' else 'clear')

def utils_hash(value): # returns a hashed string
    import hashlib
    return hashlib.sha256(value.encode()).hexdigest()

def validate_username(username): # validates the username
    import re
    username_regex = re.compile(r'^[_a-zA-Z][a-zA-Z0-9_\'\.]{7,9}$', re.IGNORECASE)
    if username_regex.match(username):
        return True
    else:
        return False

def validate_password(password): # validates the password
    import re
    password_regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[~!@#$%&_\-+=`|\\(){}[\]:\;\'<>,\.\?/])[A-Za-z\d~!@#$%&_\-+=`|\\(){}[\]:\;\'<>,\.\?/]{12,30}$')
    if password_regex.match(password):
        return True
    else:
        return False

def symmetric_get_key():
    from pathlib import Path
    key_path = Path(__file__).parent / "secret.key"
    with open(key_path, "rb") as key_file:
        return key_file.read()

def symmetric_encrypt(plaintext): # encrypts plaintext with symmetric encryption using Fernet
    key = symmetric_get_key()
    engine = Fernet(key)
    encrypted = engine.encrypt(plaintext.encode())
    return encrypted

def symmetric_decrypt(encrypted): # decrypts encrypted text with symmetric encryption using Fernet
    key = symmetric_get_key()
    engine = Fernet(key)
    decrypted = engine.decrypt(encrypted).decode()
    return decrypted