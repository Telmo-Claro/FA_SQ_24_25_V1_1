import sqlite3
from pathlib import Path
import helper

class Database:
    def __init__(self, logger, db_name):
        self._logger = logger
        self.db_name = db_name
        self.path = Path(__file__).parent / f"{db_name}.db"

    def create(self):
        self._logger.log_info(f"Creating database", "DATABASE")
        try:
            with sqlite3.connect(self.path) as conn:
                cursor = conn.cursor()
                queries = [
                    """CREATE TABLE IF NOT EXISTS travellers (
                        id INTEGER PRIMARY KEY,
                        first_name TEXT,
                        last_name TEXT,
                        birthday TEXT,
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
                        brand TEXT,
                        model TEXT,
                        serial_number TEXT,
                        top_speed TEXT,
                        battery_capacity TEXT,
                        state_of_charge TEXT,
                        target_range_soc TEXT,
                        location TEXT,
                        out_of_service_status TEXT,
                        mileage TEXT,
                        last_maintenance_date DATE
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

                    ]
                for query in queries:
                    cursor.execute(query)
                cursor.close()
                conn.commit()
                self._logger.log_info("Database tables created successfully", "DATABASE")

        except Exception as e:
            self._logger.log_error(e, "during data setup")

    def add_user(self, Fname, Lname, Uname, Pword, Role, Rdate):
        self._logger.log_info(f"Attempting to add new user: {Uname}", "DATABASE")
        try:
            with sqlite3.connect(self.path) as conn:
                cursor = conn.cursor()
                Uname = helper.symmetric_encrypt(Uname)
                Pword = helper.utils_hash(Pword)
                query = """INSERT INTO users (first_name, last_name, 
                                              username, password, 
                                              user_role, registration_date)
                           VALUES (?, ?, ?, ?, ?, ?)"""
                cursor.execute(query, (Fname, Lname, Uname, Pword, Role, Rdate))
                cursor.close()
                self._logger.log_info(f"Successfully added user: {Uname}", "DATABASE")
                return True
        except Exception as e:
            self._logger.log_error(e, "during add user to databse")
            return False

    def delete_user(self, username, password):
        self._logger.log_info(f"Attempting to delete user: {username}", "DATABASE")
        users = self.get_users()
        to_delete = None
        for user in users:
            if helper.symmetric_decrypt(user[2]) == username and helper.utils_hash(user[3]) == password:
                to_delete = user
        try:
            with sqlite3.connect(self.path) as conn:
                cursor = conn.cursor()
                query = """DELETE FROM users WHERE username = ? AND password = ?"""
                cursor.execute(query, (username, password))
                cursor.close()
                self._logger.log_info(f"Successfully deleted user: {username}", "DATABASE")
                return True
        except Exception as e:
            self._logger.log_error(e, "during delete user from database")
            return False

    def get_users(self):
        self._logger.log_info(f"Attempting to get usernames and passwords", "DATABASE")
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            query = """SELECT * FROM users"""
            cursor.execute(query)
            users = cursor.fetchall()
            cursor.close()
            self._logger.log_info(f"Successfully retrieved usernames and passwords", "DATABASE")
            return users
        
