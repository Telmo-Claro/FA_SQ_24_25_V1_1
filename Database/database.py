import sqlite3

class database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def create(self):
        self.connect()
        self.create_tables()
        self.close()

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.db_name)
        except sqlite3.OperationalError as e:
            print(f"Failed to open database", e)

    def close(self):
        if self.connection:
            self.connection.close()
            print(f"Connection to database closed")

    def create_tables(self):
        sql_statements = [
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

    """CREATE TABLE IF NOT EXISTS service_engineers (
        id INTEGER PRIMARY KEY,
        username TEXT UNIQUE,
        password TEXT,
        first_name TEXT,
        last_name TEXT,
        registration_date TEXT
    )""",
    
    """CREATE TABLE IF NOT EXISTS system_administrators (
        id INTEGER PRIMARY KEY,
        username TEXT UNIQUE,
        password TEXT,
        first_name TEXT,
        last_name TEXT,
        registration_date TEXT
    )""",
    ]
        if not self.connection:
            print("No database connection established.")
            return
        
        cursor = self.connection.cursor()
        for query in sql_statements:
            try:
                cursor.execute(query)
            except sqlite3.OperationalError as e:
                print(f"Failed to execute query", e)
        
        self.connection.commit()
        print("All queries executed successfully")
