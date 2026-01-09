# Manage reminders stored in a JSON file

import json
import os

filename = "Reminders.txt"

# Ensure the file exists
if not os.path.exists(filename):
    with open(filename, "w") as f:
        json.dump([], f)  # start with an empty list

while True:
    # Load reminders safely
    with open(filename, "r") as f:
        try:
            reminders = json.load(f)
            if not isinstance(reminders, list):
                reminders = []
        except json.JSONDecodeError:
            reminders = []

    print("\n--------------------------------")
    menu = ["1: Insert Reminder", "2: Delete Reminder", "3: Print Reminders", "4: Exit"]
    for option in menu:
        print(option)

    # Get choice safely
    try:
        choice = int(input("Make a choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        new_reminder = input("Enter reminder: ")
        reminders.append(new_reminder)
        with open(filename, "w") as f:
            json.dump(reminders, f)

    elif choice == 2:
        if not reminders:
            print("No reminders to delete.")
            continue
        try:
            for i, reminder in enumerate(reminders, 1):
                print(f"{i}: {reminder}")
            index = int(input("Enter reminder number to delete: ")) - 1
            reminders.pop(index)
            with open(filename, "w") as f:
                json.dump(reminders, f)
        except (ValueError, IndexError):
            print("Invalid reminder number.")

    elif choice == 3:
        if not reminders:
            print("No reminders found.")
        else:
            for i, reminder in enumerate(reminders, 1):
                print(f"{i}: {reminder}")

    elif choice == 4:
        print("Exiting...")
        break

    else:
        print("Invalid choice. Try again.")
