import user_interface as ui
from logger import Logger
from database import Database

if __name__ == "__main__":
    db = Database("urban_mobility")
    db.load()
    log = Logger(db) # initialize the logger
    main_ui = ui.Ui(log, db) # initializes the main UI
    main_ui.landing() # start the application with the landing page