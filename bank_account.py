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


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(interest_rate=0.01, balance=0)

    def make_deposit(self, amount):
      self.account.deposit(amount)
      return self

    def make_withdrawal(self, amount):
      self.account.withdraw(amount)
      return self

    def display_user_balance(self):
      print(f"Your current account balance is: {self.account.balance}")
      return self
    
    # def transfer_money(self, amount, user_john):
    #   self.account.balance -= amount
    #   user_john += amount
    #   return self
    #   transfer_money(100, 'John White')
    

user_helen = User('Helen Miller', 'helen@gmail.com')
user_helen.make_deposit(300).make_withdrawal(100).display_user_balance()

user_john = User('John White', 'john@yahoo.com')
user_john.make_deposit(500).make_withdrawal(240).display_user_balance()