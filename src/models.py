class SuperAdministrator:
    username = "super_admin"
    password = "Admin_123?"
    role = "Super Administrator"
    firstname = "Super"
    lastname = "Administrator"

    def update_password(self):
        new_password = input(f"New password: ")
        second_try = input(f"Confirm new password: ")
        if new_password == second_try:
            self.password = second_try
        else:
            print(f"Passwords do not match. Try again.")