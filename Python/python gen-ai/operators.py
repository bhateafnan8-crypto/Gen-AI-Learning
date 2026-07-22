# Question-> 
'''
1. Take two numbers as input and print:
Their sum, difference, product, division, and remainder.
'''
# Soltuion-> 

num1 = int(input("Enter first number->>"))
num2 = int(input("Enter second number->>"))

print("addtion->>",num1+num2)
print("difference->>",num1-num2)
print("product->>",num1*num2)
print("division->>",num1/num2)
print("remainder->>",num1%num2)


# Question-> 
'''
2. Ask the user for their age and check:
Are they 18 or older? Print True or False.
'''
# Soltuion-> 
print("---------------------------")
age = int(input("Enter your age->>"))
if age == 18:
    print("you are 18 years old")
else:
    print("you are older than 18 years ")


# Question-> 
'''
3. Ask the user to enter their math and science marks (out of 100). If both are greater than 40, print “Pass”, else “Fail”.
'''
# Soltuion-> 
print("---------------------------")
mathMarks = int(input("Enter your math marks->>"))
scienceMarks = int(input("Enter your science marks->>"))
if mathMarks > 40 and scienceMarks > 40:
    print("Pass!")
else:
    print("Fail!")

# Question-> 
'''
4. Check the result of:

x = 7
print(x > 5 and x < 10)
print(x > 10 or x < 5)
print(not(x > 5))
'''
# Soltuion-> 
print("---------------------------")
x = 7
print(x > 5 and x < 10) #True
print(x > 10 or x < 5) #False
print(not(x > 5)) #False

# Question-> 
'''
5. Challenge: Ask for two numbers and print True if the first number is divisible by the second and greater than it.
'''
# Soltuion-> 
print("---------------------------")
n1 = int(input("Enter first number->>"))
n2 = int(input("Enter second number->>"))

if(n1/n2) and (n1>n2):
    print("True")
else:
    print(False)