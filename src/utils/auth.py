from src.models.super_administrator import *

def auth_super_admin(username, password):
    sa = SuperAdministrator
    if username == sa.username and password == sa.password:
        return sa
    return False

def auth_user(user, first_name, last_name, username, password, role, registration_date):
    return