import json

def authenticate(username, password):

    with open("users.json") as f:
        admin = json.load(f)

        if username in users:
            if password == users[username]["password"]:
                return True

    return False
