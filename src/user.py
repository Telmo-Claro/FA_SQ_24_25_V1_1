class User:
    def __init__(self, username, password, role, firstname, lastname, registrationDate):
        self.username = username
        self.password = password
        self.role = role
        self.firstname = firstname
        self.lastname = lastname
        self.registrationDate = registrationDate

    def update_password(self):
        new_password = input(f"New password: ")
        second_try = input(f"Confirm new password: ")
        if new_password == second_try:
            self.password = second_try
        else:
            print(f"Passwords do not match. Try again.")
