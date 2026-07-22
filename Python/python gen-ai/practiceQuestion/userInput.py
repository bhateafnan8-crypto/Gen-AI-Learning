# Question-> 
'''
1. Ask the user for:
Their name
Their birth year

Then print: Hello <name>, you are <age> years old!
'''
# Soltuion-> 
print("---------------------------")
name = input("Enter your name ->>>> ")
age = int(input("Enter your age ->>>> "))
print("---------------------------")
print(f"Hello {name} , you are {age} years old! ")


# Question-> 
'''
2. Ask the user for two numbers and print:
Their sum
Their difference
Their product
'''
# Soltuion-> 
print("---------------------------")

num1 = int(input("Enter num-1 ->>> "))
num2 = int(input("Enter num-2 ->>> "))
print("---------------------------")
print(f"sum {num1+num2}")
print(f"difference {num1-num2}")
print(f"product {num1*num2}")

# Question-> 
'''
3. Ask the user to enter a float number and cast it to integer. Print both values.
'''
# Soltuion-> 
print("---------------------------")
float1 = float(input("Enter float number ->>>"))
print("---------------------------")
print(f"your float {float1} number convert to integer {int(float1)} ")

# Question-> 
'''
4. Ask the user to enter two words and print them in reverse order, separated by a comma.
Example:

Input 1: Hello
Input 2: World
Output: World, Hello
'''
# Soltuion-> 
print("---------------------------")
word1 = input("Enter word 1 ->>>")
word2 = input("Enter word 2 ->>>")
print("---------------------------")
print(f"{word2},{word1}",sep=",")
# Question-> 
'''
5. Challenge: Ask for a number, multiply it by 5, then convert the result to a string and print:
"Your number multiplied by 5 is: <result>"
'''
# Soltuion-> 
print("---------------------------")
num= int(input("Enter any number ->>"))
print("---------------------------")
print(f"your number -> {num} , is multiply  by 5 -> {num*5} , and convert to string -> {str(num)}")