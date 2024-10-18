# Abstract classes cannot be instantiated and often include abstract methods that must be implemented by subclasses.
# Here’s how to create an abstract class:

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Creating an object of Rectangle
rectangle = Rectangle(10, 5)
print(f"Area of rectangle: {rectangle.area()}")  # Output: 50
