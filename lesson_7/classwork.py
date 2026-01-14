# Class
# Dunder methods: double underscore we use those methods to manipulate the objects

# __eq__ for equal
# __add__ for adding classes
# __str__ for printing classes

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sayHello(self):
        print(f"Hello {self.name}")