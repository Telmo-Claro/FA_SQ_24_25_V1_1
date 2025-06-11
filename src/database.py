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
        self.add_user("Super", "Administrator",
                          "super_admin", "Admin_123?",
                          "Super Administrator")
        
    def create(self):
        try:
            with sqlite3.connect(self.path) as conn:
                cursor = conn.cursor()
                queries = [
                    """CREATE TABLE IF NOT EXISTS travelers (
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

                    """CREATE TABLE IF NOT EXISTS logger (
                        id INTEGER PRIMARY KEY,
                        date TEXT,
                        time TEXT,
                        username TEXT,
                        activity_description TEXT,
                        additional_info TEXT,
                        suspicious_level TEXT
                    )"""
                    ]
                for query in queries:
                    cursor.execute(query)
                cursor.close()
                conn.commit()
            return True
        except Exception as e:
            return False

    def get_users(self):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            query = """SELECT * FROM users"""
            cursor.execute(query)
            users = cursor.fetchall()
            cursor.close()
            return users

    def add_user(self, first_name, last_name,
                     username, password, user_role,
                     registration_date=datetime.now()):

        valid = self.user_exists(username)
        if not valid:
            try:
                with sqlite3.connect(self.path) as conn:
                    cursor = conn.cursor()
                    username = Helper.symmetric_encrypt(username)
                    password = Helper.utils_hash(password)
                    query = """INSERT INTO users (first_name, last_name, 
                                                  username, password, 
                                                  user_role, registration_date)
                               VALUES (?, ?, ?, ?, ?, ?)"""
                    cursor.execute(query, (first_name, last_name,
                                           username, password, user_role,
                                           registration_date))
                    cursor.close()
                    return True
            except Exception as e:
                
                return False
        return False

    def database_delete_user(self, username):
        try:
            with sqlite3.connect(self.path) as conn:
                cursor = conn.cursor()
                users = self.get_users()
                for user in users:
                    if Helper.symmetric_decrypt(user[3]) == username:
                        query = """DELETE FROM users WHERE username = ?"""
                        cursor.execute(query, (user[3],))
                        conn.commit()
                        return True
                return False
        except:
            return False

    def return_user(self, username):
        users = self.get_users()
        for user in users:
            if Helper.symmetric_decrypt(user[3]) == username:
                return User(
                    first_name=user[1],
                    last_name=user[2],
                    username=Helper.symmetric_decrypt(user[3]),
                    password=user[4],
                    role=user[5],
                )
        return False

    def update_user(self, current_username, first_name, last_name, username, password):
        with sqlite3.connect(self.path) as conn:
            users = self.get_users()
            cursor = conn.cursor()
            for user in users:
                if Helper.symmetric_decrypt(user[3]) == current_username:
                    query = """UPDATE users 
                                SET first_name = ?, last_name = ?, username = ?, password = ? 
                                WHERE username = ?"""
                    username_encrypted = Helper.symmetric_encrypt(username)
                    password_hashed = Helper.utils_hash(password)
                    cursor.execute(query, (first_name, last_name, username_encrypted, password_hashed, user[3]))
                    conn.commit()
                    cursor.close()
                    return True
        return False
        
    def user_exists(self, username):
        users = self.get_users()
        for user in users:
            if Helper.symmetric_decrypt(user[3]) == username:
                return True
        return False

    def add_traveller_data(self,
                           first_name, last_name, birthday, gender,
                           street_name, house_number, zip_code, city,
                           email_address, mobile_phone, driving_license_number):
        return

    def add_scooter_data(self,
                         brand, model, serial_number, top_speed, battery_capacity,
                         state_of_charge, target_range_soc, location, out_of_service_status,
                         mileage, last_maintenance_date):
        return

    def add_log(self, date, time, username, activity_description, additional_info, suspicious_level):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            query = """INSERT INTO logger (date, time, username, activity_description, additional_info, suspicious_level)
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