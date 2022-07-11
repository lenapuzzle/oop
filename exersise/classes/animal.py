
class Animal:
    def __init__(self, name, owner, breed):
        self.name = name
        self.owner = owner
        self.breed = breed

    def print_info(self):
        print(f'Name of an animal: {self.name}')
        print(f'Owner: {self.owner}')
        print(f'Breed: {self.breed}')

        # Polymorphism - leaves it to child classes to implement their own methods
    def walk_animal(self):
        raise NotImplementedError
