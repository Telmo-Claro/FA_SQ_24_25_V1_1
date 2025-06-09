import logging
from logging import basicConfig

from pathlib import Path
import traceback
from datetime import datetime
import helper

"""
logging.debug()
logging.info()
logging.warning()
logging.error()
logging.critical()
"""

class Logger():
    def __init__(self):
        self.setup_logging()

    def setup_logging(self): # create a log file with datetime in the filename
        logs_dir = Path(__file__).parent.parent / "logs"
        logs_dir.mkdir(exist_ok=True)  # Create a logs directory if it doesn't exist
        log_file = logs_dir / f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log" # creates a timestamp in the filename
        logging.basicConfig(
            level=logging.INFO,
            filename=log_file,
            filemode='w',
            format="%(asctime)s - %(levelname)s - %(message)s")

    def log_info(self, username, message, context): # for normal activity
        """Log information messages"""
        logging.info(f"User: {username} / [{context}] {message} / Low Risk")

    def log_warning(self, username, message, context): # casual warnings
        """Log warning messages"""
        logging.warning(f"User: {username} / [{context}] {message} / Medium Risk ")

    def log_error(self, username, e: Exception, context): # severe errors in the code
        """Log an exception with optional context"""
        returned_error = traceback.format_exc()
        logging.error(f"User: {username} / [{context}] {returned_error} / High Risk")


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

