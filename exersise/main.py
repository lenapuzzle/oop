
from classes.animal import Animal
from classes.dog import Dog
from classes.cat import Cat

max = Animal("Max", "Alex")
max.print_info()

jagger = Dog("Jagger", "Alfredo", "Husky", 5)
jagger.print_info()
jagger.walk_animal()

chester = Cat("Chester", "Helen", "Brown", 3)
chester.print_info()
chester.walk_animal()

# Input-Output
first_name = input("Your first name:")
print(f"It is nice to meet you {first_name}")

print("0) EXIT this program")
print("1) Add a CAT")
print("2) Add a DOG")
print('3) print all cats')
print('4) print all dogs')
option = input("Select an option: ")

while option != '0':
    if option == '1':
      name = input("Name of your cat: ")
      owner = input("What is your name: ")
      breed = input("What is the breed of your cat: ")
      age = input("What is the age of your cat: ")
      new_cat = Cat(name, owner, breed, age)
    elif option == '2': 
      name = input("Name of your dog: ")
      owner = input("What is your name: ")
      breed = input("What is the breed of your dog: ")
      age = input("What is the age of your dog: ")
      new_dog = Dog(name, owner, breed, age) 
    elif option == '3':
      Cat.print_all_cats
    elif option == '4':
      Dog.print_all_dogs
    print("*****MENU OF OPTIONS*****")
    print("0) EXIT this program")
    print("1) Add a CAT")
    print("1) Add a DOG")
    option = input("Select an option: ")