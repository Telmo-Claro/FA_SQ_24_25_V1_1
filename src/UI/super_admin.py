from datetime import datetime
from src.data import database
from src.logs.logger import log_exception


def landing_super_admin(user):
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
                add_user_super_admin(user)
        else:
            print(f"Wrong input! Try again!")

def add_user_super_admin(user):
    print(f"Great!")
    first_name = input("First name: ")
    last_name = input("Last name: ")
    username = input("Username: ")
    password = input("Password: ")
    print(f"Please choose a role:")
    print(f"1) System Administrator")
    print(f"2) System Engineer")
    role = input("Role: ")
    registration_date = datetime.now()
    db = database.Database("Urban Mobility")
    try:
        if not db.add_user(user, first_name, last_name, username, password, role, registration_date):
            print(f"Sorry, didn't work!")
    except Exception as e:
        log_exception(e, "add_user_super_admin")
