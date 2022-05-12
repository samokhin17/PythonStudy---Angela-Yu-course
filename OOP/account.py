import pytz
import datetime

class Account:
    def __init__(self, name, balance):
        self.history = []
        self.balance = balance
        self.name = name


    def deposit(self, amount):
        self.balance += amount
        self.show_balance()
        self.history.append([amount, pytz.utc.localize(datetime.utcnow())])

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            print(f'You spent {amount} units')
            self.show_balance()
        else:
            print('Not enough money')
            self.show_balance()

    def show_balance(self):
        print(f'Balance: {self.balance}')

a = Account('Sasha', 0)


