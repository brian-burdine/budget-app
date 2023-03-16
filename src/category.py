class Category():
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def deposit(self, amount, description = ""):
        self.ledger.append(
            {"amount": amount, "description": description}
        )
    
    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            self.deposit(amount * -1, description)
            return True
        else:
            return False

    def transfer(self, amount, destination):
        if self.check_funds(amount):
            self.withdraw(amount)
            destination.deposit(amount)
            return True
        else:
            return False

    def get_balance(self):
        balance = 0.0
        for item in self.ledger:
            balance += item["amount"]
        return balance
    
    def check_funds(self, amount):
        if amount <= self.get_balance():
            return True
        else:
            return False