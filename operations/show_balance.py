from ..users.customer import Customer

class ShowBalance(Operation):
    """Show balance operation of a customer"""
    def __init__(self, summary):
        self._summary = summary

    def execute(self, user):
        customer = user
        print (f"{customer.balance}")
