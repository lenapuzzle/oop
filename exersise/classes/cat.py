from classes.animal import Animal

class Cat(Animal):
    list_of_cats = []

    def __init__(self, name, owner, breed, age):
        super().__init__(name, owner)
        self.breed = breed
        self.age = age
        Cat.list_of_cats.append(self)

    def walk_animal(self):
        print("I don't need to pet a human...")

    def print_info(self):
        super().print_info()
        print(f"Age: {self.age}")

    @classmethod
    def print_all_cats(cls):
        for cat in cls.list_of_cats:
            cat.print_info()
