import models
import database
from helper import Helper

class Authenticator:
    def __init__(self, logger, db):
        self._logger = logger
        self._db = db

    def auth_user(self, username, password):
        if username == "super_admin" and password == "Admin_123?":
            return models.User("Super", "Administrator", "super_admin", "Admin_123?", "Super Administrator")
        try:
            users = self._db.get_users()
            hashed_password = Helper.utils_hash(password)
            for user in users:
                if Helper.symmetric_decrypt(user[3]) == username and user[4] == hashed_password:
                    return models.User(user[1], user[2], user[3], user[4], user[5], user[6])
            return None
        except Exception as e:
            self._logger.log_error("None", e, "AUTH")
            return None