class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

    def return_balance(self):
        return self._balance


account = BankAccount(1000)
account.deposit(500)
print(account.return_balance())
account.withdraw(25)
print(account.return_balance())
