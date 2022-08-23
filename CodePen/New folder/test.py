

class Vehicle:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        
    def car(self):
        print(f"The name of this car is {name} with {color} in color")
        
h = Vehicle("Toyota", "Black")
h.car()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()