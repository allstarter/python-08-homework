class User:
    """Basic class for bank application user that handle login and logout"""
    def __init__(self, username, password):
        self._username = username
        self._password = password
        self._loggedin = False

    def login(self, password):
        if self._password == password:
            self._loggedin = True
        else:
            self._loggedin = False
        return self._loggedin

    def logout(self):
        self._loggedin = False    
