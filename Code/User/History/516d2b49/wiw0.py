class Person:
    def __init__(self, name):
        self.name = name
        
    def greet(self):
        return f"Hello, my name is {self.name}"

def add_farewell(cls):
    def farewell(self):
        return f"Goodbye from {self.name}"
    
    cls.farewell = farewell  # Add the method to the class
    return cls


@add_farewell
class EnhancedPerson:
    def __init__(self, name):
        self.name = name
        
    def greet(self):
        return f"Hello, my name is {self.name}"

person = EnhancedPerson("Alice")
print(person.greet())     # Hello, my name is Alice
print(person.farewell())  # Goodbye from Alice


def add_tracking(cls):
    original_greet = cls.greet  # Store the original method

    def tracked_greet(self):
        print(f"greet was called")   # Extra behaviour before
        return original_greet(self)  # Call the original method

    cls.greet = tracked_greet  # Replace the method on the class
    return cls

@add_tracking
class TrackedPerson:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, my name is {self.name}"


person = TrackedPerson("Alice")
print(person.greet())
# greet was called
# Hello, my name is Alice