# Question-> 
'''
1. Write a program that:
Asks the user to enter two numbers
Adds and multiplies them
Prints both results
'''
# Soltuion-> 
print("---------------------------")
num1 = int(input("Enter num1 ->>"))
num2 = int(input("Enter num2 ->>"))
print("---------------------------")

print(f"sum of {num1} and {num2} => {num1+num2}")
print(f"multiplies of {num1} and {num2} => {num1*num2}")


# Question-> 
'''
2. Introduce an error:
Try adding a string and an integer
Fix it using typecasting
'''
# Soltuion-> 
print("---------------------------")
text = input("Enter number text ->>")
num = int(input("Enter number  ->>"))
print("---------------------------")
print(f"typeCasting -> {int(text) + num}")


# Question-> 
'''
3. Create a program that:
Asks for name and age
Prints: Hi <name>, you will be 100 years old in the year <calculated_year>
'''
# Soltuion-> 
print("---------------------------")
name = input("Enter your name ->>")
age = int(input("Enter your age ->>"))
print("---------------------------")
print(f"Hi {name}, you will be 100 years old in the year {2026 + ( 100 - age)}")



# Question-> 
'''
4. Write a buggy program that crashes, then fix it:

--python code:--
# Bug: input not converted to int
age = input("Enter your age: ")
years_left = 100 - age
print("Years left to turn 100:", years_left)
--python code:--
'''
# Soltuion-> 
print("---------------------------")
age = int(input("Enter your age: "))
years_left = 100 - age
print("---------------------------")
print("Years left to turn 100:", years_left)

