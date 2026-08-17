# Question-> 
"""
1. Write a program that opens a file and reads its content. Use try-except-finally to handle FileNotFoundError.
"""
# Soltuion-> 
print("---------------------------")
try:
    file = open("abc.py","r")
    read = file.read()
    print(f"read content= : {read}")
except FileNotFoundError:
    print(f"File not found!")
finally:
    print("try-catch-finall => finaly block here")





# Question-> 
"""
2. Ask the user for a positive number. Raise a ValueError if the input is zero or negative.
"""
# Soltuion-> 
print("---------------------------")

try:
    nums = int(input("Enter positive number => "))
    if nums <= 0:
        raise ValueError("number should be positive neither zero nor negative")
    print(f"Positive Number =>  {nums}")
except ValueError as e:
    print(f"Error => {e}")





# Question-> 
"""
3. Create a custom exception OutOfRangeError and raise it if a number is not between 1 and 100.
"""
# Soltuion-> 
print("---------------------------")
class OutOfRangeError(Exception):
    pass
try:
    nume = int(input("Enter number => "))
    if nume < 1 or nume > 100 :
        raise OutOfRangeError(f"{nume} is out of range => {nume} number should be in in between  1-100")
    print(f"number in between 1-100 => {nume}")
except OutOfRangeError as e:
    print(f"Error => {e}")





# Question-> 
"""
4. Write a program that divides two numbers. Catch and handle ZeroDivisionError and ValueError. Use finally to print "Done."
"""
# Soltuion-> 
print("---------------------------")
try:
    divider = int(input("Enter number for divider =>"))
    result = 10 / divider
    print(f"result => {int(result)}")
except ZeroDivisionError:
    print(f" divider  cannot be zero ")
except ValueError:
    print(f"divider should be only integer => Invalid input")
finally:
    print("Done!!!")

# Question-> 
"""
5. Modify the password validation example to raise a custom exception if:
The password is < 6 characters
It doesn't contain a digit

(Hint: Create a WeakPasswordError class.)
"""
# Soltuion-> 
print("---------------------------")
class WeakPasswordError(Exception):
    pass

try:
    password = input("Enter your password only char no digit => ")
    if len(password) < 6 or not any(ch.isdigit() for ch in password):
        raise WeakPasswordError(f"your password : {password} is weak =>  password should be > 6 and not only charecter , required with digit")
    print(f"your password set successfully check => {password}")
except WeakPasswordError as e:
    print(F"Error => {e}")