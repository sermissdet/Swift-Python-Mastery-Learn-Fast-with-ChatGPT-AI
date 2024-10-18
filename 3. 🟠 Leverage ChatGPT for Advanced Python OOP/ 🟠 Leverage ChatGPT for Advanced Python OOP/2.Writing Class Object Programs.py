#Classes are blueprints for creating objects. Below is an example of a simple class that represents a Car.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

# Creating an object of the Car class
my_car = Car("Toyota", "Camry", 2022)
print(my_car.display_info())
