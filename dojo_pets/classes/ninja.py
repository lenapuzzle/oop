from classes.pet import Pet

class Ninja:
  def __init__(self, first_name, last_name, pet, treats, pet_food):
    self.first_name = first_name
    self.last_name = last_name
    self.pet = pet
    self.treats = treats
    self.pet_food = pet_food

  def walk_pet(self):
    print("I am your pet and I need to be walked outside regularly!")
    # Pet.play(self)
    return self
  
  def feed_pet(self):
    print("I am constantly hungry, so feed my at least from time to time...")
    # Pet.eat(self)
    return self

  def bathe_pet(self):
    print("What bath? You can take your bath, human")
    # Pet.noise(self)
    return self