from src.models.super_administrator import SuperAdministrator
from src.models.user import User

def auth_super_admin(username, password):
    sa = SuperAdministrator
    if username is sa.username and password is sa.password:
        return sa
    return False

def auth_user(username, password, role):
    return