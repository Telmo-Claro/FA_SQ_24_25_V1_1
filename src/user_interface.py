import authenticator
from helper import Helper

class Ui:
    def __init__(self, logger, database):
        self._logger = logger
        self._db = database

    def landing(self):
        while True:
            Helper.clear_console()
            print("URBAN MOBILITY SYSTEM")
            print("Welcome to Urban Mobility!")
            print("1) Login")
            print("2) Exit")
            choice = input("Please enter a number from the menu above: ")
            print("")

            if choice == "2":
                quit()
            elif choice == "1":
                while True:
                    print("LOGIN")
                    print("If you wish to cancel, enter 'exit' as the username.")
                    username = input("Username: ")
                    password = input("Password: ")
                    print("")

                    if username == "exit":
                        break
                    auth = authenticator.Authenticator(self._logger, self._db)
                    user = auth.auth_user(username, password)
                    
                    if user is False or user is None:
                        print("Wrong username or password. Try again!")
                        input("Press Enter to continue...")
                        continue
                    elif user.role == "Super Administrator":
                        print("Login successful! Redirecting...")
                        self.landing_super_admin(user)
                    elif user.role == "System Administrator":
                        print("You don't exist... yet")
                        input("Press Enter to continue...")
                        break
                    elif user.role == "Service Engineer":
                        print("You don't exist... yet")
                        input("Press Enter to continue...")
                        break
                    else:
                        print("Wrong username or password. Try again!")
                        input("Press Enter to continue...")
            else:
                print("Wrong input! Try again!")
                input("Press Enter to continue...")

    def landing_super_admin(self, user):
        try:
            while True:
                print(f"SUPER ADMINISTRATOR DASHBOARD")
                print(f"Welcome, {user.firstname} {user.lastname}!")
                print("1) Users")
                print("2) Travellers")
                print("3) Scooters")
                print("4) System Services")
                print("5) Logout")
                choice = input("> ")
                print("")

                if choice == "5":
                    self.landing()
                elif choice == "1":
                    while True:
                        print("USER MANAGEMENT")
                        print(f"1) View Users")
                        print(f"2) Add User")
                        print(f"3) Delete User")
                        print(f"4) Update User")
                        print(f"5) Back")
                        choice = input("> ")
                        print("")

                        if choice == "1":
                            if user.view_users(self._db, self._logger):
                                input("Press Enter to continue...")
                            else:
                                print("Failed to view users. Please try again.")
                        elif choice == "2":
                            if user.add_user(self._db, self._logger):
                                print("User added successfully!")
                            else:
                                print("Failed to add user. Please try again.")
                        elif choice == "3":
                            if user.delete_user(self._db, self._logger):
                                print("User deleted successfully!")
                            else:
                                print("Failed to delete user. Please try again.")
                        elif choice == "4":
                            if user.update_user(self._db, self._logger):
                                print("User updated successfully!")
                            else:
                                print("Failed to update user. Please try again.")
                        elif choice == "5":
                            break
                        else:
                            print("Invalid option. Please try again.")
                            input("Press Enter to continue...")

                elif choice == "2":
                    while True:
                        Helper.clear_console()
                        print("TRAVELLER MANAGEMENT")
                        print(f"1) View Travellers")
                        print(f"2) Add Traveller")
                        print(f"3) Update Traveller")
                        print(f"4) Delete Traveller")
                        print(f"5) Back")
                        choice = input("> ")

                        if choice == "1":
                            print("Feature not yet implemented")
                            input("Press Enter to continue...")
                        elif choice == "2":
                            print("Feature not yet implemented")
                            input("Press Enter to continue...")
                        elif choice == "3":
                            print("Feature not yet implemented")
                            input("Press Enter to continue...")
                        elif choice == "4":
                            print("Feature not yet implemented")
                            input("Press Enter to continue...")
                        elif choice == "5":
                            break
                        else:
                            print("Invalid option. Please try again.")
                            input("Press Enter to continue...")

                elif choice == "3":
                    while True:
                        Helper.clear_console()
                        print("SCOOTER MANAGEMENT")
                        print(f"1) View Scooters")
                        print(f"2) Add Scooter")
                        print(f"3) Update Scooter")
                        print(f"4) Delete Scooter")
                        print(f"5) Back")
                        choice = input("> ")
                        if choice == "1":
                            print("Feature not yet implemented")
                            input("Press Enter to continue...")
                        elif choice == "2":
                            print("Feature not yet implemented")
                            input("Press Enter to continue...")
                        elif choice == "3":
                            print("Feature not yet implemented")
                            input("Press Enter to continue...")
                        elif choice == "4":
                            print("Feature not yet implemented")
                            input("Press Enter to continue...")
                        elif choice == "5":
                            break
                        else:
                            print("Invalid option. Please try again.")
                            input("Press Enter to continue...")
                elif choice == "4":
                    while True:
                        Helper.clear_console()
                        print("SYSTEM SERVICES")
                        print("Feature not yet implemented")
                        input("Press Enter to continue...")
                else:
                    print("Invalid option. Please try again.")
                    input("Press Enter to continue...")

        except Exception as e:
            self._logger.error(f"An error occurred in the super admin dashboard: {e}")
            print("An unexpected error occurred. Please try again later.")
            input("Press Enter to continue...")
            self.landing()
