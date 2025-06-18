import authenticator
from helper import Helper

print("Starting user interface...")
print("")

class Ui:
    def __init__(self, logger, database):
        self._logger = logger
        self._db = database

    def landing(self):
        while True:
            print("\n=== URBAN MOBILITY SYSTEM ===")
            print("=== Welcome to Urban Mobility! ===\n")
            print("1. Login")
            print("Q. Exit\n")
            choice = input("> ").strip().upper()
            print("")

            if choice == "Q":
                quit()
            elif choice == "1":
                self.login()
            else:
                print("Wrong input! Try again!")
                input("Press Enter to continue...")

    def login(self):
        tries = 0
        while True:
            if tries > 2:
                self._logger.log_warning("None", "Too many logins attempts")
                break
            print("LOGIN")
            print("If you wish to cancel, enter 'exit' as the username.")
            username = input("Username: ").lower().strip()
            password = input("Password: ").strip()
            encrypted_username = Helper.symmetric_encrypt(username)
            hashed_password = Helper.utils_hash(password)
            print("")

            if Helper.symmetric_decrypt(encrypted_username) == "exit":
                break
            auth = authenticator.Authenticator(self._logger, self._db)
            user = auth.auth_user(encrypted_username, hashed_password)
            
            if user is False or user is None:
                print("Wrong username or password. Try again!")
                input("Press Enter to continue...")
                self.landing()
            elif user.role == "Super Administrator":
                self.landing_super_admin(user)
            elif user.role == "System Administrator":
                self.landing_system_admin(user)
                break
            elif user.role == "Service Engineer":
                self.landing_service_engineer(user)
                input("Press Enter to continue...")
                break
            else:
                tries = tries + 1
                print("Wrong username or password. Try again!")
                input("Press Enter to continue...")

    def landing_super_admin(self, user):
        self._logger.log_info(user=user,
                              activity_description="Accessed Super Administrator Dashboard",
                              additional_info="")
        try:
            while True:
                print(f"SUPER ADMINISTRATOR DASHBOARD")
                print(f"Welcome, {user.first_name} {user.last_name}!")
                print("1. User Management")
                print("2. Backup Management")
                print("3. Data Management")
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
                print("\n=== USER MANAGEMENT ===")
                
                print("\n=== System Administrator ===")
                print("1. Add new System Administrator")
                print("2. Modify or update System Administrator")
                print("3. Delete System Administrator")
                print("4. Reset System Administrator password (temporary)")
                
                print("\n=== Service Engineer ===")
                print("5. Add new Service Engineer")
                print("6. Modify or update Service Engineer")
                print("7. Delete Service Engineer")
                print("8. Reset Service Engineer password (temporary)")
                
                print("\n=== Other ===")
                print("9. View Users")
                print("\nQ. Back\n")
                choice = input("> ").strip().lower()
                print("")

                if choice == "q":
                    self.landing_super_admin(user)
                elif choice == "1":
                    if user.add_new_system_admin(self._db, self._logger):
                        print("System Administrator added successfully!")
                        input("Press any key to continue...")
                        print("")
                    else:
                        print("Failed to add System Administrator. Please try again.")
                        input("Press any key to continue...")
                        print("")
                elif choice == "2":
                    if user.update_system_admin(self._db, self._logger):
                        print("User updated successfully!")
                        input("Press any key to continue...")
                        print("")
                    else:
                        print("Failed to update user. Please try again.")
                        input("Press any key to continue...")
                        print("")
                elif choice == "3":
                    if user.delete_system_admin(self._db, self._logger):
                        print("User deleted successfully!")
                        input("Press any key to continue...")
                        print("")
                    else:
                        print("Failed to delete user. Please try again.")
                        print("")
                elif choice == "4":
                    if user.reset_system_admin_password(self._db, self._logger):
                        print("User updated successfully!")
                        input("Press any key to continue...")
                        print("")
                    else:
                        print("Failed to update user. Please try again.")
                        input("")
                elif choice == "5":
                    if user.add_new_service_engineer(self._db, self._logger):
                        print("Service Engineer added successfully!")
                        input("Press any key to continue...")
                        print("")
                    else:
                        print("Failed to add Service Engineer. Please try again.")
                        input("Press any key to continue...")
                        print("")
                elif choice == "6":
                    if user.update_service_engineer(self._db, self._logger):
                        print("Service Engineer updated successfully!")
                        input("Press any key to continue...")
                        print("")
                    else:
                        print("Failed to update Service Engineer. Please try again.")
                        input("Press any key to continue...")
                        print("")
                elif choice == "7":
                    if user.delete_service_engineer(self._db, self._logger):
                        print("Service Engineer deleted successfully!")
                        input("Press any key to continue...")
                        print("")
                    else:
                        print("Failed to delete Service Engineer. Please try again.")
                        input("Press any key to continue...")
                        print("")
                elif choice == "8":
                    if user.reset_service_engineer_password(self._db, self._logger):
                        print("Service Engineer password reset successfully!")
                        input("Press any key to continue...")
                        print("")
                    else:
                        print("Failed to reset Service Engineer password. Please try again.")
                        input("Press any key to continue...")
                        print("")
                elif choice == "9":
                    if user.view_users(self._db, self._logger):
                        input("Press Enter to continue...")
                    else:
                        print("Failed to view users. Please try again.")
                        input("Press any key to continue...")
                        print("")
                else:
                    print("Invalid option. Please try again.")
                    input("Press any key to continue...")
                    print("")
        except Exception as e:
            self._logger.log_error(user=user,
                                  activity_description="An unexpected error occurred in User Management",
                                  additional_info=e)
            print("An unexpected error occurred. Please try again later.")
            input("Press Enter to continue...")
            self.landing_super_admin(user)

    def backup_management_super_admin(self, user):
        while True:
            print("\n=== BACKUP MANAGEMENT ===")
            print("1. Create system backup")
            print("2. Restore system backup")
            print("3. Generate one-use restore code")
            print("4. Revoke one-use restore code")
            print("\nQ. Back\n")
            choice = input("> ").strip().lower()
            print("")

            if choice == "q":
                 self.landing_super_admin(user)
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
                    print("An error occurred. Please try again.")
                input("Press Enter to continue...")
            elif choice == "3":
                if user.generate_one_use_restore_code(self._db, self._logger):
                    print("One-use restore code generated successfully!")
                else:
                    print("An error occurred. Please try again.")
                input("Press Enter to continue...")
            elif choice == "4":
                if user.revoke_one_use_restore_code(self._db, self._logger):
                    print("One-use restore code revoked successfully!")
                else:
                    print("An error occurred. Please try again.")
                input("Press Enter to continue...")
            else:
                print("An error occurred. Please try again.")
                input("Press Enter to continue...")   

    def data_management_super_admin(self, user):
        while True:
            print("\n=== DATA MANAGEMENT ===")
            print("\n=== Scooters ===")
            print("1. Add new scooter")
            print("2. Modify or update scooter")
            print("3. Delete scooter")
            print("4. Search scooter")
            
            print("\n=== Travellers ===")
            print("5. Add new traveller")
            print("6. Modify or update traveller")
            print("7. Delete traveller")
            print("8. Search traveller")
            
            print("\n=== Other ===")
            print("9. View logs")
            print("\nQ. Back\n")
            choice = input("> ").strip().lower()
            print("")

            if choice == "q":
                self.landing_super_admin(user)
            elif choice == "1":
                if user.add_scooter(self._db, self._logger):
                    print("Scooter added successfully!")
                    input("Press enter to continue...")
                else:
                    print("Feature not yet implemented")
                input("Press Enter to continue...")
            elif choice == "2":
                if user.admin_update_scooter(self._db, self._logger):
                    print("Scooter updated successfully!")
                else:
                    print("Feature not yet implemented")
                input("Press Enter to continue...")
            elif choice == "3":
                if user.admin_delete_scooter(self._db, self._logger):
                    print("Scooter deleted successfully!")
                else:
                    print("Feature not yet implemented")
                input("Press Enter to continue...")
            elif choice == "4":
                if user.search_scooter(self._db, self._logger):
                    print("")
                else:
                    print("Feature not yet implemented")
                input("Press Enter to continue...")
            elif choice == "5":
                if user.add_traveler(self._db, self._logger):
                    print("Traveller added successfully!")
                else:
                    print("Feature not yet implemented")
                input("Press Enter to continue...")
            elif choice == "6":
                if user.update_traveler(self._db, self._logger):
                    print("Traveller updated successfully!")
                else:
                    print("Feature not yet implemented")
                input("Press Enter to continue...")
            elif choice == "7":
                if user.delete_traveler(self._db, self._logger):
                    print("Traveller deleted successfully!")
                else:
                    print("Feature not yet implemented")
                input("Press Enter to continue...")
            elif choice == "8":
                if user.search_traveller(self._db, self._logger):
                    print("")
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

    def landing_system_admin(self, user):
        self._logger.log_info(user=user,
                              activity_description="Accessed System Administrator Dashboard")
        try:
            while True:
                print(f"=== SYSTEM ADMINISTRATOR DASHBOARD ===")
                print(f"Welcome, {user.first_name} {user.last_name}!")
                print("1. Account Features")
                print("2. User Management")
                print("3. Backup Management")
                print("4. Data Management")
                print("Q) Logout")
                choice = input("> ").strip().lower()
                print("")

                if choice == "q":
                    self.landing()
                elif choice == "1":
                    self.account_features_system_admin(user)
                elif choice == "2":
                    self.user_management_system_admin(user)
                    return
                elif choice == "3":
                    self.backup_management_system_admin(user)
                    return
                elif choice == "4":
                    self.data_management_system_admin(user)
                    return
                else:
                    print("Invalid option. Please try again.")

        except Exception as e:
            self._logger.log_error(user=user,
                                  activity_description="An unexpected error occurred in the System Administrator Dashboard",
                                  additional_info=e)
            print("An unexpected error occurred. Please try again later.")
            input("Press Enter to continue...")
            self.landing()

    def account_features_system_admin(self, user):
        self._logger.log_info(user=user,
                              activity_description="Accessed Account Features",
                              additional_info="")
        try:
            while True:
                print("\n=== ACCOUNT FEATURES ===")
                print("1. Change password")
                print("2. Update own profile")
                print("3. Delete own account")
                print("\nQ. Back\n")
                choice = input("> ").strip().lower()
                print("")
                if choice == "q":
                    self.landing_system_admin(user)
                elif choice == "1":
                    if user.change_own_password(self._db, self._logger):
                        print("Password changed successfully!")
                        input("Press Enter to continue...")
                    else:
                        print("Failed to change password. Please try again.")
                        input("Press Enter to continue...")
                elif choice == "2":
                    if user.update_own_profile(self._db, self._logger):
                        print("Profile updated successfully!")
                        input("Press Enter to continue...")
                    else:
                        print("Failed to update profile. Please try again.")
                        input("Press Enter to continue...")
                elif choice == "3":
                    if user.delete_own_account(self._db, self._logger):
                        print("Account deleted successfully!")
                        input("Press Enter to continue...")
                        self.landing()
                    else:
                        print("Failed to delete account. Please try again.")
                        input("Press Enter to continue...")
                else:
                    print("Invalid option. Please try again.")
                    input("Press Enter to continue...")
        except Exception as e:
            self._logger.log_error(user=user,
                                  activity_description="An unexpected error occurred in Account Features",
                                  additional_info=e)
            print("An unexpected error occurred. Please try again later.")
    
    def user_management_system_admin(self, user):
        try:
            self._logger.log_info(user=user,
                                 activity_description="Accessed User Management",
                                 additional_info="")
            while True:
                print("=== USER MANAGEMENT ===")
                print("1. Add new Service Engineer")
                print("2. Modify or update Service Engineer")
                print("3. Delete Service Engineer")
                print("4. Reset Service Engineer password (temporary)")
                print("5. View Users")
                print("\nQ. Back\n")
                choice = input("> ").strip().lower()

                if choice == "q":
                    self.landing_system_admin(user)
                elif choice == "1":
                    if user.add_new_service_engineer(self._db, self._logger):
                        print("Service Engineer added successfully!")
                        input("Press Enter to continue...")
                    else:
                        print("Failed to add Service Engineer. Please try again.")
                        input("Press Enter to continue...")
                elif choice == "2":
                    if user.update_service_engineer(self._db, self._logger):
                        print("Service Engineer updated successfully!")
                        input("Press Enter to continue...")
                    else:
                        print("Failed to update Service Engineer. Please try again.")
                        input("Press Enter to continue...")
                elif choice == "3":
                    if user.delete_service_engineer(self._db, self._logger):
                        print("Service Engineer deleted successfully!")
                        input("Press Enter to continue...")
                    else:
                        print("Failed to delete Service Engineer. Please try again.")
                        input("Press Enter to continue...")
                elif choice == "4":
                    if user.reset_service_engineer_password(self._db, self._logger):
                        print("Service Engineer password reset successfully!")
                        input("Press Enter to continue...")
                    else:
                        print("Failed to reset Service Engineer password. Please try again.")
                        input("Press Enter to continue...")
                elif choice == "5":
                    if user.view_users(self._db, self._logger):
                        input("Press Enter to continue...")
                    else:
                        print("Failed to view users. Please try again.")
                        input("Press Enter to continue...")
        except Exception as e:
            self._logger.log_error(user=user,
                                  activity_description="An unexpected error occurred in User Management",
                                  additional_info=e)
            
            print("An unexpected error occurred. Please try again later.")
            input("Press Enter to continue...")
            self.landing_system_admin(user)
            
    def backup_management_system_admin(self, user):
        try:
            self._logger.log_info(user=user,
                                  activity_description="Accessed Backup Management",
                                  additional_info="")
            while True:
                print("\n=== BACKUP MANAGEMENT ===")
                print("1. Create system backup")
                print("2. Restore system backup (with one-use restore code)")
                print("\nQ. Back\n")
                choice = input("> ").strip().lower()
                print("")

                if choice == "q":
                    self.landing_system_admin(user)
                elif choice == "1":
                    if user.create_system_backup(self._db, self._logger):
                        print("System backup created successfully!")
                    else:
                        print("Feature not yet implemented")
                    input("Press Enter to continue...")
                elif choice == "2":
                    if user.restore_one_system_backup(self._db, self._logger):
                        print("System backup restored successfully!")
                    else:
                        print("An error occurred. Please try again.")
                    input("Press Enter to continue...")
                else:
                    print("An error occurred. Please try again.")
                    input("Press Enter to continue...")
                    
        except Exception as e:
            self._logger.log_error(user=user,
                                  activity_description="An unexpected error occurred in Backup Management",
                                  additional_info=e)
            print("An unexpected error occurred. Please try again later.")
            input("Press Enter to continue...")
            self.landing_system_admin(user)
    
    def data_management_system_admin(self, user):
        while True:
            print("\n=== DATA MANAGEMENT ===")
            print("\n=== Scooters ===")
            print("1. Add new scooter")
            print("2. Modify or update scooter")
            print("3. Delete scooter")
            print("4. Search scooter")
            
            print("\n=== Travellers ===")
            print("5. Add new traveller")
            print("6. Modify or update traveller")
            print("7. Delete traveller")
            print("8. Search traveller")
            
            print("\n=== Other ===")
            print("9. View logs")
            print("\nQ. Back\n")
            choice = input("> ").strip().lower()
            print("")

            if choice == "q":
                self.landing_system_admin(user)
            elif choice == "1":
                if user.add_scooter(self._db, self._logger):
                    print("Scooter added successfully!")
                    input("Press enter to continue...")
                else:
                    print("Feature not yet implemented")
                input("Press Enter to continue...")
            elif choice == "2":
                if user.admin_update_scooter(self._db, self._logger):
                    print("Scooter updated successfully!")
                else:
                    print("Feature not yet implemented")
                input("Press Enter to continue...")
            elif choice == "3":
                if user.admin_delete_scooter(self._db, self._logger):
                    print("Scooter deleted successfully!")
                else:
                    print("Feature not yet implemented")
                input("Press Enter to continue...")
            elif choice == "4":
                if user.search_scooter(self._db, self._logger):
                    print("")
                else:
                    print("Feature not yet implemented")
                input("Press Enter to continue...")
            elif choice == "5":
                if user.add_traveler(self._db, self._logger):
                    print("Traveller added successfully!")
                else:
                    print("Feature not yet implemented")
                input("Press Enter to continue...")
            elif choice == "6":
                if user.update_traveler(self._db, self._logger):
                    print("Traveller updated successfully!")
                else:
                    print("Feature not yet implemented")
                input("Press Enter to continue...")
            elif choice == "7":
                if user.delete_traveler(self._db, self._logger):
                    print("Traveller deleted successfully!")
                else:
                    print("Feature not yet implemented")
                input("Press Enter to continue...")
            elif choice == "8":
                if user.search_traveller(self._db, self._logger):
                    print("")
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

    "SERVICE ENGINEER STUFF"

    def landing_service_engineer(self, user):
        self._logger.log_info(user=user,
                              activity_description="Accessed System Administrator Dashboard")
        try:
            while True:
                print(f"=== SYSTEM ADMINISTRATOR DASHBOARD ===")
                print(f"Welcome, {user.first_name} {user.last_name}!")
                print("1. Account Features")
                print("2. Scooter Management")
                print("Q) Logout")
                choice = input("> ").strip().lower()
                print("")

                if choice == "q":
                    self.landing()
                elif choice == "1":
                    self.account_features_service_engineer(user)
                elif choice == "2":
                    self.scooter_management_service_engineer(user)
                    return
                else:
                    print("Invalid option. Please try again.")

        except Exception as e:
            self._logger.log_error(user=user,
                                  activity_description="An unexpected error occurred in the System Administrator Dashboard",
                                  additional_info=e)
            print("An unexpected error occurred. Please try again later.")
            input("Press Enter to continue...")
            self.landing()

    def account_features_service_engineer(self, user):
        self._logger.log_info(user=user,
                              activity_description="Accessed Account Features",
                              additional_info="")
        try:
            while True:
                print("\n=== ACCOUNT FEATURES ===")
                print("1. Change password")
                print("2. Update own profile")
                print("\nQ. Back\n")
                choice = input("> ").strip().lower()
                print("")
                if choice == "q":
                    self.landing_service_engineer(user)
                elif choice == "1":
                    if user.change_own_password(self._db, self._logger):
                        print("Password changed successfully!")
                        input("Press Enter to continue...")
                    else:
                        print("Failed to change password. Please try again.")
                        input("Press Enter to continue...")
                elif choice == "2":
                    if user.update_own_profile(self._db, self._logger):
                        print("Profile updated successfully!")
                        input("Press Enter to continue...")
                    else:
                        print("Failed to update profile. Please try again.")
                        input("Press Enter to continue...")
                else:
                    print("Invalid option. Please try again.")
                    input("Press Enter to continue...")
        except Exception as e:
            self._logger.log_error(user=user,
                                  activity_description="An unexpected error occurred in Account Features",
                                  additional_info=e)
            print("An unexpected error occurred. Please try again later.")
    
    def scooter_management_service_engineer(self, user):
        self._logger.log_info(user=user,
                              activity_description="Accessed Account Features",
                              additional_info="")
        try:
            while True:
                print("\n=== SCOOTER MANAGEMENT ===")
                print("1. Update scooter attributes")
                print("2. Search scooter")
                print("\nQ. Back\n")
                choice = input("> ").strip().lower()
                print("")
                if choice == "q":
                    self.landing_service_engineer(user)
                elif choice == "1":
                    if user.engineer_partial_scooter_update(self._db, self._logger):
                        print("Success!")
                        input("Press Enter to continue...")
                    else:
                        input("Press Enter to continue...")
                elif choice == "2":
                    if user.search_scooter(self._db, self._logger):
                        print("Success!")
                        input("Press Enter to continue...")
                    else:
                        print("Failed. Please try again.")
                        input("Press Enter to continue...")
                else:
                    print("Invalid option. Please try again.")
                    input("Press Enter to continue...")
        except Exception as e:
            self._logger.log_error(user=user,
                                  activity_description="An unexpected error occurred in Account Features",
                                  additional_info=e)
            print("An unexpected error occurred. Please try again later.")