import sqlite3
from pathlib import Path

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
                self._logger.log_info("Database tables created successfully", "DATABASE")
        except Exception as e:
            self._logger.log_error(e, "during data setup")

    def add_user(self, user, Fname, Lname, Uname, Pword, Role, Rdate):
        self._logger.log_info(f"Attempting to add new user: {Uname}", "DATABASE")
        if user.role not in ["Super Administrator", "System Administrator"]:
            self._logger.log_warning(f"Unauthorized user role: {user.role} attempted to add new user", "DATABASE")
            return False
        try:
            with sqlite3.connect(self.path) as conn:
                cursor = conn.cursor()
                query = """INSERT INTO users (first_name, last_name, username, password, user_role, registration_date)
                           VALUES (?, ?, ?, ?, ?, ?)"""
                cursor.execute(query, (Fname, Lname, Uname, Pword, Role, Rdate))
                cursor.close()
                self._logger.log_info(f"Successfully added user: {Uname}", "DATABASE")
                return True
        except Exception as e:
            self._logger.log_error(e, "during add user to databse")
            return False