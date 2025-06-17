import sqlite3
from pathlib import Path
from helper import Helper
from datetime import datetime
from models import User
from logger import Logger

class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.path = Path(__file__).parent / f"{db_name}.db"
        self.logger = Logger(self)

    def load(self):
        self.create()
        super_admin_added = self.add_user("Super", "Administrator",
                          Helper.symmetric_encrypt("super_admin"), Helper.utils_hash("Admin_123?"),
                          "Super Administrator")
        if super_admin_added:
            print("Super Admin added to the system...")
            print("")    

    def create(self):
        try:
            with sqlite3.connect(self.path) as conn:
                cursor = conn.cursor()
                queries = [
                    """CREATE TABLE IF NOT EXISTS travelers (
                        id INTEGER PRIMARY KEY,
                        registration_date DATETIME,
                        first_name TEXT,
                        last_name TEXT,
                        birthday DATETIME,
                        gender TEXT,
                        street_name TEXT,
                        house_number TEXT,
                        zip_code TEXT,
                        city TEXT,
                        email_address TEXT,
                        mobile_phone TEXT,
                        driving_license_number TEXT
                    )""",

                    """CREATE TABLE IF NOT EXISTS scooters (
                        id INTEGER PRIMARY KEY,
                        in_service_date DATETIME,
                        brand TEXT,
                        model TEXT,
                        serial_number TEXT,
                        top_speed TEXT,
                        battery_capacity TEXT,
                        state_of_charge TEXT,
                        target_range_soc TEXT,
                        location TEXT,
                        out_of_service_status BOOLEAN DEFAULT 0,
                        mileage TEXT,
                        last_maintenance_date TEXT
                    )""",

                    """CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        first_name TEXT,
                        last_name TEXT,
                        username TEXT UNIQUE,
                        password TEXT,
                        user_role TEXT,
                        registration_date DATE
                    )""",

                    """CREATE TABLE IF NOT EXISTS logger (
                        id INTEGER PRIMARY KEY,
                        date TEXT,
                        time TEXT,
                        username TEXT,
                        activity_description TEXT,
                        additional_info TEXT,
                        suspicious_level TEXT
                    )""",

                    """CREATE TABLE IF NOT EXISTS codes (
                        id INTEGER PRIMARY KEY,
                        code TEXT,
                        zip_name TEXT,
                        is_used BOOLEAN DEFAULT 0
                    )"""
                    ]
                for query in queries:
                    cursor.execute(query)
                conn.commit()
                cursor.close()
            return True
        except Exception as e:
            return False

    def add_to_database(self, table, fields, values):
        try:
            if not all([table, fields, values]):
                return False
            if len(fields) != len(values):
                return False

            placeholders = ", ".join(["?"] * len(values))
            field_names = ', '.join(fields)

            with sqlite3.connect(self.path) as conn:
                cursor = conn.cursor()

                query = f"INSERT INTO {table} ({field_names}) VALUES ({placeholders})"
                cursor.execute(query, values)

                conn.commit()
                return True

        except Exception as e:
            print(e)
            return False

    def delete_one(self, table, field, value):
        try:
            if not all([table, field]):
                return False

            with sqlite3.connect(self.path) as conn:
                cursor = conn.cursor()
                query = f"DELETE FROM {table} WHERE {field} = ?"
                cursor.execute(query, (value,))
                conn.commit()
                return True

        except Exception as e:
            print(f"Delete error: {e}")
            return False

    def update_one(self, table, field, value, id):
        try:
            if not all([table, field, value, id]):
                return False

            with sqlite3.connect(self.path) as conn:
                cursor = conn.cursor()
                query = f"UPDATE {table} SET {field} = ? WHERE id = ?"
                cursor.execute(query, (value, id))
                conn.commit()
                return True

        except Exception as e:
            print(f"Update error: {e}")
            return False

    def return_all(self, table):
        try:
            with sqlite3.connect(self.path) as conn:
                cursor = conn.cursor()
                query = f"SELECT * FROM {table}"
                cursor.execute(query)
                result = cursor.fetchall()
                conn.commit()
                return result

        except Exception as e:
            print(e)
            return False

    def get_users(self):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            query = """SELECT * FROM users"""
            cursor.execute(query)
            users = cursor.fetchall()
            conn.commit()
            cursor.close()
            return users

    "USER RELATED"
    def add_user(self, first_name, last_name,
                     encrypted_username, encrypted_password, user_role,
                     registration_date=datetime.now()):
        try:
            user_exists = self.user_exists(encrypted_username)
            if not user_exists:
                with sqlite3.connect(self.path) as conn:
                    cursor = conn.cursor()
                    query = """INSERT INTO users (first_name, last_name, 
                                                username, password, 
                                                user_role, registration_date)
                            VALUES (?, ?, ?, ?, ?, ?)"""
                    cursor.execute(query, (first_name, last_name,
                                        encrypted_username, encrypted_password, user_role,
                                        registration_date))
                    conn.commit()
                    cursor.close()
                    return True
            return False
        except Exception as e:
            return False

    def add_travelers(self, first_name, last_name, birthday, gender, street_name, house_number, zip_code, city,
                      email_address, mobile_phone, driving_license):
        try:
            with sqlite3.connect(self.path) as conn:
                cursor = conn.cursor()
                query = """INSERT INTO travelers (registration_date, first_name, last_name, birthday, 
                                                  gender, street_name, house_number, 
                                                  zip_code, city, email_address, 
                                                  mobile_phone, driving_license_number)
                           VALUES (?, ?, ?, ?, ?, ?)"""
                cursor.execute(query, (datetime.now(), first_name, last_name, birthday,
                                       gender, street_name, house_number,
                                       zip_code, city, email_address,
                                       mobile_phone, driving_license))
                conn.commit()
                cursor.close()
                return True
        except Exception as e:
            return False

    def update_user(self, current_username, first_name, last_name, encrypted_username, hashed_password):
        try:
            users = self.get_users()
            user_to_update_id = 0
            for user in users:
                if Helper.symmetric_decrypt(user[3]) == current_username:
                    user_to_update_id = user[0]
            with sqlite3.connect(self.path) as conn:
                cursor = conn.cursor()
                query = """UPDATE users 
                            SET first_name = ?, last_name = ?, username = ?, password = ? 
                            WHERE id = ?"""

                cursor.execute(query, (first_name, last_name, encrypted_username, hashed_password, user_to_update_id))
                conn.commit()
                cursor.close()
                return True
        except Exception as e:
            self.logger.log_error("Database", "Updating User", e)
            return False

    def delete_user(self, username):
        try:
            users = self.get_users()
            user_to_delete_id = 0
            for user in users:
               if Helper.symmetric_decrypt(user[3]) == username:
                    user_to_delete_id = user[0]
            with sqlite3.connect(self.path) as conn:
                cursor = conn.cursor()
                query = """DELETE FROM users WHERE id = ?"""
                cursor.execute(query, (user_to_delete_id,))
                conn.commit()
                cursor.close()
                return True
            return False
        except Exception as e:
            self.logger.log_error("Database", "Deleting User", e)
            return False

    def return_user(self, encrypted_username):
        users = self.get_users()
        for user in users:
            if Helper.symmetric_decrypt(user[3]) == Helper.symmetric_decrypt(encrypted_username):
                return User(
                    first_name=user[1],
                    last_name=user[2],
                    username=user[3],
                    password=user[4],
                    role=user[5],
                    id=user[0]
                )
        return False

    def user_exists(self, encrypted_username):
        try:
            users = self.get_users()
            for user in users:
                if Helper.symmetric_decrypt(user[3]) == Helper.symmetric_decrypt(encrypted_username):
                    return True
        except Exception as e:
            print(e)
            return False

    "LOGGING RELATED"
    def add_log(self, date, time, username, activity_description, additional_info, suspicious_level):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            query = """INSERT INTO logger (date, time, username, activity_description, 
                                           additional_info, suspicious_level)
                    VALUES (?, ?, ?, ?, ?, ?)"""
            cursor.execute(query, (
                date,
                time,
                username,
                activity_description,
                additional_info,
                suspicious_level
            ))
            conn.commit()
            cursor.close()
            return True

    "ONE TIME USE CODE RELATED"
    def add_one_time_use_code(self, zip_name, code ):
        try:
            self.revoke_one_time_use_code()  # Make sure all previous codes are unusable
            with sqlite3.connect(self.path) as conn:
                cursor = conn.cursor()
                query = """INSERT INTO codes (code, zip_name, is_used)
                        VALUES (?, ?, ?)"""
                cursor.execute(query, (code, zip_name, 0))
                conn.commit()
                cursor.close()
                return True
        except Exception as e:
            return False

    def revoke_one_time_use_code(self):
        try:
            with sqlite3.connect(self.path) as conn:
                cursor = conn.cursor()
                query = "UPDATE codes SET is_used = 1"
                cursor.execute(query)
                conn.commit()
                cursor.close()
                return True
        except Exception as e:
            return False

    def return_one_time_use_code(self):
        try:
            with sqlite3.connect(self.path) as conn:
                cursor = conn.cursor()
                # Get the most recent unused code
                query = """SELECT code FROM codes
                          WHERE is_used = 0
                          AND zip_name = ?
                          ORDER BY id DESC
                          """
                cursor.execute(query)
                result = cursor.fetchone()

                if result:
                    code = result[0]
                    # Mark code as used
                    update_query = """UPDATE codes SET is_used = 1
                                   WHERE code = ?"""
                    cursor.execute(update_query, (code,))
                    conn.commit()
                    cursor.close()
                    return code
                return None
        except Exception as e:
            print(e)
            return None

    "SCOOTER RELATED"

    def add_scooter(self, brand, model, serial_number,
                    top_speed, battery_capacity, state_of_charge, target_range_soc,
                    location, mileage, last_maintenance_date):
        try:
            with sqlite3.connect(self.path) as conn:
                cursor = conn.cursor()
                query = """INSERT INTO scooters (in_service_date, brand, model, serial_number, \
                                                 top_speed, battery_capacity, state_of_charge, \
                                                 target_range_soc, location, out_of_service_status, \
                                                 mileage, last_maintenance_date) \
                           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

                cursor.execute(query, (
                    datetime.now(),
                    brand,
                    model,
                    serial_number,
                    top_speed,
                    battery_capacity,
                    state_of_charge,
                    target_range_soc,
                    location,
                    True,
                    mileage,
                    last_maintenance_date
                ))

                conn.commit()
                return True

        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return False
        except Exception as e:
            print(f"Unexpected error: {e}")
            return False

    def return_all_scooters(self):
        try:
            with sqlite3.connect(self.path) as conn:
                cursor = conn.cursor()
                query = """SELECT * FROM scooters"""
                cursor.execute(query)
                scooters = cursor.fetchall()
                conn.commit()
                cursor.close()
                return scooters
        except Exception as e:
            print(e)
            return False

    def return_scooter_by_id(self, scooter_id):
        try:
            with sqlite3.connect(self.path) as conn:
                cursor = conn.cursor()
                query = """SELECT * FROM scooters WHERE id = ?"""
                cursor.execute(query, (scooter_id,))
                scooter = cursor.fetchone()
                conn.commit()
                cursor.close()
                return scooter
        except Exception as e:
            print(e)
            return False

    def update_scooter(self, scooter_id, field_to_change, new_field):
        try:
            with sqlite3.connect(self.path) as conn:
                cursor = conn.cursor()
                query = f"UPDATE scooters SET {field_to_change} = ? WHERE id = ?"
                cursor.execute(query, (new_field, scooter_id))
                conn.commit()
                return True
        except Exception as e:
            print(f"Database error: {e}")
            return False

    def delete_scooter(self, scooter_id):
        try:
            with sqlite3.connect(self.path) as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM scooters WHERE id = ?", (scooter_id,))
                conn.commit()
                if cursor.rowcount > 0:
                    return True
        except Exception as e:
            print(f"Database error: {e}")
            return False

    "TRAVELER RELATED"

    def add_traveler(self, first_name, last_name, birthday, gender,
                     street_name, house_number, zip_code, city,
                     email_address, mobile_phone, driving_license_number):
        try:
            with sqlite3.connect(self.path) as conn:
                cursor = conn.cursor()
                query = """INSERT INTO travelers (registration_date, first_name, last_name, \
                                                  birthday, gender, street_name, \
                                                  house_number, zip_code, city, email_address, \
                                                  mobile_phone, driving_license_number) \
                           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

                cursor.execute(query, (
                    datetime.now(), first_name, last_name, birthday, gender, street_name, house_number,
                    zip_code, city, email_address, mobile_phone, driving_license_number
                ))
                conn.commit()
                return True
        except Exception as e:
            print(f"Database error: {e}")
            return False

    def return_all_travelers(self):
        try:
            with sqlite3.connect(self.path) as conn:
                cursor = conn.cursor()
                query = """SELECT * FROM travelers"""
                cursor.execute(query)
                travelers = cursor.fetchall()
                conn.commit()
                return travelers
        except Exception as e:
            print(e)
            return False

    def return_traveler_by_id(self, traveler_id):
        try:
            with sqlite3.connect(self.path) as conn:
                cursor = conn.cursor()
                query = """SELECT * FROM travelers WHERE id = ?"""
                cursor.execute(query, (traveler_id,))
                traveler = cursor.fetchone()
                conn.commit()
                return traveler
        except Exception as e:
            print(e)
            return False

    def update_traveler(self, traveler_id, field_to_change, new_field):
        try:
            with sqlite3.connect(self.path) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT id FROM travelers WHERE id = ?", (traveler_id,))
                if not cursor.fetchone():
                    print("Traveler not found.")
                    return False

                query = f"""UPDATE travelers
                            SET {field_to_change} = ?
                            WHERE id = ?"""

                cursor.execute(query, (new_field, traveler_id))
                conn.commit()
                return True
        except Exception as e:
            print(f"Database update error: {e}")
            return False

    def delete_traveler(self, traveler_id):
        try:
            with sqlite3.connect(self.path) as conn:
                cursor = conn.cursor()

                cursor.execute("SELECT id FROM travelers WHERE id = ?", (traveler_id,))
                if not cursor.fetchone():
                    print("Traveler not found.")
                    return False

                cursor.execute("DELETE FROM travelers WHERE id = ?", (traveler_id,))
                conn.commit()
                print("Traveler deleted successfully.")
                return True

        except sqlite3.Error as e:
            print(f"Database error: {str(e)}")
            return False
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            return False

    def change_own_password(self, user, new_password):
        try:
            with sqlite3.connect(self.path) as conn:
                cursor = conn.cursor()
                query = """UPDATE users 
                            SET password = ? 
                            WHERE id = ?"""
                cursor.execute(query, (new_password, user.id))
                conn.commit()
                return True

        except Exception as e:
            print(e)
            return False

    def update_own_profile_db(self, user, field_to_change, new_field):
        try:
            with sqlite3.connect(self.path) as conn:
                cursor = conn.cursor()
                if field_to_change == "First Name":
                    field_to_change = "first_name"
                elif field_to_change == "Last Name":
                    field_to_change = "last_name"
                elif field_to_change == "Username":
                    field_to_change = "username"
                    new_field = Helper.symmetric_encrypt(new_field)
                else:
                    return False

                query = f"UPDATE users SET {field_to_change} = ? WHERE id = ?"
                cursor.execute(query, (new_field, user.id))
                if cursor.rowcount == 0:
                    print("No rows were updated - user ID may not exist")
                    return False
                conn.commit()
                return True
        except Exception as e:
            print(f"Database error: {e}")
            return False
    
    def delete_own_account(self, user):
        try:
            with sqlite3.connect(self.path) as conn:
                cursor = conn.cursor()
                query = """DELETE FROM users WHERE id = ?"""
                cursor.execute(query, (user.id,))
                conn.commit()
                if cursor.rowcount > 0:
                    return True
                else:
                    print("No rows were deleted - user ID may not exist")
                    return False
        except Exception as e:
            print(f"Database error: {e}")
            return False
        