"""
Test Code1:
account = Account(1234, "George", 1000)
print(account.credit(500))
print(account.debit(1500))
print(account.info())

output1
1500
0
User George with account 1234 has 0 balance

TestCode2:
account = Account(5411256, "Peter")
print(account.debit(500))
print(account.credit(1000))
print(account.debit(500))
print(account.info())

output2
Amount exceeded balance
1000
500
User Peter with account 5411256 has 500 balance



"""

class Account:

    def __init__(self, id, name, balance = 0):
        self.id = id
        self.name = name
        self.balance = balance

    def credit(self, amount):
        self.balance += amount
        return self.balance

    def debit(self, amount):

        if amount > self.balance:
            return f'Amount exceeded balance'
        self.balance -= amount
        return self.balance

    def info(self):
        return f"User {self.name} with account {self.id} has {self.balance} balance"

account = Account(1234, "George", 1000)
print(account.credit(500))
print(account.debit(1500))
print(account.info())
