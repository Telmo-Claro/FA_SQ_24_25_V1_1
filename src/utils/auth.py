from src.models.Super_Administrator import SuperAdministrator

def auth_super_admin(username, password):
    sa = SuperAdministrator()
    if username is sa.username and password is sa.password:
        return True
    return False