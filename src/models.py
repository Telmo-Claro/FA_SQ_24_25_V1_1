from csv import excel_tab

from helper import Helper
from datetime import datetime
import zipfile
import os
from fuzzywuzzy import fuzz

class User:
    def __init__(self, first_name, last_name, username, password, role, id):
            self.first_name = first_name
            self.last_name = last_name
            self.username = Helper.symmetric_decrypt(username)
            self.password = password
            self.role = role
            self.id = id

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

        except Exception as e:
            logger.log_error(self, "Restoring a backup", e)
            return False

    def generate_one_use_restore_code(self, database, logger):
        # ToDo
        # Super Admin can do it. (only)
        try:
            logger.log_info(self, "Generating one use restore code")
            code = Helper.random_password_generator()
            code = Helper.utils_hash(code)
            result = database.add_one_time_use_code(code)
            if result:
                return True
            return False
        except Exception as e:
            logger.log_error(self, "Making a one use restore code", e)
            return False

    def revoke_one_use_restore_code(self, database, logger):
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

    "SCOOTER"

    def add_scooter(self, database, logger):
        try:
            logger.log_info(self, "Adding scooter")
            print("ADDING SCOOTER (enter 'q' at any prompt to cancel)")

            # Get scooter information with validation
            brand = Helper.get_input("Brand is the manufacturer (e.g. NIU)\nEnter brand: ")
            if brand is False: return False

            model = Helper.get_input("Enter model: ")
            if model is False: return False

            while True:
                serial_number = Helper.get_input("\nUnique identifier number, 10 to 17 digits\nEnter serial number: ")
                if serial_number is False: return False
                if Helper.validate_serial_number(serial_number):
                    break
                print("Invalid serial number (10-17 alphanumeric characters)")

            while True:
                top_speed = Helper.get_input("Enter top speed (in KM): ")
                if top_speed is False: return False
                if top_speed.isdigit():
                    top_speed = int(top_speed)
                    break
                print("Top speed must be a number")

            while True:
                battery_capacity = Helper.get_input("Enter battery capacity (in Wh): ")
                if battery_capacity is False: return False
                if battery_capacity.isdigit():
                    battery_capacity = int(battery_capacity)
                    break
                print("Battery capacity must be a number")

            while True:
                state_of_charge = Helper.get_input("Enter state of charge (%): ")
                if state_of_charge is False: return False
                if state_of_charge.isdigit() and 0 <= int(state_of_charge) <= 100:
                    state_of_charge = int(state_of_charge)
                    break
                print("State of charge must be 0-100")

            while True:
                target_range = Helper.get_input("Enter target range (in KM): ")
                if target_range is False: return False
                if target_range.isdigit():
                    target_range = int(target_range)
                    break
                print("Target range must be a number")

            while True:
                location = Helper.get_input("\nFive decimal places, in Rotterdam\nEnter location: ")
                if location is False: return False
                if Helper.validate_location(location):
                    break
                print("Invalid location (format: 51.92250, 4.47917 within Rotterdam)")

            while True:
                mileage = Helper.get_input("Enter mileage (in KM): ")
                if mileage is False: return False
                if mileage.isdigit():
                    mileage = int(mileage)
                    break
                print("Mileage must be a number")

            while True:
                last_maintenance = Helper.get_input("\nEnter last maintenance date (YYYY-MM-DD): ")
                if last_maintenance is False: return False
                if Helper.validate_last_maintenance_date(last_maintenance):
                    break
                print("Invalid date format (YYYY-MM-DD)")

            # Encrypt sensitive data before storing
            encrypted_brand = Helper.symmetric_encrypt(brand)
            encrypted_model = Helper.symmetric_encrypt(model)
            encrypted_serial = Helper.symmetric_encrypt(serial_number)
            encrypted_location = Helper.symmetric_encrypt(location)
            encrypted_top_speed = Helper.symmetric_encrypt(str(top_speed))
            encrypted_state_of_charge = Helper.symmetric_encrypt(str(state_of_charge))
            encrypted_target_range = Helper.symmetric_encrypt(str(target_range))
            encrypted_mileage = Helper.symmetric_encrypt(str(mileage))
            encrypted_last_maintenance = Helper.symmetric_encrypt(last_maintenance)
            encrypted_battery_capacity = Helper.symmetric_encrypt(str(battery_capacity))

            return database.add_scooter(
                brand=encrypted_brand,
                model=encrypted_model,
                serial_number=encrypted_serial,
                top_speed=encrypted_top_speed,
                battery_capacity=encrypted_battery_capacity,
                state_of_charge=encrypted_state_of_charge,
                target_range_soc=encrypted_target_range,
                location=encrypted_location,
                mileage=encrypted_mileage,
                last_maintenance_date=encrypted_last_maintenance
            )

        except Exception as e:
            logger.log_error(self, f"Error adding scooter". e)
            return False

    def admin_update_scooter(self, database, logger):
        try:
            logger.log_info(self, "Updating scooter")
            scooters = database.return_all_scooters()

            print("\nCurrent scooters:")
            for scooter in scooters:
                print(f"ID: {scooter[0]}, "
                      f"Brand: {Helper.symmetric_decrypt(scooter[2])}, "
                      f"Model: {Helper.symmetric_decrypt(scooter[3])}, "
                      f"Serial: {Helper.symmetric_decrypt(scooter[4])}")

            number_of_scooters = len(scooters)
            while True: # Checks if ID is on the list
                print("Enter the ID of the scooter you want to update.")
                input_id = input("> ")
                try:
                    input_id = int(input_id)
                    if input_id > number_of_scooters:
                        print("Invalid ID. Please try again.")
                        continue
                    else:
                        break
                except:
                    print("Invalid ID. Please try again.")
                    continue

            scooter_to_update = database.return_scooter_by_id(input_id)
            print("\nScooter to update:")
            print(f"ID: {scooter_to_update[0]}")
            print(f"Brand: {Helper.symmetric_decrypt(scooter_to_update[2])}")
            print(f"Model: {Helper.symmetric_decrypt(scooter_to_update[3])}")
            print(f"Serial: {Helper.symmetric_decrypt(scooter_to_update[4])}")
            print(f"Top Speed: {scooter_to_update[5]}")
            print(f"Battery: {scooter_to_update[6]} Wh")
            print(f"Charge: {scooter_to_update[7]}%")
            print(f"Range: {scooter_to_update[8]} km")
            print(f"Location: {Helper.symmetric_decrypt(scooter_to_update[9])}")
            print(f"Status: {'Out of Service' if scooter_to_update[10] else 'Available'}")
            print(f"Mileage: {scooter_to_update[11]} km")
            print(f"Last Maintenance: {scooter_to_update[12]}")

            fields_map = {
                1: ("brand", "Brand"),
                2: ("model", "Model"),
                3: ("serial_number", "Serial Number"),
                4: ("top_speed", "Top Speed"),
                5: ("battery_capacity", "Battery Capacity"),
                6: ("state_of_charge", "State of Charge"),
                7: ("target_range_soc", "Target Range"),
                8: ("location", "Location"),
                9: ("mileage", "Mileage"),
                10: ("last_maintenance_date", "Last Maintenance Date")
            }

            while True:
                print("\nWhich field do you want to update?")
                for num, (_, display) in fields_map.items():
                    print(f"{num}. {display}")

                try:
                    choice = int(input("> "))
                    if choice not in fields_map:
                        print("Invalid choice. Please try again.")
                        continue

                    db_field, display_name = fields_map[choice]
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.")

            # Field-specific validation
            new_value = None
            if db_field in ["brand", "model"]:
                new_value = input(f"Enter new {display_name}: ")

            elif db_field == "serial_number":
                while True:
                    new_value = input("Enter new serial number (10-17 chars): ")
                    if Helper.validate_serial_number(new_value):
                        break
                    print("Invalid serial number (10-17 alphanumeric chars)")

            elif db_field == "location":
                while True:
                    new_value = input("Enter new location (51.xxxxx,4.xxxxx): ")
                    if Helper.validate_location(new_value):
                        break
                    print("Invalid location format or outside Rotterdam")

            elif db_field == "last_maintenance_date":
                while True:
                    new_value = input("Enter new maintenance date (YYYY-MM-DD): ")
                    if Helper.validate_last_maintenance_date(new_value):
                        break
                    print("Invalid date format")

            elif db_field in ["top_speed", "battery_capacity",
                              "state_of_charge", "target_range_soc", "mileage"]:
                while True:
                    new_value = input(f"Enter new {display_name}: ")
                    if new_value.isdigit():
                        new_value = int(new_value)
                        if db_field == "state_of_charge" and not (0 <= new_value <= 100):
                            print("Must be 0-100%")
                            continue
                        break
                    print("Must be a number")

            # Encrypt sensitive fields before updating
            if db_field in ["brand", "model", "serial_number", "location"]:
                new_value = Helper.symmetric_encrypt(new_value)

            return database.update_scooter(
                scooter_id=input_id,
                field_to_change=db_field,
                new_field=new_value
            )


        except Exception as e:
            logger.log_error(self, "Updating scooter", e)
            return False

    def admin_delete_scooter(self, database, logger):
        try:
            logger.log_info(self, "Deleting scooter")
            scooters = database.return_all_scooters()

            print("\nCurrent scooters:")
            print("\nCurrent scooters:")
            for scooter in scooters:
                print(f"ID: {scooter[0]}, "
                      f"Brand: {Helper.symmetric_decrypt(scooter[2])}, "
                      f"Model: {Helper.symmetric_decrypt(scooter[3])}, "
                      f"Serial: {Helper.symmetric_decrypt(scooter[4])}")

            number_of_scooters = len(scooters)
            while True: # Checks if ID is on the list
                print("Enter the ID of the scooter you want to delete.")
                input_id = input("> ")
                try:
                    input_id = int(input_id)
                    if input_id > number_of_scooters:
                        print("Invalid ID. Please try again.")
                        continue
                    else:
                        break
                except:
                    print("Invalid ID. Please try again.")
                    continue

            scooter_to_delete = database.return_scooter_by_id(input_id)
            print("\nScooter to delete:")
            print(f"ID: {scooter_to_delete[0]}")
            print(f"Brand: {Helper.symmetric_decrypt(scooter_to_delete[2])}")
            print(f"Model: {Helper.symmetric_decrypt(scooter_to_delete[3])}")
            print(f"Serial: {Helper.symmetric_decrypt(scooter_to_delete[4])}")
            print(f"Top Speed: {scooter_to_delete[5]} km/h")
            print(f"Battery: {scooter_to_delete[6]} Wh")
            print(f"Charge: {scooter_to_delete[7]}%")
            print(f"Range: {scooter_to_delete[8]} km")
            print(f"Location: {Helper.symmetric_decrypt(scooter_to_delete[9])}")
            print(f"Status: {'Out of Service' if scooter_to_delete[10] else 'Available'}")
            print(f"Mileage: {scooter_to_delete[11]} km")
            print(f"Last Maintenance: {scooter_to_delete[12]}")

            # Confirmation
            while True:
                print("\nAre you sure you want to delete this scooter? (Y/N)")
                choice = input("> ").upper().strip()
                if choice == 'Y':
                    return database.delete_scooter(input_id)
                elif choice == 'N':
                    print("Deletion cancelled.")
                    return False
                print("Please enter Y or N.")

        except Exception as e:
            logger.log_error(self, "Updating scooter", e)
            return False

    def search_scooter(self, database, logger):
        try:
            logger.log_info(self, "Searching scooter")
            print("=== SCOOTER SEARCH ===")
            print("Enter search terms (leave blank to ignore a field)")

            brand = input("Brand (partial match allowed): ").strip().lower()
            model = input("Model (partial match allowed): ").strip().lower()
            serial_number = input("Serial number (partial match allowed): ").strip().lower()

            scooters = database.return_all_scooters()
            results = []

            for scooter in scooters:
                scooter_brand = Helper.symmetric_decrypt(scooter[2]).strip().lower()
                scooter_model = Helper.symmetric_decrypt(scooter[3]).strip().lower()
                scooter_serial = Helper.symmetric_decrypt(scooter[4]).strip().lower()

                brand_match = not brand or fuzz.partial_ratio(brand, scooter_brand) > 70
                model_match = not model or fuzz.partial_ratio(model, scooter_model) > 70
                serial_match = not serial_number or serial_number in scooter_serial

                if brand_match and model_match and serial_match:
                    results.append(scooter)

            if not results:
                print("\nNo matching scooters found.")
            else:
                print(f"\nFound {len(results)} matching scooters:")
                for scooter in results:
                    print(f"Brand: {Helper.symmetric_decrypt(scooter[2])}, "
                          f"Model: {Helper.symmetric_decrypt(scooter[3])}, "
                          f"Serial: {Helper.symmetric_decrypt(scooter[4])}")

            return results
        except Exception as e:
            logger.log_error(self, "Searching scooter", e)
            return False

    "TRAVELLER"
    def add_traveler(self, database, logger):
        try:
            logger.log_info(self, "Adding traveler")
            while True:
                print("ADDING TRAVELER (enter 'q' at any prompt to cancel)")

                # Get traveler information
                first_name = Helper.get_input("Enter first name: ")
                if first_name is False:
                    return False

                last_name = Helper.get_input("Enter last name: ")
                if last_name is False:
                    return False

                while True:
                    birthday = Helper.get_input("Enter birthday [YYYY-MM-DD]: ")
                    if birthday is False:
                        return False
                    if Helper.validate_last_maintenance_date(birthday):
                        break
                    print("Invalid date format. Please use YYYY-MM-DD.")

                gender = Helper.get_input("Enter gender: ")
                if gender is False:
                    return False

                street_name = Helper.get_input("Enter street name: ")
                if street_name is False:
                    return False

                house_number = Helper.get_input("Enter house number: ")
                if house_number is False:
                    return False

                while True:
                    print("\nZip code has 4 digits and 2 letters.")
                    zip_code = Helper.get_input("Enter zip code (DDDDXX): ")
                    if zip_code is False:
                        return False
                    if Helper.validate_zip_code(zip_code):
                        break
                    print("Wrong format. It should look like this: 1234AB")

                cities = ["Rotterdam", "The Hague", "Delft", "Haarlem", "Leiden"]
                print("Please choose one of the following cities:")
                for i, city in enumerate(cities, 1):
                    print(f"{i}. {city}")

                while True:
                    city_choice = input("Enter city number: ")
                    try:
                        city_choice = int(city_choice)
                        if 1 <= city_choice <= len(cities):
                            city = cities[city_choice - 1]
                            break
                        print("Invalid choice. Please enter a number between 1 and", len(cities))
                    except ValueError:
                        print("Please enter a valid number.")

                email_address = input("Enter email address: ").strip()


                while True:
                    mobile_phone = input("Enter mobile phone (8 digits after '06'): ").strip()
                    if mobile_phone.isdigit() and len(mobile_phone) == 8:
                        mobile_phone = "+31-6-" + mobile_phone
                        break
                    print("Please enter exactly 6 digits.")

                while True:
                    print("A driving license number is a combination of 2 letters followed by 7 digits or 1 letter followed by 8 digits.")
                    driving_license = input("Enter driving license (XXDDDDDDD or XDDDDDDDD): ").strip().upper()
                    if Helper.validate_driving_license(driving_license):
                        break
                    print("Invalid format. Should be XX1234567 or X12345678")


                encrypted_first_name = Helper.symmetric_encrypt(first_name)
                encrypted_last_name = Helper.symmetric_encrypt(last_name)
                encrypted_birthday = Helper.symmetric_encrypt(birthday)
                encrypted_gender = Helper.symmetric_encrypt(gender)
                encrypted_street_name = Helper.symmetric_encrypt(street_name)
                encrypted_zip_code = Helper.symmetric_encrypt(zip_code)
                encrypted_email_address = Helper.symmetric_encrypt(email_address)
                encrypted_mobile_phone = Helper.symmetric_encrypt(mobile_phone)
                encrypted_driving_license = Helper.symmetric_encrypt(driving_license)
                encrypted_house_number = Helper.symmetric_encrypt(house_number)

                # Add traveler to database with unencrypted data
                result = database.add_traveler(
                    first_name=encrypted_first_name,
                    last_name=encrypted_last_name,
                    birthday=encrypted_birthday,
                    gender=encrypted_gender,
                    street_name=encrypted_street_name,
                    house_number=encrypted_house_number,
                    zip_code=encrypted_zip_code,
                    city=city,
                    email_address=encrypted_email_address,
                    mobile_phone=encrypted_mobile_phone,
                    driving_license_number=encrypted_driving_license
                )

                return result

        except Exception as e:
            logger.log_error(self, f"Error adding traveler", e)
            return False

    def update_traveler(self, database, logger):
        try:
            logger.log_info(self, "Updating traveler")
            travellers = database.return_all_travelers()
            print("\nCurrent travellers:")
            for traveller in travellers:
                print(f"ID: {traveller[0]}, "
                      f"First Name: {Helper.symmetric_decrypt(traveller[2])}, "
                      f"Last Name: {Helper.symmetric_decrypt(traveller[3])}")

            while True:  # Get the ID of the user to update
                print("Enter the ID of the traveler you want to update.")
                input_id = input("> ")
                try:
                    input_id = int(input_id)
                    if not any(traveller[0] == input_id for traveller in travellers):
                        print("Invalid ID. Please try again.")
                        continue
                    break
                except ValueError:
                    print("Invalid ID. Please try again.")

            traveller_to_update = database.return_traveler_by_id(input_id)
            print(f"\nTraveler to update:")
            print(f"ID: {traveller_to_update[0]}")
            print(f"First Name: {Helper.symmetric_decrypt(traveller_to_update[2])}")
            print(f"Last Name: {Helper.symmetric_decrypt(traveller_to_update[3])}")
            print(f"Birthday: {Helper.symmetric_decrypt(traveller_to_update[4])}")
            print(f"Gender: {Helper.symmetric_decrypt(traveller_to_update[5])}")
            print(f"Street Name: {Helper.symmetric_decrypt(traveller_to_update[6])}")
            print(f"House Number: {Helper.symmetric_decrypt(traveller_to_update[7])}")
            print(f"Zip Code: {Helper.symmetric_decrypt(traveller_to_update[8])}")
            print(f"City: {traveller_to_update[9]}")
            print(f"Email Address: {Helper.symmetric_decrypt(traveller_to_update[10])}")
            print(f"Mobile Phone: {Helper.symmetric_decrypt(traveller_to_update[11])}")
            print(f"Driving License: {Helper.symmetric_decrypt(traveller_to_update[12])}")

            fields = {
                1: ("first_name", "First Name"),
                2: ("last_name", "Last Name"),
                3: ("birthday", "Birthday"),
                4: ("gender", "Gender"),
                5: ("street_name", "Street Name"),
                6: ("house_number", "House Number"),
                7: ("zip_code", "Zip Code"),
                8: ("city", "City"),
                9: ("email_address", "Email Address"),
                10: ("mobile_phone", "Mobile Phone"),
                11: ("driving_license_number", "Driving License")
            }

            while True:
                print("\nWhich field do you want to update?")
                for num, (field, display) in fields.items():
                    print(f"{num}. {display}")

                try:
                    choice = int(input("> "))
                    if choice not in fields:
                        print("Invalid choice. Please try again.")
                        continue

                    field_to_change, display_name = fields[choice]
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.")

            new_value = None
            if field_to_change == "birthday":
                while True:
                    new_value = input("Enter birthday [YYYY-MM-DD]: ")
                    if Helper.validate_last_maintenance_date(new_value):
                        break
                    print("Invalid date format. Please use YYYY-MM-DD.")

            elif field_to_change == "zip_code":
                while True:
                    new_value = input("Enter zip code (DDDDXX): ")
                    if Helper.validate_zip_code(new_value):
                        break
                    print("Invalid format. Should be like 1234AB")

            elif field_to_change == "city":
                cities = ["Rotterdam", "The Hague", "Delft", "Haarlem", "Leiden"]
                while True:
                    print("Available cities:")
                    for i, city in enumerate(cities, 1):
                        print(f"{i}. {city}")
                    try:
                        city_choice = int(input("Enter city number: "))
                        if 1 <= city_choice <= len(cities):
                            new_value = cities[city_choice - 1]
                            break
                        print(f"Please enter number between 1-{len(cities)}")
                    except ValueError:
                        print("Please enter a valid number.")

            elif field_to_change == "mobile_phone":
                while True:
                    new_value = input("Enter mobile phone (6 digits after '06'): ").strip()
                    if new_value.isdigit() and len(new_value) == 6:
                        new_value = "+31-6-" + new_value
                        break
                    print("Please enter exactly 6 digits.")

            elif field_to_change == "driving_license_number":
                while True:
                    print("\nDriving license number has 2 letters followed by 7 digits or 1 letter followed by 8 digits.")
                    new_value = input("Enter driving license (XXDDDDDDD or XDDDDDDDD): ").upper()
                    if Helper.validate_driving_license(new_value):
                        break
                    print("Invalid format. Should be XX1234567 or X12345678")

            else:
                new_value = input(f"Enter new {display_name}: ")

            # Encrypt all fields except city
            encrypted_value = new_value if field_to_change == "city" else Helper.symmetric_encrypt(new_value)
            return database.update_traveler(input_id, field_to_change, encrypted_value)

        except Exception as e:
            logger.log_error(self, f"Error updating traveler: {e}")
            return False

    def delete_traveler(self, database, logger):
        try:
            logger.log_info(self, "Deleting traveler")
            travelers = database.return_all_travelers()
            print("\nCurrent travelers:")
            for traveler in travelers:
                print(f"ID: {traveler[0]}, "
                      f"First Name: {traveler[2]}, "
                      f"Last Name: {traveler[3]}, "
                      f"Birthday: {traveler[4]}")
            number_of_travelers = len(travelers)

            while True: # Checks if ID is on the list
                print("Enter the ID of the traveler you want to delete.")
                input_id = input("> ")
                try:
                    input_id = int(input_id)
                    if input_id > number_of_travelers:
                        print("Invalid ID. Please try again.")
                        continue
                    else:
                        break
                except:
                    print("Invalid ID. Please try again.")
                    continue

            traveler_to_delete = database.return_traveler_by_id(input_id)
            print("\nTraveler to delete:")
            print(f"ID: {traveler_to_delete[0]}")
            print(f"First Name: {Helper.symmetric_decrypt(traveler_to_delete[2])}")
            print(f"Last Name: {Helper.symmetric_decrypt(traveler_to_delete[3])}")
            print(f"Birthday: {Helper.symmetric_decrypt(traveler_to_delete[4])}")
            print(f"Gender: {Helper.symmetric_decrypt(traveler_to_delete[5])}")
            print(f"Street Name: {Helper.symmetric_decrypt(traveler_to_delete[6])}")
            print(f"House Number: {Helper.symmetric_decrypt(traveler_to_delete[7])}")
            print(f"Zip Code: {Helper.symmetric_decrypt(traveler_to_delete[8])}")
            print(f"City: {traveler_to_delete[9]}")  # City is not encrypted
            print(f"Email Address: {Helper.symmetric_decrypt(traveler_to_delete[10])}")
            print(f"Mobile Phone: {Helper.symmetric_decrypt(traveler_to_delete[11])}")
            print(f"Driving License: {Helper.symmetric_decrypt(traveler_to_delete[12])}")

            while True:
                print("\nAre you sure you want to delete this traveler? [Y/N]")
                choice = input("> ").upper().strip()
                if choice == "N":
                    return False
                elif choice == "Y":
                    return database.delete_traveler(input_id)
                print("Invalid choice. Please enter Y or N.")

        except Exception as e:
            logger.log_error(self, "Deleting scooter", e)
            return False

    def search_traveller(self, database, logger):
        try:
            logger.log_info(self, "Searching traveler")
            print("=== TRAVELER SEARCH ===")
            print("Enter search terms (leave blank to ignore a field)")

            first_name = input("First Name (partial match allowed): ").strip().lower()
            last_name = input("Last Name (partial match allowed): ").strip().lower()
            birthday = input("Birthday (partial match allowed): ").strip().lower()

            travelers = database.return_all_travelers()
            results = []

            for traveler in travelers:
                traveler_first_name = Helper.symmetric_decrypt(traveler[2]).strip().lower()
                traveler_last_name = Helper.symmetric_decrypt(traveler[3]).strip().lower()
                traveler_birthday = Helper.symmetric_decrypt(traveler[4]).strip().lower()

                first_name_match = not first_name or fuzz.partial_ratio(first_name, traveler_first_name) > 70
                last_name_match = not last_name or fuzz.partial_ratio(last_name, traveler_last_name) > 70
                serial_match = not birthday or birthday in traveler_birthday

                if first_name_match and last_name_match and serial_match:
                    results.append(traveler)

            if not results:
                print("\nNo matching travelers found.")
            else:
                print(f"\nFound {len(results)} matching travelers:")
                for traveler in results:
                    print(f"First Name: "
                          f"{Helper.symmetric_decrypt(traveler[2])}, "
                          f"Last Name: {Helper.symmetric_decrypt(traveler[3])}, "
                          f"Birthday: {Helper.symmetric_decrypt(traveler[4])}")

            return results
        except Exception as e:
            logger.log_error(self, "Searching traveler", e)
            return False

    def view_logs(self, database, logger):
        try:
            logger.log_info(self, "Viewing logs")
            print("=== LOGS ===")
            logs = database.return_all("logger")
            if not logs:
                print("No logs found.")
            else:
                for log in logs:
                    print(f"ID: {log[0]}, "
                          f"Date: {Helper.symmetric_decrypt(log[1])}, "
                          f"Time: {Helper.symmetric_decrypt(log[2])}, "
                          f"Username: {Helper.symmetric_decrypt(log[3])}, "
                          f"Activity: {Helper.symmetric_decrypt(log[4])}, "
                          f"Extra: {Helper.symmetric_decrypt(log[5])}, "
                          f"Risk: {Helper.symmetric_decrypt(log[6])}")
                return True
        except Exception as e:
            logger.log_error(self, "Viewing logs", e)
            return False

    "SYSTEM ADMIN STUFF"

    def change_own_password(self, database, logger):
        """Handles password change with proper hashing and validation"""
        try:
            logger.log_info(self, "Changing password")
            print("\n=== CHANGE PASSWORD ===")

            # Verify old password
            attempts = 0
            while attempts < 3:
                old_password = input("Enter current password: ").strip()
                if Helper.verify_password(old_password, self.password_hash):  # Changed to password_hash
                    break
                attempts += 1
                print(f"Invalid password. {3 - attempts} attempts remaining.")
            else:
                print("Too many failed attempts.")
                return False


            new_password = Helper.validate_password(input("Enter new password: ").strip())

            # Update password in database
            new_password_hash = Helper.hash_password(new_password)
            return database.change_own_password(
                user=self,
                new_password=new_password_hash,
            )

        except Exception as e:
            logger.log_error(self, f"Password change failed: {str(e)}")
            return False

    def update_own_profile(self, database, logger):
        try:
            logger.log_info(self, "Updating own profile")
            print("\n=== UPDATE OWN PROFILE ===")

            fields = ["First Name", "Last Name", "Username"]
            while True:
                print("Which field do you want to update?")
                for i, field in enumerate(fields, 1):
                    print(f"{i}. {field}")
                field = input("> ")
                try:
                    if int(field) > len(fields):
                        print("Invalid choice. Please try again.")
                except:
                    print("Invalid choice. Please try again.")
                break

            print(f"Please enter the new {fields[int(field) - 1]}:")
            new_value = input("> ")

            if database.update_own_profile_db(self, fields[int(field) - 1], new_value):
                return True
            return False

        except Exception as e:
            logger.log_error(self, "Updating own profile", e)
            return False