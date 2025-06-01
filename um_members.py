from Database.database import database
from UI import ui

if __name__ == "__main__":
    db = database("UMDB.db")
    db.create()
    userinterface = ui.ui(True)
    userinterface.landing(True)
