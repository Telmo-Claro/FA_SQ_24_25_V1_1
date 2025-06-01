# Same as Service Engineer:
# • To update their own password.
# • To update the attributes of scooters in the system
# • To search and retrieve the information of a scooter (check note 2 below)
# Specific for the System Administrator:
# • To check the list of users and their roles.
# • To add a new Service Engineer to the system.
# • To update an existing Service Engineer account and profile.
# • To delete an existing Service Engineer account.
# • To reset an existing Service Engineer password (a temporary password).
# • To update his own account and profile.
# • To delete his own account.
# • To make a backup of the backend system.
# • To restore a specific backup of the backend system. For this purpose, the Super Administrator has generated a specific ‘one-use only’ code to restore a specific backup.
# • To see the logs file(s) of the backend system.
# • To add a new Traveller to the backend system.
# • To update the information of a Traveller in the backend system.
# • To delete a Traveller record from the backend system.
# • To add a new scooter to the backend system.
# • To update the information of a scooter in the backend system.
# • To delete a scooter from the backend system.
# • To search and retrieve the information of a Traveller (check note 2 below).

from datetime import datetime

class SystemAdministrator:
    def __init__(self, username, password, first_name, last_name, registration_date=datetime.now()):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.registration_date = registration_date

    def __str__(self):
        return f"System Administrator: {self.username}, Name: {self.first_name} {self.last_name}, Registered on: {self.registration_date}"