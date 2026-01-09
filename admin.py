import json


def get_password():
    while True:
        password = input("Enter password: ")
        if len(password) >= 8:
            return password
        else:
            print("Password must be at least 8 characters long.")


def get_full_name():
    while True:
        fullname = input("Enter FullName: ").strip()
        if not fullname:
            print("FullName must not be empty.")
        elif not fullname.isalpha():
            print("FullName must contain only letters.")
        else:
            return fullname


def get_username():
    while True:
        username = input("Enter username: ")
        if username.isalnum():
            return username
        else:
            print("Username must contain only letters and numbers.")


def get_role():
    roles = {"1": "user", "2": "admin"}
    while True:
        choice = input(f"Chose role {roles}")

        if choice == "1":
            return "user"
        elif choice == "2":
            return "admin"
        else:
            print("Give choice 1 or 2. Try again")


def create_account():
    users = []
    fullname = get_full_name()
    username = get_username()
    password = get_password()
    role=get_role()
    try:
        with open("users.json") as f:
            users = json.load(f)
            users.append(
                {"fullname": fullname, "username": username, "password": password, "role": role})
    except FileNotFoundError:
        users.append(
            {"fullname": fullname, "username": username, "password": password, "role": role})
    with open("users.json", "w") as f2:
        json.dump(users, f2)


create_account()
