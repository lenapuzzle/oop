
class Animal:
  def __init__(self, name, owner):
    self.name = name
    self.owner = owner

    def print_info(self):
      print(f'Name of animal: {self.name}')
      print(f'Owner: {self.owner}')

    # Polymorphism
    def walk_animal(self):
      raise NotImplementedError