def landing_super_admin(user):
    while True:
        print(f"Welcome {user.firstname} {user.lastname}!")
        print(f"1) Users")
        print(f"2) Exit")
        choice = input("> ")
        if choice == "2":
            return
        elif choice == "1":
            print(f"2) Add User")
            print(f"1) View Users")
            print(f"3) Delete User")
            print(f"4) Update User")
            print(f"5) Back")
            choice = input("> ")
        else:
            print(f"Wrong input! Try again!")