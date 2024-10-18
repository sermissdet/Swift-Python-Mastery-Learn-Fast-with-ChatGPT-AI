#Object-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects," which can contain data and code.
# Here's a simple function that explains the main OOP concepts:



def explain_oop_concepts():
    concepts = {
        "Encapsulation": "The bundling of data (attributes) and methods (functions) that operate on the data within a single unit, usually a class. This restricts direct access to some of the object's components.",
        "Inheritance": "The mechanism by which one class can inherit the attributes and methods of another class, promoting code reusability.",
        "Polymorphism": "The ability to present the same interface for different data types. It allows methods to do different things based on the object it is acting upon.",
        "Abstraction": "The concept of hiding the complex implementation details and showing only the essential features of the object. It simplifies the usage of complex systems."
    }
    return concepts

# Usage
for concept, definition in explain_oop_concepts().items():
    print(f"{concept}: {definition}")
