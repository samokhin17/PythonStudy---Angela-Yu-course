import pytz
import datetime


WHITE = '\033[00m'
GREEN ='\033[0;92m'
RED ='\033[1;31m'

class Account:
    def __init__(self, name, balance):
        self.history = []
        self.balance = balance
        self.name = name

    @staticmethod
    def _get_current_time():
        return pytz.utc.localize(datetime.datetime.utcnow())

    def deposit(self, amount):
        self.balance += amount
        self.show_balance()
        self.history.append([amount, self._get_current_time()])

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            print(f'You spent {amount} units')
            self.show_balance()
            self.history.append([-amount, self._get_current_time()])
        else:
            print('Not enough money')
            self.show_balance()

    def show_balance(self):
        print(f'Balance: {self.balance}')

    def show_history(self):
        for amount, date in self.history:
            if amount > 0:
                transaction = 'deposited'
                color = GREEN
            else:
                transaction = 'withdrown'
                color = RED
            print(f'{color} {amount} {WHITE} {transaction} on {date.astimezone()}')



a = Account('Sasha', 0)
