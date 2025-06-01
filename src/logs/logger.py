import logging
from pathlib import Path
import traceback
from datetime import datetime

def setup_logging():
    # create a log file with datetime in the filename
    log_file = Path(__file__).parent / f"error_log_{datetime.now().strftime('%Y%m%d')}.log"
    logging.basicConfig(
        level=logging.ERROR, 
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[logging.FileHandler(log_file)])
    
def log_exception(e: Exception, context: str = ""):
    """Log an exception with optional context"""
    logging.error(f"Exception occurred{f' in {context}' if context else ''}: {str(e)}")
    logging.error(traceback.format_exc())