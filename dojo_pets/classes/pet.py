
class Pet:
  def __init__(self, name, type, tricks, health=100, energy=100):
    self.name = name
    self.type = type
    self.tricks = tricks
    self.health = health
    self.energy = energy

  def sleep(self):
    print("I can sleep whenever and wherever I wish!")
    print("My energy is up!")
    self.energy += 25
    print(f"My health is now: {self.energy}")
    return self

  def eat(self):
    print("Keep it coming, human, keep it coming!")
    print("My energy is up and I am more healthy now")
    self.energy +=5
    self.health += 10
    print(f"My health is now: {self.health}, and energy: {self.energy}")
    return self
  
  def play(self):
    print("I like to play ball and chase other animals")
    self.health += 5
    self.energy -= 5
    print(f"My health is now: {self.health}, and energy: {self.energy}")
    return self

  def noise(self):
    print("Scream, scream, scream, yell and growl....grrrrhh LOUD")