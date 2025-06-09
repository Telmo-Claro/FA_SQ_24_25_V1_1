import models
import database
import helper

class Authenticator:
    def __init__(self, logger):
        self._logger = logger

    def auth_super_admin(self, username, password):
        try:
            db = database.Database(self._logger, "urban_mobility")
            users = db.get_users()
            hashed_password = helper.utils_hash(password)
            encrypted_username = helper.symmetric_encrypt(username)
        
            for user in users:
                if user[3] == encrypted_username and user[4] == hashed_password:
                    return models.User(user[1], user[2], user[3], user[4], user[5], user[6])
            return False
        except Exception as e:
            self._logger.log_error(e, "AUTH")
            return False

    def auth_user(self, user, first_name, last_name, username, password, role, registration_date):
        self._logger.log_info(f"Authentication attempt for user: {username}", "AUTH")
        # ToDo: implement other user types authentication