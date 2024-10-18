
#Polymorphism allows methods to perform different tasks based on the object calling them. Here’s an example:

class Bird:
    def sound(self):
        return "Chirp!"

class Dog:
    def sound(self):
        return "Bark!"

def animal_sound(animal):
    print(animal.sound())

# Creating objects
bird = Bird()
dog = Dog()

# Demonstrating polymorphism
animal_sound(bird)  # Output: Chirp!
animal_sound(dog)   # Output: Bark!
