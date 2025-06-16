from cryptography.fernet import Fernet
from pathlib import Path
import re
import os
import platform
import hashlib
import string
import random
from datetime import datetime

class Helper:

    @staticmethod
    def print_header(title):
        """Prints header with custom text"""
        width = 60
        print("\n" + "=" * width)
        print(f"{title.center(width)}")
        print("=" * width + "\n")

    @staticmethod
    def get_input(prompt, allow_empty=False):
        """Gets user input with a quit option"""
        while True:
            value = input(prompt).strip()
            if value.lower().strip() == 'q':
                print("\nExiting to main menu...")
                return False
            if value or allow_empty:
                return value
            print("Input cannot be empty. Please try again or 'q' to quit.")

    @staticmethod
    def utils_hash(value):
        """Returns a hashed string"""
        return hashlib.sha256(value.encode()).hexdigest()

    @staticmethod
    def validate_username(username):
        """Validates the username"""
        username_regex = re.compile(r'^[_a-zA-Z][a-zA-Z0-9_\'\.]{7,9}$', re.IGNORECASE)
        while bool(username_regex.match(username)) is False:
            print("Username invalid.")
            print("Username must be 8-10 characters long, start with a letter or underscore, and can contain letters, numbers, underscores, apostrophes, and periods.")
            username = input("Please enter a valid username: ")
        return username

    @staticmethod
    def validate_password(password):
        """Validates the password"""
        password_regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[~!@#$%&_\-+=`|\\(){}[\]:\;\'<>,\.\?/])[A-Za-z\d~!@#$%&_\-+=`|\\(){}[\]:\;\'<>,\.\?/]{12,30}$')
        while bool(password_regex.match(password)) is False:
            print("Password invalid.")
            print("Password must be 12-30 characters long, contain at least one uppercase letter, one lowercase letter, one number, and one special character.")
            password = input("Please enter a valid password: ")
        return password
    
    @staticmethod
    def random_password_generator(length=12):
        """Generate a random password that matches the security regex"""
        password_regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[~!@#$%&_\-+=`|\\(){}[\]:\;\'<>,\.\?/])[A-Za-z\d~!@#$%&_\-+=`|\\(){}[\]:\;\'<>,\.\?/]{12,30}$')
        characters = string.ascii_letters + string.digits + string.punctuation

        while True:
            password = ''.join(random.choice(characters) for _ in range(length))
            if password_regex.match(password):
                return password

    @staticmethod
    def symmetric_get_key():
        """Gets the encryption key from a file"""
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

    @staticmethod
    def clear_console():
        """Clears the console screen across different operating systems"""
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')  # For Linux and macOS

    "Scooter Related Helpers"
    @staticmethod
    def validate_serial_number(serial_number):
        pattern = re.compile(r'^[a-zA-Z0-9]{10,17}$')
        return bool(pattern.match(serial_number))

    @staticmethod
    def validate_location(location):
        # Rotterdam boundaries
        rotterdam_north = 51.96
        rotterdam_south = 51.89
        rotterdam_west = 4.35
        rotterdam_east = 4.55

        try:
            # Split and clean the input
            parts = location.strip().split(',')
            if len(parts) != 2:
                return False

            lat = parts[0].strip()
            lon = parts[1].strip()

            # Validate format: check if they are numbers and have exactly 5 decimal places
            lat_parts = lat.split('.')
            lon_parts = lon.split('.')

            # Check if each coordinate has exactly one decimal point and a valid decimal part
            if (len(lat_parts) != 2 or len(lon_parts) != 2 or
                    not lat_parts[0].replace('-', '').isdigit() or
                    not lon_parts[0].replace('-', '').isdigit() or
                    not lat_parts[1].isdigit() or
                    not lon_parts[1].isdigit() or
                    len(lat_parts[1]) != 5 or
                    len(lon_parts[1]) != 5):
                return False

            # Convert to float for boundary comparison
            lat_float = float(lat)
            lon_float = float(lon)

            # Check if within Rotterdam boundaries
            if (rotterdam_south <= lat_float <= rotterdam_north and
                    rotterdam_west <= lon_float <= rotterdam_east):
                return True

            return False

        except:
            return False

    @staticmethod
    def validate_last_maintenance_date(last_maintenance_date):
        pattern = re.compile(r'^(?P<year>2[0-9]{3})-(?P<month>0[1-9]|1[0-2])-(?P<day>0[1-9]|[12][0-9]|3[01])$')
        match = pattern.match(last_maintenance_date)

        if not match:
            return False

        try:
            datetime.strptime(last_maintenance_date, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    @staticmethod
    def validate_zip_code(zip_code):
        pattern = re.compile(r'^[1-9][0-9]{3}[A-Z]{2}$')
        return bool(pattern.match(zip_code))

    @staticmethod
    def validate_driving_license(license_number):
        pattern = re.compile(r'^[A-Z]{1,2}\d{7}$')
        return bool(re.match(pattern, license_number))
