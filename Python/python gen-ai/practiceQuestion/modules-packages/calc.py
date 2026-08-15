# Question-> 
"""
3. Apna ek module banao "calculator.py" mein:
   add, subtract, multiply, divide functions
   Phir alag file mein import karke use karo
"""
# Soltuion-> 
print("---------------------------")

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        print("divided should not be zero")




