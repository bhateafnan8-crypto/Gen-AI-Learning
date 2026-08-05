# Question-> 
"""
1. Create a Car class with private attribute __speed. Add methods to accelerate(), brake(), and get_speed().
"""
# Soltuion-> 
print("---------------------------")
class Car:
    # instance method - constuctor
    def __init__(self):
        self.__speed = 80

    def get_speed(self):
        return f"{self.__speed} kph"

    def brake(self):
        self.__speed = 0
        return f"{self.__speed} kph"

    def  accelerate(self):
        self.__speed += 20
        return f"{self.__speed} kph"

Bugatti = Car()
print(f"speed => {Bugatti.get_speed()} || accelerate speed => {Bugatti.accelerate()} || brake speed => {Bugatti.brake()}")



# Question-> 
"""
2. Modify the Student class from the previous project to make marks private and accessible via get_marks().
"""
# Soltuion-> 
print("---------------------------")
class Student:
    # instance method - constuctor
    def __init__(self):
        self.__marks = 80

    def get_marks(self):
        return self.__marks

adfar = Student()
print(f"marks => {adfar.get_marks()}")




# Question-> 
"""
3. What will happen if you try to access a private variable directly? Try it in your code.
"""
# Soltuion-> 
print("---------------------------")
try:
    print(f"access of Student class private variable outside => {adfar.__marks} ")
except AttributeError:
    print(f"you can't access private variable of the class outside of the class")


# Reason and error of private variable access
"""
Traceback (most recent call last):
  File "D:\Gen Ai\python\python gen-ai\practiceQuestion\oops\encapsulate.py", line 55, in <module>
    print(f"access of Student class private variable outside => {adfar.__marks} ")
                                                                 ^^^^^^^^^^^^^
AttributeError: 'Student' object has no attribute '__marks'. Did you mean: 'get_marks'?
"""
