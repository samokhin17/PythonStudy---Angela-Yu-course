

class Account:
    def __init__(self, name, balance):
        self.balance = balance
        self.name = name

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount

