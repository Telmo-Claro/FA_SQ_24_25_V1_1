# Same as Service Engineer:
# • To update the attributes of scooters in the system
# • To search and retrieve the information of a scooter (check note 2 below)
# Same as System Administrator:
# • To check the list of users and their roles.
# • To add a new Service Engineer to the backend system.
# • To modify or update an existing Service Engineer account and profile.
# • To delete an existing Service Engineer account.
# • To reset an existing Service Engineer password (a temporary password).
# • To see the logs file(s) of the backend system.
# • To add a new Traveller to the backend system.

# • To update the information of a Traveller in the backend system.
# • To delete a Traveller from the backend system.
# • To add a new scooter to the backend system.
# • To update the information of a scooter in the backend system.
# • To delete a scooter from the backend system.
# • To search and retrieve the information of a Traveller (check note 2 below).
# Specific for the Super Administrator:
# • To add a new System Administrator to the backend system.
# • To modify or update an existing System Administrator account and profile.
# • To delete an existing System Administrator account.
# • To reset an existing System Administrator password (a temporary password).
# • To make a backup of the backend system and to restore a backup.
# • To allow a specific System Administrator to restore a specific backup. For this purpose,
# the Super Administrator should be able to generate a restore-code linked to a specific
# backup and System Administrator. The restore-code is one-use-only.
# • To revoke a previously generated restore-code for a System Administrator.

# The fixed username must be: super_admin
# The fixed password must be: Admin_123?

from src.models.System_Administrator import SystemAdministrator

class SuperAdministrator:
    def __init__(self):
        self.username = "super_admin"
        self.password = "Admin_123?"
        self.first_name = "Super"
        self.last_name = "Administrator"

    def __str__(self):
        return f"Super Administrator: {self.username}, Name: {self.first_name} {self.last_name}"

    def CreateSystemAdmin(self):
        username = input(f"Username: ")
        password = input(f"Password: ")
        first_name = input(f"First Name: ")
        last_name = input(f"Last Name: ")
        NewSystemAdmin = SystemAdministrator(username, password, first_name, last_name)