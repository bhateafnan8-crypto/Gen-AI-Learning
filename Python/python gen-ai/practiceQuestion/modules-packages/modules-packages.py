import os 
import sys
# Question-> 
"""
1. os module use karo:
   - Current directory print karo
   - Ek folder banao "test_folder"
   - Check karo exist karta hai ya nahi
   - Delete karo
"""
# Soltuion-> 
print("---------------------------")
print(os.getcwd())

os.mkdir("test_folder")
print(os.path.exists("test_folder"))

os.rmdir("test_folder")


# Question-> 
"""
2. sys module use karo:
   - Python version print karo
   - Current script ka path print karo
   - sys.argv use karke command line 
     se naam lo aur print karo
"""
# Soltuion-> 
print("---------------------------")

print(sys.version)

print(sys.argv[0])

print(sys.argv[1])

if len(sys.argv) > 1:
    print(f"Hello! {sys.argv[1]}")
else:
    print("There is no arguments provided")

# Question-> 
"""
3. Apna ek module banao "calculator.py" mein:
   add, subtract, multiply, divide functions
   Phir alag file mein import karke use karo
"""
# Soltuion-> 
print("---------------------------")

import calc

calc.add(2,3)
calc.sub(4,2)
calc.mul(2,3)
calc.div(5,2)
calc.div(5,0)
# calc.div(5,"b")

"""
1. os module use karke:
   - "projects" folder banao
   - Usme "project1.txt" file banao (open/write se)
   - os.listdir() se folder ka content print karo
   - File aur folder dono delete karo

2. sys.argv use karke ek calculator banao:
   Terminal se 3 arguments lo — num1, operator, num2
   python calc.py 10 + 5  → Output: 15
   python calc.py 10 / 0  → ZeroDivisionError handle karo

3. Apna package banao:
   myutils/
     __init__.py
     string_ops.py  → reverse(), uppercase(), word_count()
     number_ops.py  → is_even(), factorial(), is_prime()
   Main file mein import karke use karo

4. os.path use karke:
   - Ek file ka full path nikalo
   - File ka extension nikalo (.txt, .py etc.)
   - File size nikalo bytes mein
   - Check karo file hai ya directory

5. Ek "config.py" module banao jisme 
   sirf constants hon:
   DB_NAME = "myapp.db"
   MAX_RETRIES = 3
   DEBUG = True
   Phir main file mein import karke use karo
   aur ek function banao jo config print kare
"""


# modules-packages
# modules-packages.py