#Python supports object-oriented programming (OOP) with classes and objects.

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"


dog1 = Dog("Buddy", 3)
print(dog1.bark())
