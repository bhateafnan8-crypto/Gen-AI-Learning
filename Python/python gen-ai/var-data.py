# Question-> 
'''
1. Create variables to store your:

Name
Age
Favorite programming language
Whether you're a student (True/False)

Print each of them with appropriate labels using f-strings.
----------------------------------------------------------------
'''
# Soltuion-> 
Name = "Allice"
Age = 20
Language = "Python"
Student = True

print(f" Welcome {Name} You're {Age} years old and your favourite laguage is {Language} ")
if True:
    print("you're a student")


# Question-> 
'''
2. Predict the output and data types:

x = 10
y = 3.14
z = x + y
print(z)
print(type(z))
----------------------------------------------------------------
'''
# Soltuion-> 
print("---------------------------")
x = 10
y = 3.14
z = x + y
print(z) #13.14
print(type(z)) #float


# Question-> 
'''
3. Create a variable with a value "123" and check if it’s a number or string. Then convert it to an integer and add 10.
'''
# Soltuion-> 
print("---------------------------")
num = "123"
if type(num) == str :
    print("convert to int and add 10 ->>>",int(num)+10)


# Question-> 
'''
4. Try creating invalid variable names like 2name, class, or my-name and note what errors Python gives you.
----------------------------------------------------------------
'''
# Soltuion-> 
print("---------------------------")

invalid = "2name class my-name "
print("Invalid variable-name->>>",invalid) #SyntaxError: invalid decimal literal

# Question-> 
'''
5. Advanced: Can a variable store multiple data types during execution?

x = 10
print(type(x))

x = "Now I am a string"
print(type(x))
----------------------------------------------------------------
'''
# Soltuion-> 
print("---------------------------")
#yes but in different location
x = 10
print(id(type(x))) #integer 

x = "Now I am a string"
print(id(type(x))) #string 