#!/usr/bin/python3

# abstract parent/base class
class AnimalActions:
    def quack(self): return self.strings['quack']
    def feathers(self): return self.strings['feathers']
    def bark(self): return self.strings['bark']
    def fur(self): return self.strings['fur']

class Duck(AnimalActions):
    strings = dict(
        quack = "Quaaaaak!",
        feathers = "The duck has gray and white feathers.",
        bark = "The duck cannot bark.",
        fur = "The duck has no fur."
    )
 
class Person(AnimalActions):
    strings = dict(
        quack = "The person imitates a duck.",
        feathers = "The person takes a feather from the ground and shows it.",
        bark = "The person says woof!",
        fur = "The person puts on a fur coat."
    )

class Dog(AnimalActions):
    strings = dict(
        quack = "The dog cannot quack.",
        feathers = "The dog has no feathers.",
        bark = "Arf!",
        fur = "The dog has white fur with black spots."
    )

def in_the_doghouse(dog):
    print(dog.bark())
    print(dog.fur())

def in_the_forest(duck):
    print(duck.quack())
    print(duck.feathers())

# main method 
def main():
    donald = Duck()
    john = Person()
    fido = Dog()

    # Polymorphism & Inheritance
    # even tho in_the_forest takes a duck object,
    # it can also accept a person or dog b/c they
    # all inherit from Animal Actions 
    print("- In the forest:")   
    for o in ( donald, john, fido ):
        in_the_forest(o)

    # even tho in_the_doghouse takes a dog object,
    # it can also accept a person or duck b/c they
    # all inherit from Animal Actions 
    print("- In the doghouse:")
    for o in ( donald, john, fido ):
        in_the_doghouse(o)

 
if __name__ == "__main__": main()
