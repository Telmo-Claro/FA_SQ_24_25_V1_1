import database
from datetime import datetime
import auth
import os

class Ui():
    def __init__(self, logger):
        self._logger = logger
        self._db = database.Database(self._logger, "urban_mobility")
        self._db.create()
    
    def cls(self):
        """Clear the console screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def Landing(self):
        try:
            self.cls()
            while True:
                print(f"Welcome to Urban Mobility!")
                print(f"To navigate, please enter the numerical value")
                print(f"Log in as: ")
                print(f"1) Super Administrator")
                print(f"2) System Administrator")
                print(f"3) Service Engineer")
                print(f"4) Exit")
                choice = input("> ")
                if choice == "4":
                    return
                elif choice == "1":
                    username = input("Username: ")
                    password = input("Password: ")
                    temp_auth = auth.Authenticator(self._logger)
                    sa = temp_auth.auth_super_admin(username, password)
                    if not sa:
                        print("Wrong username or password. Try again!")
                    else:
                        self.landing_super_admin(sa)
                elif choice == "2":
                    username = input("Username: ")
                    password = input("Password: ")
                elif choice == "3":
                    username = input("Username: ")
                    password = input("Password: ")
                else:
                    print(f"Wrong input! Try again!")
        except Exception as e:
            self._logger.log_error(e, "during landing page navigation")
            print("An error occurred. Sorry for the inconvenience.")

    def landing_super_admin(self, user):
        while True:
            print(f"Welcome {user.firstname} {user.lastname}!")
            print(f"To navigate, please enter the numerical value")
            print(f"Choose a sub-menu")
            print(f"1) Users")
            print(f"2) Exit")
            choice = input("> ")
            if choice == "2":
                return
            elif choice == "1":
                print(f"2) Add User")
                print(f"1) View Users")
                print(f"3) Delete User")
                print(f"4) Update User")
                print(f"5) Back")
                choice = input("> ")
                if choice == "1":
                    self.add_user_super_admin(user)
            else:
                print(f"Wrong input! Try again!")

    def add_user_super_admin(self, user):
        try:
            print(f"Great!")
            first_name = input("First name: ")
            last_name = input("Last name: ")
            username = input("Username: ")
            password = input("Password: ")
            print(f"Please choose a role:")
            print(f"1) System Administrator")
            print(f"2) System Engineer")
            role = input("Role: ")
            while role not in ["1", "2"]:
                if role == "1":
                    role = "System Administrator"
                elif role == "2":
                    role = "Service Engineer"
                else:
                    print(f"Invalid role selected. Try again.")
            registration_date = datetime.now()
            if not self._db.add_user(user, first_name, last_name, username, password, role, registration_date):
                    print(f"Sorry, didn't work!")
        except Exception as e:
            self._logger.log_error(e, "SUPER ADMIN USER ADDITION")