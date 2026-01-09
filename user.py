import json


def get_username():
    while True:
        username = input("Enter username: ")
        if username.isalnum():
            return username
        else:
            print("Username must contain only letters and numbers.")


def get_password():
    while True:
        password = input("Enter password: ")
        if len(password) >= 8:
            return password
        else:
            print("Password must be at least 8 characters long.")


try:
    with open("users.json") as f:
        users = json.load(f)
except FileNotFoundError:
    users = []
username = get_username()
password = get_password()
found = False
for user in users:
    if user["username"] == username and user["password"] == password:
        if user["role"] == "admin":
            print("Wellcome Admin")

        else:
            print(f"Wellcome {user["fullname"]}")
        break
else:
    print("Wrong username or password")

