from helper import Helper
from datetime import datetime
import zipfile
import os
from pathlib import Path

class User:
    def __init__(self, first_name, last_name, username, password, role):
            self.first_name = first_name
            self.last_name = last_name
            self.username = username
            self.password = password
            self.role = role

    "From here on, these methods are specific for user management, like adding, updating and deleting users."

    def view_users(self, database, logger):
        # ToDo
        try:
            if self.role != "Service Engineer":
                users = database.get_users()
                print("USER LIST")
                print("Username - Role")
                for user in users:
                    print(f"{Helper.symmetric_decrypt(user[3])} - {user[5]}")
                print("")
                logger.log_info(self, "Viewed users", "")
                return True
            else:
                return False
        except Exception as e:
            logger.log_error(self, "Viewing users", e)
            return False

    def add_new_system_admin(self, database, logger):
        # ToDo
        try:
            while True:
                user_role = "System Administrator"
                print("New System Administrator Details")
                first_name = input("First Name: ")
                last_name = input("Last Name: ")
                username = Helper.validate_username(input("Username: "))
                password = Helper.validate_password(input("Password: "))

                print(f"New System Administrator: {first_name} {last_name}, Username: {username}, Role: {user_role}")
                confirm = input("Confirm (Y/N): ").strip().upper()
                if confirm == "Y":
                    encrypted_username = Helper.symmetric_encrypt(username)
                    hashed_password = Helper.utils_hash(password)
                    result = database.add_user(first_name, last_name, encrypted_username, hashed_password, user_role)
                    if result:
                        logger.log_info(self, f"Added {encrypted_username}", "System Administrator")
                        return True
                    return False
                elif confirm == "N":
                    print("User creation cancelled.")
                    return False
                else:
                    print("Invalid input. Please enter Y or N.")
        except Exception as e:
            logger.log_error(self, "Adding a new System Administrator", e)
            return False

    def update_system_admin(self, database, logger):
        # ToDo
        try:
            print("Please enter the username of the System Administrator you want to update.")
            current_username = input("Username: ").lower().strip()
            while True:
                role = "System Administrator"
                print("All information will be replaced.\nIf you wish to keep old information, please write it again.")
                first_name = input("First Name: ")
                last_name = input("Last Name: ")

                username = Helper.validate_username(input("Username: "))
                password = Helper.validate_password(input("Password: "))

                print(f"Updated Information: {first_name} {last_name}, Username: {username}, Role: {role}")

                confirm = input("Confirm (Y/N): ").strip().upper()
                if confirm == "Y":
                    encrypted_username = Helper.symmetric_encrypt(username)
                    hashed_password = Helper.utils_hash(password)
                    result = database.update_user(current_username, first_name, last_name, encrypted_username, hashed_password)
                    if result:
                        logger.log_info(self, "Updated a system admin", f"User: {username}")
                        return True
                    return False
                elif confirm == "N":
                    print("User creation cancelled.")
                    return False
                else:
                    print("Invalid input. Please enter Y or N.")
        except Exception as e:
            logger.log_error(self, "Updating a System Admin", e)
    
    def delete_system_admin(self, database, logger):
        # ToDo
        try:
            while True:
                print("Please insert the username of the user you wish to delete")
                username = input("Username: ").lower().strip()
                print(f"Are you sure you want to delete the following user:")
                print(f"Username: {username}")
                confirm = input("Confirm (Y/N): ").strip().upper()
                if confirm == "Y":
                    result = database.delete_user(username)
                    if result:
                        logger.log_info(self, f"Deleted {username}", "System Administrator")
                        return True
                    return False
                elif confirm == "N":
                    print("User creation cancelled.")
                    return False
                else:
                    print("Invalid input. Please enter Y or N.")
        except Exception as e:
            logger.log_error(self, "Deleting a System Administrator", e)
            return False
    
    def reset_system_admin_password(self, database, logger):
        # ToDo
        while True:
            logger.log_info(self, "Resetting User Password")
            try:
                print("=== Resetting User Password ===")
                print("Please insert the System Administrator username you wish to update")
                username = input("> ")
                user = database.return_user(Helper.symmetric_encrypt(username))
                if user is None or user is False:
                    print("User not found")
                    input("Press Enter to continue...")
                    return False
                while True:
                    print(f"This username belongs to: {user.first_name} {user.last_name}")
                    print(f"Do you wish to proceed [Y/N]")
                    choice = input("> ").upper().strip()
                    if choice == "N":
                        return False
                    new_password = Helper.random_password_generator()
                    print(f"\nThis message will only be shown once, this is the new password: {new_password}")
                    return database.update_user(user.username, user.first_name, user.last_name, user.username, Helper.utils_hash(new_password))
            except Exception as e:
                logger.log_error(self, f"Resetting a System Admin password", e)
                return False
    
    def add_new_service_engineer(self, database, logger):
        # ToDo
        try:
            while True:
                user_role = "Service Engineer"
                print("New Service Engineer Details")
                first_name = input("First Name: ")
                last_name = input("Last Name: ")
                username = Helper.validate_username(input("Username: "))
                password = Helper.validate_password(input("Password: "))

                print(f"New Service Engineer: {first_name} {last_name}, Username: {username}, Role: {user_role}")
                confirm = input("Confirm (Y/N): ").strip().upper()
                if confirm == "Y":
                    encrypted_username = Helper.symmetric_encrypt(username)
                    hashed_password = Helper.utils_hash(password)
                    result = database.add_user(first_name, last_name, encrypted_username, hashed_password, user_role)
                    if result:
                        logger.log_info(self, f"Added {encrypted_username}", "Service Engineer")
                        return True
                    return False
                elif confirm == "N":
                    print("User creation cancelled.")
                    return False
                else:
                    print("Invalid input. Please enter Y or N.")
        except Exception as e:
            logger.log_error(self, "Adding a new Service Engineer", e)
            return False
    
    def update_service_engineer(self, database, logger):
        # ToDo
        try:
            print("Please enter the username of the Service Engineer you want to update.")
            current_username = input("Username: ").lower().strip()
            while True:
                role = "Service Engineer"
                print("All information will be replaced.\nIf you wish to keep old information, please write it again.")
                first_name = input("First Name: ")
                last_name = input("Last Name: ")

                username = Helper.validate_username(input("Username: "))
                password = Helper.validate_password(input("Password: "))

                print(f"Updated Information: {first_name} {last_name}, Username: {username}, Role: {role}")

                confirm = input("Confirm (Y/N): ").strip().upper()
                if confirm == "Y":
                    encrypted_username = Helper.symmetric_encrypt(username)
                    hashed_password = Helper.utils_hash(password)
                    result = database.update_user(current_username, first_name, last_name, encrypted_username, hashed_password)
                    if result:
                        logger.log_info(self, "Updated a Service Engineer", f"User: {username}")
                        return True
                    return False
                elif confirm == "N":
                    print("User creation cancelled.")
                    return False
                else:
                    print("Invalid input. Please enter Y or N.")
        except Exception as e:
            logger.log_error(self, "Updating a Service Engineer", e)
    
    def delete_service_engineer(self, database, logger):
        # ToDo
        try:
            while True:
                print("Please insert the username of the user you wish to delete")
                username = input("Username: ").lower().strip()
                print(f"Are you sure you want to delete the following user:")
                print(f"Username: {username}")
                confirm = input("Confirm (Y/N): ").strip().upper()
                if confirm == "Y":
                    result = database.delete_user(username)
                    if result:
                        logger.log_info(self, f"Deleted {username}", "Service Engineer")
                        return True
                    return False
                elif confirm == "N":
                    print("User creation cancelled.")
                    return False
                else:
                    print("Invalid input. Please enter Y or N.")
        except Exception as e:
            logger.log_error(self, "Deleting a Service Engineer", e)
            return False
    
    def reset_service_engineer_password(self, database, logger):
        # ToDo
        while True:
            logger.log_info(self, "Resetting User Password")
            try:
                print("=== Resetting User Password ===")
                print("Please insert the Service Engineer username you wish to update")
                username = input("> ")
                user = database.return_user(Helper.symmetric_encrypt(username))
                if user is None or user is False:
                    print("User not found")
                    input("Press Enter to continue...")
                    return False
                while True:
                    print(f"This username belongs to: {user.first_name} {user.last_name}")
                    print(f"Do you wish to proceed [Y/N]")
                    choice = input("> ").upper().strip()
                    if choice == "N":
                        return False
                    new_password = Helper.random_password_generator()
                    print(f"\nThis message will only be shown once, this is the new password: {new_password}")
                    return database.update_user(user.username, user.first_name, user.last_name, user.username, Helper.utils_hash(new_password))
            except Exception as e:
                logger.log_error(self, f"Resetting a Service Engineer password", e)
                return False
    
    def delete_own_account(self, database, logger):
        # ToDo
        # System Admin can do it
        return

    "From here on, these methods are used for backup management."

    def create_system_backup(self, database, logger):
        try:
            os.makedirs("Backups", exist_ok=True)

            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
            zip_filename = f"backup_{timestamp}.zip"

            zip_path = os.path.join("Backups", zip_filename)

            with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
                zipf.write(database.path, os.path.basename(database.path))

            logger.log_info(self, "Made a backup", f"{zip_filename}")
            return True
        except Exception as e:
            logger.log_error(self, "Making a backup", e)
            return False

    def restore_system_backup(self, database, logger):
        try:
            backup_folder = "Backups"

            if not os.path.exists(backup_folder):
                print("No backups found! Folder is empty or missing.")
                return False

            backups = [f for f in os.listdir(backup_folder) if f.endswith('.zip')]
            if not backups:
                print("No ZIP backups found in the folder.")
                return False

            print("\nAvailable Backups:")
            for i, backup in enumerate(backups, 1):
                print(f"{i}. {backup}")

            try:
                choice = int(input("\nEnter the number of the backup to restore: ")) - 1
                selected_backup = backups[choice]
            except Exception as e:
                print("Invalid choice!")
                return False
            
            zip_path = os.path.join(backup_folder, selected_backup)
            with zipfile.ZipFile(zip_path, "r") as zipf:
                zipf.extractall(f"./src")
                logger.log_info(self, "Restored a backup", f"{selected_backup}")
                return True
            
            return False
        except Exception as e:
            logger.log_error(self, "Restoring a backup", e)
            return False

    def generate_one_use_restore_code(self, database, logger, filename="one_time_code.txt"):
        # ToDo
        # Super Admin can do it. (only)
        try:
            code = Helper.random_password_generator()
            code = Helper.utils_hash(code)
            result = database.add_one_time_use_code(code)
            if result:
                return True
            return False
        except Exception as e:
            logger.log_error(self, "Making a one use restore code", e)
            return False
        return False
    
    def revoke_one_use_restore_code(self, database, logger, filename="one_time_code.txt"):
        # ToDo
        # Super Admin can do it. (only)
        try:
            code = database.return_one_time_use_code()
            if code is None or code is False:
                return False
            return code
        except Exception as e:
            logger.log_error(self, "Revoking a one use restore code", e)
            return False
        return False

    "From here on, these methods are used for data management."

    def add_scooter(self, database, logger):
        # ToDo
        return

    def update_scooter(self, database, logger):
        # ToDo
        return

    def delete_scooter(self, database, logger):
        # ToDo
        return

    def search_scooter(self, database, logger):
        # ToDo
        return

    def add_traveller(self, database, logger):
        # ToDo
        return

    def update_traveller(self, database, logger):
        # ToDo
        return

    def delete_traveller(self, database, logger):
        # ToDo
        return

    def search_traveller(self, database, logger):
        # ToDo
        return

    def view_logs(self, database, logger):
        # ToDo
        return
