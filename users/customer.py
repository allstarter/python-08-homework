from .user import User

class Customer(User):
    """Special class for bank customers with their operations"""
    _poweruser = False

    def __init__(self, username, password, balance):
        super().__init__(username, password)
        self._balance = balance

    def save_as_dict(self):
        dict = super().save_as_dict()
        dict[self._username].append({"balance": self._balance})
        return dict
    
    def menu_options(self):
        dict = {
            "1": "Check Balance",
            "2": "Transfer money",
            "3": "Log off"
        }
        return dict
