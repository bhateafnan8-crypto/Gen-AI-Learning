"""
6. Apna package banao:
   myutils/
     __init__.py
     string_ops.py  → reverse(), uppercase(), word_count()
     number_ops.py  → is_even(), factorial(), is_prime()
   Main file mein import karke use karo
"""
# Soltuion-> 
print("---------------------------")

def is_even(num):
    iseven = num % 2 == 0

    if iseven:
       return True
    else:
       return False

def factorial(num):
    if num == 0 or num == 1:
        return 1
    if num < 0:
        return "Number should be positive"
    return num * factorial(num-1) 

def fact2(num):
    facts = 1

    for i in range(2,num+1):
        facts *= i

    return facts

def is_prime(num):
    if num < 2:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True