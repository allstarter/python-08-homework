import json
from users.customer import Customer
from users.employee import Employee
from users.user import User

# getting application data in new shape
employees = json.loads(open("employees.json", "r").read())
customers = json.loads(open("customers.json", "r").read())

users: {str: User} = {}

# the ** operator does a cool trick for us ..
for username in employees:
    users[username] = Employee(username, **employees[username])

for username in customers:
    users[username] = Customer(username, **customers[username])

for username in users:
    print(f"User {username} is {users[username].__class__}")

# here you can start implementing your bank application using objects
# to check if a users element is Employee or not you could use isinstance()
# you will find old application also in the bank_application_old.py file

## Have fun ! ##
