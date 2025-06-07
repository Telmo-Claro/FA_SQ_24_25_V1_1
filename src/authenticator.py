import models
import database
import helper

class Authenticator:
    def __init__(self, logger):
        self._logger = logger

    def auth_super_admin(self, username, password):
        db = database.Database(self._logger, "urban_mobility")
        users = db.get_users()
        username = helper.symmetric_decrypt(username)
        password = helper.utils_hash(password)
        for user in users:
            if user[2] == username and user[3] == password:
                return models.User(user[1], user[2], user[3], user[4], user[5], user[6])
            return None
        return None

    def auth_user(self, user, first_name, last_name, username, password, role, registration_date):
        self._logger.log_info(f"Authentication attempt for user: {username}", "AUTH")
        # ...existing code...