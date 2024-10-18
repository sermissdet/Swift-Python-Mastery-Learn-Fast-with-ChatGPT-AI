
# Encapsulation restricts access to certain details of an object.
# You can implement this using private variables in Python:

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited: {amount}"
        return "Invalid deposit amount."

    def get_balance(self):
        return f"Balance: {self.__balance}"

# Creating an object of BankAccount
account = BankAccount("123456")
print(account.deposit(1000))  # Output: Deposited: 1000
print(account.get_balance())   # Output: Balance: 1000
