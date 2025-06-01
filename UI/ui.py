import Classes.validate as validate

class ui:
    def __init__(self, status):
        self.status = False
    
    def landing(self, status):
        while status is True:
            print(f"Welcome to Urban Mobility!")
            print(f"Log in as: ")
            print(f"1) Super Administrator")
            print(f"2) System Administrator")
            print(f"3) Service Engineer")
            print(f"4) Exit")
            choice = input()
            if choice == "4":
                status = False

            if choice == "1":
                self.user_landing(True)
            if choice == "2":
                code = input(f"Enter code: ")
                if not validate.validate_login(code):
                    print(f"Wrong code")
                    self.landing(True)

    def user_landing(self, status):
        if status is True:
            print(f"Nothing to see here :D")
            return
