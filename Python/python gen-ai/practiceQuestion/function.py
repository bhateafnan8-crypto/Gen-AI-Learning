import math
# Question-> 
'''
1. Create a function greet_user(name) that prints:
"Hello, <name>. Welcome to Python!"
'''
# Soltuion-> 
print("---------------------------")
def greet_user(name):
    print(f"Hello, {name}. Welcome to Python!")
greet_user("Alice")

# Question-> 
'''
2. Write a function add(a, b) that returns the sum. Add a default value of b=0.
'''
# Soltuion-> 
print("---------------------------")
def add(a,b=0):
    return a+b
print(f"addition is ->> {add(1,2)}")


# Question-> 
'''
3. Create a function max_of_all(*args) that prints the maximum number from a list of numbers.
'''
# Soltuion-> 
print("---------------------------")
numbers = [1,2,3,4,5]
def max_of_all(*args):
    return max(numbers)
print(f"maximum number in list ->>{max_of_all(numbers)}")

# Question-> 
'''
4. Create a function print_student(**kwargs) that accepts arbitrary student details and prints them.
'''
# Soltuion-> 
print("---------------------------")
def print_student(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")
print_student(name="Alice", age=20, city="Delhi")

# Question-> 
'''
5. Challenge: Write a function calculate(operation, *args) that performs the operation (like 'add', 'multiply') on the numbers passed.
calculate("add", 1, 2, 3)       # 6
calculate("multiply", 2, 3, 4)  # 24
'''
# Soltuion-> 
print("---------------------------")
def calculate(operation, *args):
    if operation == "add":
        return sum(args)
    elif operation == "multiply":
        return math.prod(args)

print(f"sum of numbers ->> {calculate("add", 1, 2, 3) } ")
print(f"prod of numbers ->> {calculate("multiply", 2, 3, 4)}")