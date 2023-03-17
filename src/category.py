# Describes a budget category, marking deposits and withdrawals in a ledger
class Category():
    # Creates a new Category object with a passed "name" attribute and an empty
    # ledger
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    # Takes an amount and optionally a description and adds a transaction item 
    # to the ledger
    def deposit(self, amount, description = ""):
        self.ledger.append(
            {"amount": amount, "description": description}
        )
    
    # Takes an amount and optionally a description, and attempts to withdraw
    # the amount from the ledger. If there are sufficient funds to cover it, 
    # the amount is registered as a negative deposit in the ledger
    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            self.deposit(amount * -1, description)
            return True
        else:
            return False

    # Takes an amount and a destination Category, and attempts to transfer the 
    # amount from the current object to the destination one. Like withdraw, 
    # something is added to the ledger only in the case that the current object
    # has funds to cover the transaction
    def transfer(self, amount, destination):
        if self.withdraw(amount, "Transfer to " + destination.name):
            destination.deposit(amount, "Transfer from " + self.name)
            return True
        else:
            return False

    # Sums up the current items in the object's ledger and returns the value. 
    # Should always be 0 or greater, as overdraws are not allowed
    def get_balance(self):
        balance = 0.0
        for item in self.ledger:
            balance += item["amount"]
        return balance
    
    # Checks to see if amount passed can be covered by the current balance 
    # of the object's ledger and returns True or False accordingly
    def check_funds(self, amount):
        if amount <= self.get_balance():
            return True
        else:
            return False