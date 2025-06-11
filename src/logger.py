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

    def get_username(self, user):
        if hasattr(user, "username"):
            return user.username
        elif isinstance(user, str):
            return user
        elif user is None:
            return "Anonymous"
        else:
            return str(user)

    def log_to_database(self, user, activity_description, additional_info, suspicious_level):
        username = self.get_username(user)
        date = datetime.now().strftime("%Y-%m-%d")
        time = datetime.now().strftime("%H:%M:%S")
        username = Helper.symmetric_encrypt(username)
        activity_description = Helper.symmetric_encrypt(activity_description)
        additional_info = Helper.symmetric_encrypt(additional_info)
        self.database.add_log(date, time, username, activity_description, additional_info, suspicious_level)
        
    def setup_logging(self): # create a log file with datetime in the filename
        logs_dir = Path(__file__).parent.parent / "logs"
        logs_dir.mkdir(exist_ok=True)  # Create a logs directory if it doesn't exist
        log_file = logs_dir / f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log" # creates a timestamp in the filename
        logging.basicConfig(
            level=logging.INFO,
            filename=log_file,
            filemode='w',
            format="%(asctime)s - %(levelname)s - %(message)s")

    def log_info(self, user, activity_description, additional_info=""): # for normal activity
        """Log information messages"""
        username = self.get_username(user)
        self.log_to_database(
            user,
            activity_description,
            additional_info,
            suspicious_level="Low Risk"
        )
        logging.info(f"User activity logged: {username}, {activity_description}, {additional_info}, Low Risk")

    def log_warning(self, user, activity_description, additional_info=""): # casual warnings
        """Log warning messages"""
        username = self.get_username(user)
        self.log_to_database(
            user,
            activity_description,
            additional_info,
            suspicious_level="Medium Risk"
        )
        logging.warning(f"User activity logged: {username}, {activity_description}, {additional_info}, Medium Risk")

    def log_error(self, user, activity_description, additional_info: Exception):
        """Log an exception with optional context"""
        username = self.get_username(user)
        error_message = traceback.format_exc()      

        self.log_to_database(
            user,
            activity_description,
            error_message,
            suspicious_level="High Risk"
        )
        logging.error(f"User activity logged: {username}, {activity_description}, {additional_info}, High Risk")

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

