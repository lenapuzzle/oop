class BankAccount:

    all_accounts = []  # Ninja Bonus

    def __init__(self, balance = 0, interest_rate = 0.01):
        self.interest_rate = interest_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance - amount > 0:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Your account balance is: {self.balance}")
        print(f"Current interest rate is: {self.interest_rate}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.interest_rate
        else:
            print("N/A, you have a negative balance")
        return self

    @classmethod  # Ninja Bonus
    def print_accounts(cls):
        for i in cls.all_accounts:
          print(i.display_account_info())

bank_account_one = BankAccount(100, 0.03)
bank_account_two = BankAccount(100, 0.02)

BankAccount.print_accounts()

bank_account_one.deposit(300).deposit(100).deposit(
    400).withdraw(500).yield_interest().display_account_info()

bank_account_two.deposit(500).deposit(800).withdraw(300).withdraw(
    500).withdraw(300).withdraw(100).yield_interest().display_account_info()
