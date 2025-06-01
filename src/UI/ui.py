import src.utils.validate as validate

class ui:

    def landing(self):
        while True:
            print(f"Welcome to Urban Mobility!")
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
                if validate.validate_super_admin(username, password) is True:
                    print(f"Welcome!")
            elif choice == "2":
                username = input("Username: ")
                password = input("Password: ")
            elif choice == "3":
                username = input("Username: ")
                password = input("Password: ")
            else:
                print(f"Wrong input! Try again!")
    def landing_service_engineer(self):
        while True:
            print(f"Nothing to see here! (yet)")
    def landing_system_admin(self):
        while True:
            print(f"Nothing to see here! (yet)")
    def landing_super_admin(self):
        while True:
            print(f"Nothing to see here! (yet)")