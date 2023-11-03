class Operation:
    """Basic class for bank operation a user can do"""
    def __init__(self, summary):
        self._summary = summary

    def execute(self, user):
        pass
