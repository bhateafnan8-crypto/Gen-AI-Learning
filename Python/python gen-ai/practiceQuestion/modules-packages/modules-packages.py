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




# modules-packages
# modules-packages.py