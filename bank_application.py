import json


# getting data
employees = json.loads(open("employee.json", "r").read())
users = json.loads(open("users.json", "r").read())


def register():
    pass

def login():
    username = input("Username: ")
    password = input("Password: ")

    if username in employees:
        if employees[username] == password:
            return ("employee", username)
    if username in users:
        if users[username] == password:
            return ("user", username)
    print("Wrong credentials.")
    # default action when a function finishes executing
    # return None

def user_menu():
    user_menu_dict = {
        "1": "Check Balance",
        "2": "Deposit Funds",
        "3": "Withdraw",
        "4": "Transaction History",
        "5": "Generate File Report",
        "6": "Log off"
    }


# Menu
menu = ["1. Register", "2. Login", "3. Exit"]

print("Welcome to Bank Application!")
print("Please login or register!")
while True:
    for item in menu:
        print(item)
    user_input = input("> ")
    if user_input == "1":
        register()
    elif user_input == "2":
        logged_user = login()
        if logged_user:
            print("welcome to the menu")
    elif user_input == "3":
        print("Thanks for using our Bank!")
        break
    else:
        print("Wrong option, please use 1, 2 or 3.")