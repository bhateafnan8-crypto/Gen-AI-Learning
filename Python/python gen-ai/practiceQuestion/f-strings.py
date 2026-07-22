# Question-> 
'''
1. Create a function area_of_circle(radius) that returns the area using π ≈ 3.14 and includes a docstring.
'''
# Soltuion-> 
print("---------------------------")
pie = 3.14
def area_of_circle(r):
    return pie*r*r
print(f"area of circle ->> {area_of_circle(2)}")



# Question-> 
'''
2. Use an f-string to print:
Name: Alice, Age: 25, Score: 89.5%
'''
# Soltuion-> 
print("---------------------------")
Name = "Alice"
Age = 25
Score = 89.5

print(f"Name: {Name}, Age: {Age}, Score: {Score}%")



# Question-> 
'''
3. USing an fstring, write a program that takes two numbers from the user and prints:
Sum of <a> and <b> is <sum>
'''
# Soltuion-> 
print("---------------------------")
num1 = int(input("Enter num1 ->>"))
num2 = int(input("Enter num2 ->>"))
sum = num1 + num2
print("---------------------------")
print(f"Sum of {num1} and {num2} is => {sum}")



# Question-> 
'''
4. Write a function is_even(num) that returns True if number is even. Add a docstring explaining the logic.
'''
# Soltuion-> 
print("---------------------------")
def is_even(num):
    '''
    It will return true if the remainder is 0 while divide by 2
    '''
    if num % 2 == 0:
        return True
print(f"true if even ->> {is_even(2)}")



# Question-> 
'''
5. Challenge: Take name and marks as input and print a report card like(use fstring):
Student Report:
---------------
Name: Rahul
Marks: 86.45%
Grade: B+
'''
# Soltuion-> 
print("---------------------------")
Naam = input("Enter your name ->> ")
Maarks = float(input("Enter your marks ->> "))
grade = input("Enter your grade ->> ")
print("---------------------------")

print(f"Name: {Naam}\nMarks: {Maarks}%\nGrade: {grade}" )


