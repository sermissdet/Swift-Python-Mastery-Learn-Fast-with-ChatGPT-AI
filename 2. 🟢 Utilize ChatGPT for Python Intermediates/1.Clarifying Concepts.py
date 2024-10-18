#If you encounter a Python concept that’s unclear, ask ChatGPT for explanations.
# You can request simple definitions, practical examples, or even analogies.
#Ask ChatGPT: “Can you explain how decorators work in Python?”
#Example: Understanding Decorators

def decorator_function(original_function):
    def wrapper_function():
        print("Wrapper executed before {}".format(original_function.__name__))
        return original_function()
    return wrapper_function

@decorator_function
def display():
    return "Display function executed"

print(display())
