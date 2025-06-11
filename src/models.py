from helper import Helper
from datetime import datetime

class User:
    def __init__(self, first_name, last_name, username, password, role, registration_date=datetime.now()):
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
            if Helper.validate_password(password):
                self.password = password
            else:
                raise ValueError(f"Invalid password: {password}. Must be 12-30 characters long, contain at least one uppercase letter, one lowercase letter, one digit, and one special character.")
            self.role = role
            self.firstname = first_name
            self.lastname = last_name
            self.registrationDate = registration_date


    def delete_own_account(self):
        # ToDo
        # System Admin can do it, super admin too but no use
        return

    def view_users(self, database, logger):
        # ToDo
        try:
            if self.role != "Service Engineer":
                users = database.get_users()
                print("USER LIST")
                print("Username - Role")
                for user in users:
                    print(f"{Helper.symmetric_decrypt(user[3])}: {user[5]}")
                print("")
                return True
            else:
                return False
        except Exception as e:
            return False

    def add_user(self, database, logger):
        # Super Admin can add System Admin and Service Engineer.
        # System Admin can add Service Engineer.
        # Service Engineer can't add anyone.
        try:
            print("ADD NEW USER")
            print("Please enter the following information:")

            first_name = input("First name: ")
            last_name = input("Last name: ")
            while True:
                username = input("Username: ")
                if Helper.validate_username(username):
                    break
                print(
                    "Invalid username. Must be 8-10 characters long, start with a letter or underscore, and contain only letters, numbers, and underscores.")

            while True:
                password = input("Password: ")
                if Helper.validate_password(password):
                    break
                print(
                    "Invalid password. Must be 8-10 characters long, contain at least one uppercase letter, one lowercase letter, one number, and one special character.")

            while True:
                print("Please select a role:")
                print("1) System Administrator")
                print("2) Service Engineer")
                role_choice = input("> ")

                if role_choice == "1":
                    role = "System Administrator"
                    break
                elif role_choice == "2":
                    role = "Service Engineer"
                    break
                else:
                    print("Invalid role selected.")


            super_admin_users_allowed = ["System Administrator", "Service Engineer"]
            system_admin_users_allowed = ["Service Engineer"]
            if self.role == "Super Administrator":
                if role not in super_admin_users_allowed:
                    print("You don't have permission to add this user.")
                    input("Press Enter to return to the previous menu...")
            elif self.role == "System Administrator":
                if role not in system_admin_users_allowed:
                    print("You don't have permission to add this user.")
                    input("Press Enter to return to the previous menu...")

            result = database.add_new_user(first_name, last_name, username, password, role)
            if result:
                print("User created successfully!")
                input("Press Enter to return to the previous menu...")
                return True
            else:
                print("Failed to create user. Please try again.")
                input("Press Enter to return to the previous menu...")
                return False
        except Exception as e:
            print("An error occurred while adding the user.")
            input("Press Enter to return to the previous menu...")
            return False

    def delete_user(self, database, logger):
        try:
            while True:
                username = input("Enter the username of the user you want to delete: ")
                print("Are you sure you want to delete this user? (y/n)")
                input_choice = input("> ")

                if input_choice == "y":
                    result = database.database_delete_user(username)
                    if result:
                        return True
                    else:
                        return False
                elif input_choice == "n":
                    print("Deletion cancelled.")
                    break
                else:
                    print("Invalid input. Please try again.")
                    input("Press Enter to return to the previous menu...")

        except Exception as e:
            print("An error occurred while deleting the user.")
            return False

    def update_user(self, database, logger):
        # ToDo
        # Super Admin can update any user.
        # System Admin can update service engineer.
        # Service Engineer can't update anyone.
        while True:
            "This part checks if the user has permission to update other users."
            if self.role == "Service Engineer":
                print("You don't have permission to update users.")
                input("Press Enter to return to the previous menu...")
                return False
            
            print("Do you want to update a System Administrator or a Service Engineer?")
            print("1) System Administrator")
            print("2) Service Engineer")
            choice = input("> ")
            if self.role == "System Administrator" and choice == "1":
                print("You don't have permission to update System Administrators.")
                input("Press Enter to return to the previous menu...")
                return False
            

            user_input = ""
            while user_input not in ["back"]:
                print("UPDATE USER")
                print("Please enter the username of the user you want to update:")
                print("You can type 'back' to return to the previous menu.")
                user_input = input("> ")
                user_to_update = user_input

                print("Please enter the new information:")
                print("If you wish to keep the current value, please re-type it.")
                first_name = input("New first name: ")
                last_name = input("New last name: ")
                while True:
                    username = input("New username: ")
                    result = Helper.validate_username(username)
                    if result:
                        break
                    print("Invalid username. Must be 8-10 characters long, start with a letter or underscore, and contain only letters, numbers, underscores, apostrophes, and periods.")
                while True:
                    password = input("New password: ")
                    result = Helper.validate_password(password)
                    if result:
                        break
                    print("Invalid password. Must be 12-30 characters long, contain at least one uppercase letter, one lowercase letter, one digit, and one special character.")
                
                if database.update_user(user_to_update, first_name, last_name, username, password):
                    return True
                else:
                    return False
            return False

    def remove_user(self):
        # ToDo
        # Super Admin can remove any user.
        # System Admin can remove service engineer.
        # Service Engineer can't remove anyone.
        return

    def reset_password(self):
        # ToDo
        # Super Admin can reset any user's password.
        # System Admin can reset service engineer's password.
        # Service Engineer can't reset anyone.
        return

    def create_system_backup(self):
        # ToDo
        # Super Admin can do it.
        # System Admin can do it.
        # Service Engineer can't do it.
        return

    def restore_system_backup(self):
        # ToDo
        # Super Admin can do it. (any)
        # System Admin can do it (only with code).
        # Service Engineer can't do it.
        return

    def generate_one_use_restore_code(self):
        # ToDo
        # Super Admin can do it. (only)
        return

    def view_logs(self):
        # ToDo
        # Super Admin can view logs.
        # System Admin can view logs.
        # Service Engineer can't view logs.
        return

    def add_scooter(self):
        # ToDo

        # System Admin can add scooters at will.
        return

    def update_scooter(self):
        # ToDo
        # Super Admin can do it.
        # System Admin can do it.
        # Service engineer can update state of charge, target-range SoC, location,
        # out-of-service status, mileage, last maintenance date
        return

    def delete_scooter(self):
        # ToDo
        # Super Admin can do it.
        # System Admin can do it.
        # Service engineer can't do it.
        return
    def search_scooter(self):
        # ToDo
        # Service Engineer can do it.
        # System Admin can do it.
        return

    def add_traveller(self):
        # ToDo
        # System Admin can add.
        # Service Engineer can't add.
        return

    def update_traveller(self):
        # ToDo
        # System Admin can update.
        # Service Engineer can't update.
        return
    def delete_traveller(self):
        # ToDo
        # System Admin can delete.
        # Service Engineer can't delete.
        return

    def view_travellers(self):
        # ToDo
        # System Admin can view.
        # Service Engineer can't view.
        return
