import sqlite3
from pathlib import Path
from src.models.System_Administrator import SystemAdministrator
from src.logs.logger import log_exception

class database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.path = Path(__file__).parent / f"{db_name}.db"

    def create(self):
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
                        last_maintenance_date TEXT
                    )""",

                    """CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        username TEXT UNIQUE,
                        password TEXT,
                        role TEXT
                        first_name TEXT,
                        last_name TEXT,
                        registration_date TEXT
                    )""",

                    ]
                for query in queries:
                    cursor.execute(query)
                cursor.close()
        except sqlite3.OperationalError as e:
            log_exception(e, "during database setup")

