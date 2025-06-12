import models
from helper import Helper

class Authenticator:
    def __init__(self, logger, db):
        self._logger = logger
        self._db = db

    def auth_user(self, encrypted_username, hashed_password):
        if Helper.symmetric_decrypt(encrypted_username) == "super_admin" and hashed_password == Helper.utils_hash("Admin_123?"):
            self._logger.log_info("Super Admin", "Logged in", "")
            return models.User("Super", "Administrator", "super_admin", "Admin_123?", "Super Administrator")
        try:
            users = self._db.get_users()
            for user in users:
                if user[3] == encrypted_username and user[4] == hashed_password:
                    self._logger.log_info(f"{encrypted_username}", "Logged in", "")
                    return models.User(user[1], user[2], user[3], user[4], user[5])
            return False
        except Exception as e:
            return False