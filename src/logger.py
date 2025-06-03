import logging
from pathlib import Path
import traceback
from datetime import datetime

class Logger():
    def __init__(self):
        self.setup_logging()

    def setup_logging(self): # create a log file with datetime in the filename
        logs_dir = Path(__file__).parent.parent / "logs"
        logs_dir.mkdir(exist_ok=True)  # Create logs directory if it doesn't exist
        log_file = logs_dir / f"activity_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log" # creates a timestamp in the filename
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file)])
        
    def log_info(self, message: str, context: str = ""): # for normal activity
        """Log information messages"""
        logging.info(f"{f'[{context}] ' if context else ''}{message}")

    def log_warning(self, message: str, context: str = ""): # casual warnings
        """Log warning messages"""
        logging.warning(f"{f'[{context}] ' if context else ''}{message}")

    def log_error(self, e: Exception, context: str = ""): # severe errors in the code
        """Log an exception with optional context"""
        logging.error(f"Exception occurred{f' in {context}' if context else ''}: {str(e)}")
        logging.error(traceback.format_exc())


"""
Log regular activity
log.log_info("User logged in", "AUTH")

Log warnings
log.log_warning("Invalid input received", "UI")

Log errors
try:
    bla bla bla
except Exception as e:
    log.log_error(e, "DATABASE")
"""

