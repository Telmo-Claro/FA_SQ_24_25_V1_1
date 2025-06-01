from database.database import database
from src.UI import ui
from logs.logger import setup_logging, log_exception

# Initialize logging at application start
if __name__ == "__main__":
    setup_logging()
    db = database("Urban Mobility")
    db.create()
    userinterface = ui.ui()
    userinterface.landing()
