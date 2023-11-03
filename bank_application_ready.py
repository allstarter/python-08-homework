import json


# getting data
employees = json.loads(open("employee.json", "r").read())
users = json.loads(open("users.json", "r").read())
balances = json.loads(open("balances.json", "r").read())
print(balances)


def register():
    while True:
        username = input("Username: ")
        if username == "":
            print("Username must not be empty.")
        if username in users:
            print("Username already exists. Please try another one.")
        else:
            break

    while True:
        password = input("Password: ")
        if password == "":
            print("Password must not be empty.")
            continue

        password_repeat = input("Repeat Password: ")
        if password != password_repeat:
            print("Passwords are different. Please try again.")
        else:
            break

    users[username] = password
    with open('users.json', 'w', encoding='utf-8') as f:
        json.dump(users, f, ensure_ascii=False)

    while True:
        try:
            balance = int(input("Starting Balance: "))
            break
        except ValueError:
            print("That's not a valid number!")

    balances[username] = balance
    with open('balances.json', 'w', encoding='utf-8') as f:
        json.dump(users, f, ensure_ascii=False)


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


def user_menu(username):
    user_menu_dict = {
        "1": "Check Balance",
        "2": "Deposit Funds",
        "3": "Withdraw",
        "4": "Transaction History",
        "5": "Generate File Report",
        "6": "Log off"
    }

    while True:
        for key in user_menu_dict:
            print(f"{key}. {user_menu_dict[key]}")
        user_input = input("> ")
        if user_input == "1":
            print(user_menu_dict["1"])
            print(balances[username])
        if user_input in ["2", "3", "4", "5"]:
            print("We currently running maintenance. Please try later again.")
        elif user_input == "6":
            print("Goodbye {username}!")
            break
    else:
        print("Wrong option, please use 1, 2, 3, 4, 5 or 6.")


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
        if logged_user and logged_user[0] == "user":
            print("welcome to the menu")
            user_menu(logged_user[1])
        if logged_user and logged_user[0] == "employee":
            print("We currently running maintenance. Please try later again.")
    elif user_input == "3":
        print("Thanks for using our Bank!")
        break
    else:
        print("Wrong option, please use 1, 2 or 3.")