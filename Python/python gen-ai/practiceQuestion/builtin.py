import random
import math
from datetime import datetime , timedelta , time ,  date

# Question-> 
"""
1. Random Password Generator
Write a program to generate a random 8-character password using random.choice() from letters, digits, and symbols.
"""
# Soltuion-> 
print("---------------------------")

# print(f"random Choice => {random.choice(["a","b","c","d"],[1,2,3,4],["#","!","@","$"])}")
string = ["a","b","c","d"]
digit = ["1","2","3","4"]
specialChar =["#","!","@","$"]

randoms = string + digit + specialChar
passwords = "".join(random.choice(randoms) for _ in range(8))
print(f"random choice => { passwords }")


# Question-> 
"""
2. Math Practice Quiz
Create a program that generates two random numbers and asks the user to add/multiply them. Use random and math.
"""
# Soltuion-> 
print("---------------------------")

try:
    a = random.randint(1,10)
    b = random.randint(1,10)
    print("Enter exit to quit!!")
    while True:
        userInput = input("Enter operation (add/multiply) =>")
        if userInput == "exit":
            break 
        if userInput == "add":
            print(f"addition of {a} and {b} random (a,b) => { a + b}")
        elif userInput == "multiply":
            print(f"multiplication {a} and {b} random (a,b) => { a * b}")
        else:
            print("Choose from only (add/multiply)")
except ValueError:
    print("value should be integer or digit only!!")
finally:
    print("Program Succesfully run! => using simple logic")

print("---------------------------")
print("---------------------------")
print("---------------------------")

try:
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    print("Enter exit to quit!!")
    while True:
        userInput = input("Enter operation (add/multiply) =>")
        if userInput == "exit":
            break 
        if userInput == "add":
            print(f"addition of {num1} and {num2} random (a,b) => {sum([num1,num2])}")
        elif userInput == "multiply":
            print(f"multiplication {num1} and {num2} random (a,b) => {math.prod([num1,num2])}")
        else:
            print("Choose from only (add/multiply)")
except ValueError:
    print("value should be integer or digit only!!")
finally:
    print("Program Succesfully run! => using simple logic")


# Question-> 
"""
3. Time Calculator
Take current time and print the time after 5 hours and 30 minutes using datetime and timedelta.
"""
# Soltuion-> 
print("---------------------------")

current_time = datetime.now()
formatted = current_time.strftime("%d/%m/%Y %I:%M %p")
print(f"\ncurrent time => {current_time}\n")
print(f"\nfromatted time => {formatted}\n")

after_5H_30M = current_time + timedelta(hours= 5 ,minutes= 30);
formatted_timedelta = after_5H_30M.strftime("%d/%m/%Y %I:%M %p")


print(f"\ntime after 5 hours and 30 minutes => {after_5H_30M}\n")
print(f"\ntime after 5 hours and 30 minutes fromatted => {formatted_timedelta}\n")
