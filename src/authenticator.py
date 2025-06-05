import models
import database
import utils

class Authenticator:
    def __init__(self, logger):
        self._logger = logger

    def auth_super_admin(self, username, password):
        db = database.Database(self._logger, "urban_mobility")
        users = db.get_users()
        username = utils.symmetric_decrypt(username)
        password = utils.utils_hash(password)
        for user in users:
            if user[3] == username and user[4] == password:
                sa = models.SuperAdmin(user[0], user[1], user[2], user[3], user[4], user[5])
        self._logger.log_info(f"Authentication attempt for Super Admin: {username}", "AUTH")
        if username == sa.username and password == sa.password:
            self._logger.log_info("Super Admin authentication successful", "AUTH")
            return sa
        self._logger.log_warning("Failed Super Admin authentication attempt", "AUTH")
        return False

    def auth_user(self, user, first_name, last_name, username, password, role, registration_date):
        self._logger.log_info(f"Authentication attempt for user: {username}", "AUTH")
        # ...existing code...