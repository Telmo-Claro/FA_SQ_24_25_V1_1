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
        self.database.add_log(Helper.symmetric_encrypt(date), Helper.symmetric_encrypt(time),
                              Helper.symmetric_encrypt(username),
                              Helper.symmetric_encrypt(activity_description),
                              Helper.symmetric_encrypt(additional_info),
                              Helper.symmetric_encrypt(suspicious_level))
        

    def log_info(self, user, activity_description, additional_info=""): # for normal activity
        """Log information messages"""
        self.log_to_database(
            user,
            activity_description,
            additional_info,
            suspicious_level="Low Risk"
        )

    def log_warning(self, user, activity_description, additional_info=""): # casual warnings
        """Log warning messages"""
        self.log_to_database(
            user,
            activity_description,
            additional_info,
            suspicious_level="Medium Risk"
        )


    def log_error(self, user, activity_description, additional_info: Exception):
        """Log an exception with optional context"""
        error_message = traceback.format_exc()      
        self.log_to_database(
            user,
            activity_description,
            error_message,
            suspicious_level="High Risk"
        )

