#Inheritance allows one class to inherit attributes and methods from another class.
# Here’s how to implement it:

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def honk(self):
        return "Honk!"

class Car(Vehicle):  # Inheriting from Vehicle
    def __init__(self, brand, model):
        super().__init__(brand)  # Call the parent class constructor
        self.model = model

    def display(self):
        return f"{self.brand} {self.model}"

# Creating an object of the Car class
my_car = Car("Honda", "Civic")
print(my_car.honk())  # Inherited method
print(my_car.display())
