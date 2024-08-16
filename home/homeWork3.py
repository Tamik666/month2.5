class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def __str__(self):
        return (f"Name: {self._name}\n"
                f"Balance: {self._balance}")

    def moneyX(self):
        amount = int(input("Enter top-up value: "))
        self._balance += amount

    def _kill(self):
        self._balance = 0

    def __jackpot(self):
        self._balance *= 10

    def merge(self, other):
        self._balance += other._balance
        other._balance = 0


account = Bank("Sam", 0)
account2 = Bank("Alex", 0)
# account2.moneyX()
# account.moneyX()
# account.merge(account2)
# account._Bank__jackpot()
# account._kill()


print(account)
