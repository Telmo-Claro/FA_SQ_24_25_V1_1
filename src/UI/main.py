from src.utils.auth import *
from src.UI.super_admin import *
from src.logs.logger import *

def landing():
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
            try:
                auth_super_admin(username, password)
                sa = auth_super_admin(username, password)
                if not sa:
                    print("Wrong username or password. Try again!")
                else:
                    landing_super_admin(sa)
            except Exception as e:
                log_exception(e, "during super admin login")

        elif choice == "2":
            username = input("Username: ")
            password = input("Password: ")
        elif choice == "3":
            username = input("Username: ")
            password = input("Password: ")
        else:
            print(f"Wrong input! Try again!")