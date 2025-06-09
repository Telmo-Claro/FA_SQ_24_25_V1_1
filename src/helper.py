from cryptography.fernet import Fernet
from pathlib import Path
import re
import os
import subprocess
import platform
import hashlib

class Helper:
    @staticmethod
    def print_header(title):
        """Prints header with custom text"""
        width = 60
        print("\n" + "=" * width)
        print(f"{title.center(width)}")
        print("=" * width + "\n")

    @staticmethod
    def utils_hash(value):
        """Returns a hashed string"""
        return hashlib.sha256(value.encode()).hexdigest()

    @staticmethod
    def validate_username(username):
        """Validates the username"""
        username_regex = re.compile(r'^[_a-zA-Z][a-zA-Z0-9_\'\.]{7,9}$', re.IGNORECASE)
        return bool(username_regex.match(username))

    @staticmethod
    def validate_password(password):
        """Validates the password"""
        password_regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[~!@#$%&_\-+=`|\\(){}[\]:\;\'<>,\.\?/])[A-Za-z\d~!@#$%&_\-+=`|\\(){}[\]:\;\'<>,\.\?/]{12,30}$')
        return bool(password_regex.match(password))

    @staticmethod
    def symmetric_get_key():
        """Gets the encryption key from file"""
        key_path = Path(__file__).parent / "secret.key"
        with open(key_path, "rb") as key_file:
            return key_file.read()

    @classmethod
    def symmetric_encrypt(cls, plaintext):
        """Encrypts plaintext with symmetric encryption using Fernet"""
        key = cls.symmetric_get_key()
        engine = Fernet(key)
        return engine.encrypt(plaintext.encode())

    @classmethod
    def symmetric_decrypt(cls, encrypted):
        """Decrypts encrypted text with symmetric encryption using Fernet"""
        key = cls.symmetric_get_key()
        engine = Fernet(key)
        return engine.decrypt(encrypted).decode()