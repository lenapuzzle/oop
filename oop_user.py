
class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        return self

    def enroll(self):
        if self.is_rewards_member:
          print('User already a member')
        else:
          self.is_rewards_member = True
          print('Congratulations, you are now enrolled in our rewards program')
        
        self.gold_card_points = 200
        print(f"Your initial rewards' points balance is: {self.gold_card_points}")
        return self

    def spend_points(self, amount):
        updated_points = self.gold_card_points - amount
        if amount > self.gold_card_points:
          print(f'Sorry, that exceeds your points balance')
        else:
          print(f'Congrats on your purchases! Your updated points balance is: {updated_points}')
        return self

user_helen = User('Helen', 'Miller', 'helen@gmail.com', 32)
user_helen.display_info().enroll().spend_points(50)

user_john = User('John', 'White', 'john@yahoo.com', 28)
user_john.display_info().enroll().spend_points(210)
