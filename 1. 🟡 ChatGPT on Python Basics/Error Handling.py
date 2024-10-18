#Python handles errors using try-except blocks.

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
