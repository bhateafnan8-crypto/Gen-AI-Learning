# Question-> 
"""
1. Create a Person class with name, Student and Teacher classes that inherit it (hierarchical).
"""
# Soltuion-> 
print("---------------------------")

#Base class
class Person:
    # instance attributes - constructor --
    def __init__(self,name = "Adfar"):
        self.name = name

# child class - 1
class Student(Person):
    # instance attributes - constructor --
    def getName(self):
        return self.name

# child class - 2
class Teacher(Person):
    # instance attributes - constructor --
    def getName(self):
        return self.name

c1,c2 = Student(),Teacher()

print(f"Student inherit name from person => {c1.getName()} || Teacher inherit name from person => {c2.getName()} ")




# Question-> 
"""
2. Create a Device → Phone → Smartphone chain using multilevel inheritance.
"""
# Soltuion-> 
print("---------------------------")

#Base class 
class Device:
    #instance attribute - constructor
    def __init__(self,name = "SamSung"):
        self.name = name

class Phone(Device):
    #instance attribute - constructor
    def __init__(self,modal = "Button-phone"):
        super().__init__()
        self.modal = modal

class Smartphone(Phone):
    #instance attribute - constructor
    def __init__(self,invenstion = "ScreenTouch-phone"):
        super().__init__()
        self.invenstion = invenstion

    def getDetail(self):
        return f"Device name => {self.name} || Modal => {self.modal} || Invention to => {self.invenstion}"

d1 = Smartphone()

print(f"SmartPhone invention from device => ( {d1.getDetail()} )")