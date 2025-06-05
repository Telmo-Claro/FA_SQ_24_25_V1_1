from utils import *
from datetime import datetime

class User:
    def __init__(self, username, password, role, firstname="", lastname="", registrationDate=datetime.now()):
        if role == "Super Administrator":
            self.username = "super_admin"
            self.password = "Admin_123?"
            self.role = "Super Administrator"
            self.firstname = "Super"
            self.lastname = "Administrator"
        else:
            if validate_username(username):
                self.username = username
            else:
                raise ValueError(f"Invalid username: {username}. Must be 8-10 characters long, start with a letter or underscore, and contain only letters, numbers, underscores, apostrophes, and periods.")
            if validate_password(password):
                self.password = password
            else:
                raise ValueError(f"Invalid password: {password}. Must be 12-30 characters long, contain at least one uppercase letter, one lowercase letter, one digit, and one special character.")
            self.role = role
            self.firstname = firstname
            self.lastname = lastname
            self.registrationDate = registrationDate

    def update_password(self):
        while True:
            cls()
            print(f"Please enter your current password to update it.")
            current_password = input(f"Current password: ")
            if current_password == self.password:
                while True:
                    new_password = input(f"New password: ")
                    second_try = input(f"Confirm new password: ")
                    if new_password == second_try:
                        self.password = second_try
                    else:
                        print(f"Passwords do not match. Try again.")
            else:
                print(f"Wrong password. Try again.")