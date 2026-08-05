# Question-> 

"""
1. Create a class Employee with attributes name and salary. Create a subclass Manager that adds department and overrides a method get_details().
"""
# Soltuion-> 
print("---------------------------")

class Employee:
    # constructor
    def __init__(self):
        self.name = "adfar"
        self.salary = 20000

class Manager(Employee):
    # constructor
    def __init__(self):
        super().__init__()
        self.department = "IT department"

    def get_details(self):
        return f"department => {self.department} || name => {self.name} || salary => {self.salary}"

safdar = Manager()

print(f"safdar details => ({safdar.get_details()})")
    
    