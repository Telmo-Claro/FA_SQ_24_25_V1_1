from data import database
from logs import logger
from src.UI import main

if __name__ == "__main__":
    logger.setup_logging() # initializes logging stuff
    db = database.Database("Urban Mobility")
    db.create()
    main.landing()
