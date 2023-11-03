from .user import User

class Employee(User):
    """Special class for bank employees that internal service operations"""
    _poweruser = True

    def __init__(self, username, password):
        super().__init__(username, password)

    def menu_options(self):
        dict = {
            "1": "Check Balance",
            "2": "Pay in money",
            "4": "Deposit money",
            "5": "Generate Bank Report",
            "6": "Log off"
        }
        return dict
