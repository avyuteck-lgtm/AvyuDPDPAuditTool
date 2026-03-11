import json

def authenticate(username, password):

    with open("admin_config.json") as f:
        admin = json.load(f)

    if username == admin["username"] and password == admin["password"]:
        return True

    return False