# Service Engineers are employees of Urban Mobility who are responsible for the management of the scooter-fleet. Hence, they need to be able to manage some attributes of the existing scooter information. They are not allowed to add new or delete existing scooters. So, the minimum required functions of a Service Engineer in the system are summarized as below:
# • To update their own password
# • To update some attributes of scooters in the system
# • To search and retrieve the information of a scooter (check note 2 below)

from datetime import datetime

class ServiceEngineer:
    def __init__(self, username, password, first_name, last_name, registration_date = datetime.now()):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.registration_date = registration_date

    def __str__(self):
        return f"Service Engineer: {self.username}, Name: {self.first_name} {self.last_name}, Registered on: {self.registration_date}"