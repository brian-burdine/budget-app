class Category():
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def deposit(self, amount, *description):
        if description:
            self.ledger.append(
                {"amount": amount, "description": description}
            )
        else:
            self.ledger.append(
                {"amount": amount, "description": ""}
            )
