from helper import Helper
from datetime import datetime

class User:
    def __init__(self, first_name, last_name, username, password, role):
        if role == "Super Administrator":
            self.username = "super_admin"
            self.password = "Admin_123?"
            self.role = "Super Administrator"
            self.firstname = "Super"
            self.lastname = "Administrator"
        else:
            if Helper.validate_username(username):
                self.username = username
            else:
                raise ValueError(f"Invalid username: {username}. Must be 8-10 characters long, start with a letter or underscore, and contain only letters, numbers, underscores, apostrophes, and periods.")
            self.username = Helper.symmetric_encrypt(username)
            if Helper.validate_password(password):
                hashed_password = Helper.utils_hash(password)
                self.password = hashed_password
            else:
                raise ValueError(f"Invalid password: {password}. Must be 12-30 characters long, contain at least one uppercase letter, one lowercase letter, one digit, and one special character.")
            self.role = role
            self.firstname = first_name
            self.lastname = last_name

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
                    # Add the new user to the database
                    encrypted_username = Helper.symmetric_encrypt(username)
                    hashed_password = Helper.utils_hash(password)
                    database.add_user(first_name, last_name,
                     encrypted_username, hashed_password, user_role)
                    logger.log_info(
                        user=self,
                        activity_description="New System Administrator added",
                        additional_info=f"Username: {encrypted_username}, Role: {user_role}"
                    )
                    logger.log_info(self, f"Added {encrypted_username}", "System Administrator")
                    return True
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
            current_username = input("Username: ")
            while True:
                role = "System Administrator"
                print("Update System Administrator Details")
                first_name = input("First Name: ")
                last_name = input("Last Name: ")
                username = Helper.validate_username(input("Username: "))
                password = Helper.validate_password(input("Password: "))
                print(f"Updated System Administrator: {first_name} {last_name}, Username: {username}, Role: {role}")
                confirm = input("Confirm (Y/N): ").strip().upper()
                if confirm == "Y":
                    # Update the user in the database
                    encrypted_username = Helper.symmetric_encrypt(username)
                    hashed_password = Helper.utils_hash(password)
                    database.update_user(current_username, first_name, last_name, encrypted_username, hashed_password)
                    logger.log_info(self, "Updated a system admin", f"User: {username}")
                    return True
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
                username = input("Username: ")
                print(f"Are you sure you want to delete the following user:")
                print(f"Username: {username}")
                confirm = input("Confirm (Y/N): ").strip().upper()
                if confirm == "Y":
                    # Add the new user to the database
                    encrypted_username = Helper.symmetric_encrypt(username)
                    database.delete_user(encrypted_username)
                    logger.log_info(
                        user=self,
                        activity_description="System Administrator deleted",
                        additional_info=f"Username: {username}"
                    )
                    logger.log_info(self, f"Deleted {username}", "System Administrator")
                    return True
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
        # Super Admin can reset System Admin password.
        # System Admin can't reset System Admin password.
        # Service Engineer can't reset System Admin password.
        choice = ""
        while choice not in ["back"]:
            print("Please enter the username of the System Adminsitrator you wish to change it's password:")
            print("Otherwhise, enter 'back' to go back")
            choice = input("> ").lower().strip()

        return
    
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
                print(f"New Service Engineer: {first_name} {last_name}, \nUsername: {username}, Role: {user_role}")
                confirm = input("Confirm (Y/N): ").strip().upper()
                if confirm == "Y":
                    # Add the new user to the database
                    encrypted_username = Helper.symmetric_encrypt(username)
                    hashed_password = Helper.utils_hash(password)
                    database.add_user(first_name, last_name,
                     encrypted_username, password, user_role)
                    logger.log_info(
                        user=self,
                        activity_description="New Service Engineer added",
                        additional_info=f"Username: {username}, Role: {user_role}"
                    )
                    logger.log_info(self, f"Added {username}", "Service Engineer")
                    return True
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
        # Super Admin can update Service Engineer.
        # System Admin can update Service Engineer.
        # Service Engineer can't update Service Engineer.
        return
    
    def delete_service_engineer(self, database, logger):
        # ToDo
        # Super Admin can delete Service Engineer.
        # System Admin can delete Service Engineer.
        # Service Engineer can't delete Service Engineer.
        return
    
    def reset_service_engineer_password(self, database, logger):
        # ToDo
        # Super Admin can reset Service Engineer password.
        # System Admin can reset Service Engineer password.
        # Service Engineer can't reset Service Engineer password.
        return
    
    def delete_own_account(self, database, logger):
        # ToDo
        # System Admin can do it
        return


    "From here on, these methods are used for backup management."

    def create_system_backup(self, database, logger):
        # ToDo
        # Super Admin can do it.
        # System Admin can do it.
        # Service Engineer can't do it.
        return

    def restore_system_backup(self, database, logger):
        # ToDo
        # Super Admin can do it. (any)
        # System Admin can do it (only with code).
        # Service Engineer can't do it.
        return

    def generate_one_use_restore_code(self, database, logger):
        # ToDo
        # Super Admin can do it. (only)
        return
    
    def revoke_one_use_restore_code(self, database, logger):
        # ToDo
        # Super Admin can do it. (only)
        return

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



