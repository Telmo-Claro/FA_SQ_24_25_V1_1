import user_interface as ui
import logger
import database

if __name__ == "__main__":
    log = logger.Logger() # initialize the logger
    db = database.Database("urban_mobility")
    db.load()
    main_ui = ui.Ui(log, db) # initializes the main UI
    main_ui.landing() # start the application with the landing page
