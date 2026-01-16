import json

teachers = []


def create_teacher(name, surname):
    if not check_teacher(name, surname):
        teachers.append({"id": next_id(), "first_name": name, "last_name": surname})
        save_teachers_data()


def read_teacher(id_teacher):
    for teacher in teachers:
        if teacher["id"] == id_teacher:
            print(f"The teacher with id {id_teacher} is {teacher["last_name"]} {teacher["first_name"]}")
            return True
    else:
        print(f"The teacher with id {id_teacher}  doesnt exists")
        return False


def update_teacher(id_teacher, key, new_value):
    for teacher in teachers:
        if teacher["id"] == id_teacher:
            teacher[key] = new_value
            print("The update was successfully")
            save_teachers_data()
            return
    else:
        print("The update_teacher failed. The id doesnt exist")


def delete_teacher(id_teacher):
    for teacher in teachers:
        if teacher["id"] == id_teacher:
            teachers.remove(teacher)
            print(f"The teacher with id {id_teacher} deleted successfully")
            save_teachers_data()
            return
    else:
        print("The Delete_teacher failed. The id doesnt exist")


def check_teacher(name, lastname):
    for teacher in teachers:
        if teacher["first_name"].lower() == name.lower() and teacher["last_name"].lower() == lastname.lower():
            print("The teacher you entered already exists:")
            print(teacher)
            return True
    return False


def next_id():
    if teachers:
        return max(teacher["id"] for teacher in teachers) + 1
    return 1000# starting ID


def init_teachers_data():
    global teachers
    try:
        with open("teachers.json") as f:
            teachers = json.load(f)
    except FileNotFoundError:
        print("File not Found")

def save_teachers_data():
    with open("teachers.json","w") as f:
        json.dump(teachers,f)