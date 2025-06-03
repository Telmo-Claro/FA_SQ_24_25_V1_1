import models

class Authenticator():
    def __init__(self, logger):
        self._logger = logger
        

    def auth_super_admin(self, username, password):
        sa = models.SuperAdministrator()
        self._logger.log_info(f"Authentication attempt for Super Admin: {username}", "AUTH")
        if username == sa.username and password == sa.password:
            self._logger.log_info("Super Admin authentication successful", "AUTH")
            return sa
        self._logger.log_warning("Failed Super Admin authentication attempt", "AUTH")
        return False

    def auth_user(self, user, first_name, last_name, username, password, role, registration_date):
        self._logger.log_info(f"Authentication attempt for user: {username}", "AUTH")
        # ...existing code...