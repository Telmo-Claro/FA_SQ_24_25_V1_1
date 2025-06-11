import logging
from logging import basicConfig

from pathlib import Path
import traceback
from datetime import datetime
from helper import Helper

"""
logging.debug()
logging.info()
logging.warning()
logging.error()
logging.critical()
"""

class Logger():
    def __init__(self, db):
        self.setup_logging()
        self.database = db

    def log_to_database(self, user, activity_description, additional_info, suspicious_level):
        """Log activity to the database"""
        try:
            with self.database.get_connection() as conn:
                cursor = conn.cursor()
                query = """INSERT INTO logger (date, time, username, activity_description, additional_info, suspicious_level)
                           VALUES (?, ?, ?, ?, ?, ?)"""
                cursor.execute(query, (
                    datetime.now().strftime("%Y-%m-%d"),
                    datetime.now().strftime("%H:%M:%S"),
                    user.username,
                    activity_description,
                    additional_info,
                    suspicious_level
                ))
                conn.commit()
                cursor.close()
                return True
        except Exception as e:
            logging.error(f"Failed to log activity to database: {e}")
            logging.error(traceback.format_exc())
            return False
    def setup_logging(self): # create a log file with datetime in the filename
        logs_dir = Path(__file__).parent.parent / "logs"
        logs_dir.mkdir(exist_ok=True)  # Create a logs directory if it doesn't exist
        log_file = logs_dir / f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log" # creates a timestamp in the filename
        logging.basicConfig(
            level=logging.INFO,
            filename=log_file,
            filemode='w',
            format="%(asctime)s - %(levelname)s - %(message)s")

    def log_info(self, user, activity_description, additional_info): # for normal activity
        """Log information messages"""
        self.log_to_database(
            user=Helper.symmetric_encrypt(user.username),
            activity_description=Helper.symmetric_encrypt(activity_description),
            additional_info=Helper.symmetric_encrypt(additional_info),
            suspicious_level="Low Risk"
        )

    def log_warning(self, user, activity_description, additional_info): # casual warnings
        """Log warning messages"""
        self.log_to_database(
            user=Helper.symmetric_encrypt(user.username),
            activity_description=Helper.symmetric_encrypt(activity_description),
            additional_info=Helper.symmetric_encrypt(additional_info),
            suspicious_level="Medium Risk"
        )

    def log_exceptions(self, user, activity_description, additional_info: Exception):
        """Log an exception with optional context"""
        returned_error = traceback.format_exc()
        self.log_to_database(
            user=Helper.symmetric_encrypt(user.username),
            activity_description=Helper.symmetric_encrypt(activity_description),
            additional_info=Helper.symmetric_encrypt(additional_info),
            suspicious_level="High Risk"
        )

"""
Log regular activity
log.log_info("User", "User logged in", "AUTH")

Log warnings
log.log_warning("User", "Invalid input received", "UI")

Log errors
try:
    bla bla bla
except Exception as e:
    log.log_error(e, "DATABASE")
"""

