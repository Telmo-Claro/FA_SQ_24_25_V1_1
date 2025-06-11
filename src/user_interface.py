import authenticator
from helper import Helper

class Ui:
    def __init__(self, logger, database):
        self._logger = logger
        self._db = database

    def landing(self):
        while True:
            print("URBAN MOBILITY SYSTEM")
            print("Welcome to Urban Mobility!")
            print("1) Login")
            print("Q) Exit")
            choice = input("> ").strip().upper()
            print("")

            if choice == "Q":
                quit()
            elif choice == "1":
                while True:
                    print("LOGIN")
                    print("If you wish to cancel, enter 'exit' as the username.")
                    username = input("Username: ").lower().strip()
                    password = input("Password: ").strip()
                    print("")

                    if username == "exit":
                        break
                    auth = authenticator.Authenticator(self._logger, self._db)
                    user = auth.auth_user(username, password)
                    
                    if user is False or user is None:
                        print("Wrong username or password. Try again!")
                        input("Press Enter to continue...")
                        self.landing()
                    elif user.role == "Super Administrator":
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
        self._logger.log_info(user=user,
                              activity_description="Accessed Super Administrator Dashboard",
                              additional_info="")
        try:
            while True:
                print(f"SUPER ADMINISTRATOR DASHBOARD")
                print(f"Welcome, {user.firstname} {user.lastname}!")
                print("1) User Management")
                print("2) Backup Management")
                print("3) Data Management")
                print("Q) Logout")
                choice = input("> ").strip().lower()
                print("")

                if choice == "q":
                    self.landing()
                elif choice == "1":
                    self.user_management_super_admin(user)
                elif choice == "2":
                    self.backup_management_super_admin(user)
                elif choice == "3":
                    self.data_management_super_admin(user)
                else:
                    print("Invalid option. Please try again.")
                    input("Press Enter to continue...")

        except Exception as e:
            self._logger.log_error(user=user,
                                  activity_description="An unexpected error occurred in the Super Administrator Dashboard",
                                  additional_info=e)
            print("An unexpected error occurred. Please try again later.")
            input("Press Enter to continue...")
            self.landing()

    def user_management_super_admin(self, user):
        self._logger.log_info(user=user,
                              activity_description="Accessed User Management",
                              additional_info="")
        try:
            while True:
                print("================= USER MANAGEMENT =================")
                print("================= System Administrator =================")
                print(f"1) Add new System Administrator")
                print(f"2) Modify or update System Administrator")
                print(f"3) Delete System Administrator")
                print(f"4) Reset System Administrator password (temporary)")
                print("================= Service Engineer =================")
                print(f"5) Add new Service Engineer")
                print(f"6) Modify or update Service Engineer")
                print(f"7) Delete Service Engineer")
                print(f"8) Reset Service Engineer password (temporary)")
                print("================= Other =================")
                print(f"9) View Users")
                print(f"Q) Back")
                choice = input("> ").strip().lower()
                print("")

                if choice == "q":
                    break
                elif choice == "1":
                    if user.add_new_system_admin(self._db, self._logger):
                        print("System Administrator added successfully!")
                        print("")
                    else:
                        print("Failed to add System Administrator. Please try again.")
                        print("")
                elif choice == "2":
                    if user.update_system_admin(self._db, self._logger):
                        print("User updated successfully!")
                        print("")
                    else:
                        print("Failed to update user. Please try again.")
                        print("")
                elif choice == "3":
                    if user.delete_system_admin(self._db, self._logger):
                        print("User deleted successfully!")
                        print("")
                    else:
                        print("Failed to delete user. Please try again.")
                        print("")
                elif choice == "4":
                    if user.reset_system_admin_password(self._db, self._logger):
                        print("User updated successfully!")
                        print("")
                    else:
                        print("Failed to update user. Please try again.")
                        print("")
                elif choice == "5":
                    if user.add_new_service_engineer(self._db, self._logger):
                        print("Service Engineer added successfully!")
                        print("")
                    else:
                        print("Failed to add Service Engineer. Please try again.")
                        print("")
                elif choice == "6":
                    if user.update_service_engineer(self._db, self._logger):
                        print("Service Engineer updated successfully!")
                        print("")
                    else:
                        print("Failed to update Service Engineer. Please try again.")
                        print("")
                elif choice == "7":
                    if user.delete_service_engineer(self._db, self._logger):
                        print("Service Engineer deleted successfully!")
                        print("")
                    else:
                        print("Failed to delete Service Engineer. Please try again.")
                        print("")
                elif choice == "8":
                    if user.reset_service_engineer_password(self._db, self._logger):
                        print("Service Engineer password reset successfully!")
                        print("")
                    else:
                        print("Failed to reset Service Engineer password. Please try again.")
                        print("")
                elif choice == "9":
                    if user.view_users(self._db, self._logger):
                        input("Press Enter to continue...")
                    else:
                        print("Failed to view users. Please try again.")
                        print("")
                else:
                    print("Invalid option. Please try again.")
                    input("Press Enter to continue...")
        except Exception as e:
            self._logger.log_error(user=user,
                                  activity_description="An unexpected error occurred in User Management",
                                  additional_info=e)
            print("An unexpected error occurred. Please try again later.")
            input("Press Enter to continue...")
            self.landing_super_admin(user)

    def backup_management_super_admin(self, user):
        while True:
            print("================= BACKUP MANAGEMENT =================")
            print(f"1) Create system backup")
            print(f"2) Restore system backup")
            print(f"3) Generate one-use restore code")
            print(f"4) Revoke one-use restore code")
            print(f"Q) Back")
            choice = input("> ").strip().lower()
            print("")

            if choice == "q":
                break
            elif choice == "1":
                if user.create_system_backup(self._db, self._logger):
                    print("System backup created successfully!")
                else:
                    print("Feature not yet implemented")
                input("Press Enter to continue...")
            elif choice == "2":
                if user.restore_system_backup(self._db, self._logger):
                    print("System backup restored successfully!")
                else:
                    print("Feature not yet implemented")
                input("Press Enter to continue...")
            elif choice == "3":
                if user.generate_one_use_restore_code(self._db, self._logger):
                    print("One-use restore code generated successfully!")
                else:
                    print("Feature not yet implemented")
                input("Press Enter to continue...")
            elif choice == "4":
                if user.revoke_one_use_restore_code(self._db, self._logger):
                    print("One-use restore code revoked successfully!")
                else:
                    print("Feature not yet implemented")
                input("Press Enter to continue...")
            else:
                print("Invalid option. Please try again.")
                input("Press Enter to continue...")   

    def data_management_super_admin(self, user):
      while True:
            print("================= DATA MANAGEMENT =================")
            print(f"1) Add new scooter")
            print(f"2) Modify or update scooter")
            print(f"3) Delete scooter")
            print(f"4) Search scooter")
            print(f"5) Add new traveller")
            print(f"6) Modify or update traveller")
            print(f"7) Delete traveller")
            print(f"8) Search traveller")
            print(f"9) View logs")
            print(f"Q) Back")
            choice = input("> ").strip().lower()
            print("")

            if choice == "q":
                break
            elif choice == "1":
                if user.add_scooter(self._db, self._logger):
                    print("Scooter added successfully!")
                else:
                    print("Feature not yet implemented")
                input("Press Enter to continue...")
            elif choice == "2":
                if user.update_scooter(self._db, self._logger):
                    print("Scooter updated successfully!")
                else:
                    print("Feature not yet implemented")
                input("Press Enter to continue...")
            elif choice == "3":
                if user.delete_scooter(self._db, self._logger):
                    print("Scooter deleted successfully!")
                else:
                    print("Feature not yet implemented")
                input("Press Enter to continue...")
            elif choice == "4":
                if user.search_scooter(self._db, self._logger):
                    print("Scooter found!")
                else:
                    print("Feature not yet implemented")
                input("Press Enter to continue...")
            elif choice == "5":
                if user.add_traveller(self._db, self._logger):
                    print("Traveller added successfully!")
                else:
                    print("Feature not yet implemented")
                input("Press Enter to continue...")
            elif choice == "6":
                if user.update_traveller(self._db, self._logger):
                    print("Traveller updated successfully!")
                else:
                    print("Feature not yet implemented")
                input("Press Enter to continue...")
            elif choice == "7":
                if user.delete_traveller(self._db, self._logger):
                    print("Traveller deleted successfully!")
                else:
                    print("Feature not yet implemented")
                input("Press Enter to continue...")
            elif choice == "8":
                if user.search_traveller(self._db, self._logger):
                    print("Traveller found!")
                else:
                    print("Feature not yet implemented")
                input("Press Enter to continue...")
            elif choice == "9":
                if user.view_logs(self._db, self._logger):
                    print("Logs viewed successfully!")
                else:
                    print("Feature not yet implemented")
                input("Press Enter to continue...")
            else:
                print("Invalid option. Please try again.")
                input("Press Enter to continue...")
    
