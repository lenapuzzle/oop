from classes.animal import Animal
from classes.dog import Dog
from classes.cat import Cat

# an instance of an Animal instantiation
max = Animal("Max", "Alex", "Labrador")
max.print_info()

# an instance of a Dog instantiation
jagger = Dog("Jagger", "Alfredo", "Golden Retriever", "Golden")
jagger.print_info()
jagger.walk_animal()

monster = Dog("Monster", "Jasper", "Husky", "White")
monster.print_info()
monster.walk_animal()

# an instance of a Cat instantiation
ozzy = Cat("Ozzy", "Helen", "Tabby", 3)
ozzy.print_info()
ozzy.walk_animal()

fluffy = Cat("Fluffy", "John", "Siberian", 2)
fluffy.print_info()
fluffy.walk_animal()

# Input-Output
first_name = input("Please, give me your first name:")
print(f"It is nice to meet you {first_name}")

print("*****MENU OF OPTIONS*****")
print("0) EXIT this program")
print("1) Add a CAT")
print("2) Add a DOG")
print('3) Print all cats')
print('4) Print all dogs')
option = input("Select an option: ")

while option != '0':
    if option == '1':
        name = input("Name of a cat: ")
        owner = input("What is your name: ")
        breed = input("What is the breed of a cat: ")
        age = input("What is the age of a cat: ")
        new_cat = Cat(name, owner, breed, age)
    elif option == '2':
        name = input("Name of a dog: ")
        owner = input("What is your name: ")
        breed = input("What is the breed of a dog: ")
        color = input("What is the color of a dog: ")
        new_dog = Dog(name, owner, breed, color)
    elif option == '3':
        Cat.print_all_cats()
    elif option == '4':
        Dog.print_all_dogs()
    print("*****MENU OF OPTIONS*****")
    print("0) EXIT this program")
    print("1) Add a CAT")
    print("2) Add a DOG")
    print('3) Print all cats')
    print('4) Print all dogs')
    option = input("Select an option: ")

