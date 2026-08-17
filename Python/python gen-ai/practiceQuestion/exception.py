# Question-> 
"""
1. Write a program that opens a file and reads 
   its content. Use try-except-finally to handle 
   FileNotFoundError.
"""
# Soltuion-> 
print("---------------------------")
import json
try:
    with open("settings.json","r") as f :
        load = json.load(f)

except FileNotFoundError:
    print("File Not Found!")


# Question-> 
"""
2. Ask the user for a positive number. 
   Raise a ValueError if the input is zero or negative.
"""
# Soltuion-> 
print("---------------------------")
print("\n sol 1 custom errors of negative \n")
class NegativeError(Exception):
    pass

try:
    user = int(input("Enter positive number => "))
    if user < 0:
        raise NegativeError("Number should not be negative")
    print(user)

except NegativeError as e:
    print("Error :",e)

print("\n sol 2 VaueError of zero and negative \n")

try:
    user = int(input("Enter positive number => "))
    if user <= 0:
        raise ValueError("Number should not be Zero or  negative")
    print(user)

except ValueError as e:
    print("Error :",e)


# Question-> 
"""
3. Create a custom exception OutOfRangeError and 
   raise it if a number is not between 1 and 100.
"""
# Soltuion-> 
print("---------------------------")

class OutOfRangeError(Exception):
    pass

try:
    num = int(input("Enter number between (1-100) => "))
    if 100 < num or num < 1:
        raise OutOfRangeError("number is out of range (1-100) ",num)
    print(num)
except OutOfRangeError as e:
    print("Error",e)


# Question-> 
"""
4. Write a program that divides two numbers. 
   Catch and handle ZeroDivisionError and ValueError. 
   Use finally to print "Done."
"""
# Soltuion-> 
print("---------------------------")
try:
    n1 = int(input("Enter number 1 => "))
    n2 = int(input("Enter number 2 => "))

    result = n1 / n2

    print(result)
except ValueError:
    print("Numbers should be integer")
except ZeroDivisionError:
    print("number 2 should not be zero")
finally:
    print("Done")


# Question-> 
"""
5. Modify the password validation example to raise 
   a custom exception if:
   - Password is < 6 characters
   - It doesn't contain a digit
   (Hint: Create a WeakPasswordError class.)
"""
# Soltuion-> 
print("---------------------------")

class WeakPasswordError(Exception):
    pass

try:
    passwords = input("Enter password (min -6) only char => ")

    if len(passwords) < 6 or not any(char.isdigit() for char in passwords):
        raise WeakPasswordError(f"Password {passwords} is weak becuase not contains digit and len is less than 6")
    print(passwords)

except WeakPasswordError as e:
    print("Error",e)
