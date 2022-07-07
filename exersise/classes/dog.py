from classes.animal import Animal

class Dog(Animal):
  list_of_dogs = []
  def __init__(self, name, owner, breed, color):
    super().__init__(name, owner)
    self.breed = breed
    self.color = color
    Dog.list_of_dogs.append(self)

    def print_info(self):
      super().print_info()
      print(f"Breed: {self.breed}")
      print(f"Color: {self.color}")

    def walk_animal(self):
      print("I'm a dog so I need to be walked at least 2 times a day!")

    @classmethod
    def print_all_dogs(cls):
      for dog in cls.list_of_dogs:
        dog.print_info()