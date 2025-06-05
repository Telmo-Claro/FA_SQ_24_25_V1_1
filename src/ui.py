import database
from datetime import datetime
import authenticator
import utils
import logger

class Ui:
    def __init__(self):
        self._logger = logger.Logger()
        self._db = database.Database(self._logger, "urban_mobility")
        self._db.create()
        self._db.add_user("Super", "Administrator", "super_admin", "Admin_123?", "Super Administrator", datetime.now())


    def landing(self):
        try:
            utils.cls()
            while True:
                print(f"Welcome to Urban Mobility!")
                print(f"To navigate, please enter the numerical value")
                print(f"To login, enter th")
                print(f"1) Login")
                print(f"2) Exit")
                choice = input("> ")
                if choice == "2":
                    return
                elif choice == "1":
                    username = input("Username: ")
                    password = input("Password: ")
                    auth = authenticator.Authenticator(self._logger)
                    sa = auth.auth_super_admin(username, password)
                    if sa:
                        self.landing_super_admin(sa)
                    else:
                        print(f"Wrong username or password. Try again!")
                else:
                    print(f"Wrong input! Try again!")
        except Exception as e:
            self._logger.log_error(e, "during landing page navigation")
            print("An error occurred. Sorry for the inconvenience.")

    def landing_super_admin(self, user):
        try:
            while True:
                utils.cls()
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
        except Exception as e:
            self._logger.log_error(e, "during landing page navigation")

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