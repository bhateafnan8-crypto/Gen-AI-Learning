# Question-> 
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


def reverse(char):
   reverse_char = char[::-1]
   print(char,reverse_char)

def uppercase(char):
   uppers = char.upper()

   print(char,uppers)

def word_count(char):
   count = len(char.split())
   print(char,count)
   