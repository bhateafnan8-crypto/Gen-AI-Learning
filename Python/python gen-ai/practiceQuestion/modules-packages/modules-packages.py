import os 
import sys
# # Question-> 
# """
# 1. os module use karo:
#    - Current directory print karo
#    - Ek folder banao "test_folder"
#    - Check karo exist karta hai ya nahi
#    - Delete karo
# """
# # Soltuion-> 
# print("---------------------------")
# print(os.getcwd())

# os.mkdir("test_folder")
# print(os.path.exists("test_folder"))

# os.rmdir("test_folder")


# # Question-> 
# """
# 2. sys module use karo:
#    - Python version print karo
#    - Current script ka path print karo
#    - sys.argv use karke command line 
#      se naam lo aur print karo
# """
# # Soltuion-> 
# print("---------------------------")

# print(sys.version)

# print(sys.argv[0])

# print(sys.argv[1])

# if len(sys.argv) > 1:
#     print(f"Hello! {sys.argv[1]}")
# else:
#     print("There is no arguments provided")

# # Question-> 
# """
# 3. Apna ek module banao "calculator.py" mein:
#    add, subtract, multiply, divide functions
#    Phir alag file mein import karke use karo
# """
# # Soltuion-> 
# print("---------------------------")

# import calc

# calc.add(2,3)
# calc.sub(4,2)
# calc.mul(2,3)
# calc.div(5,2)
# calc.div(5,0)
# # calc.div(5,"b")


# Question-> 
"""
4. os module use karke:
   - "projects" folder banao
   - Usme "project1.txt" file banao (open/write se)
   - os.listdir() se folder ka content print karo
   - File aur folder dono delete karo
"""
# Soltuion-> 
print("---------------------------")
print("\n sol 1 \n")
os.mkdir("projects")
os.mkdir("projects1")

file_path = os.path.join("projects","project1.txt")
with open(file_path,"w") as f:
    f.write("Hello")


print("\n sol 2 \n")

with open("projects/project2.txt","w") as f:
    f.write("Hello")

print(os.listdir("projects"))

# os.remove("project1.txt")
os.remove("projects/project1.txt")
os.remove("projects/project2.txt")
os.rmdir("projects")
os.rmdir("projects1")


# Question-> 
"""
5. sys.argv use karke ek calculator banao:
   Terminal se 3 arguments lo — num1, operator, num2
   python calc.py 10 + 5  → Output: 15
   python calc.py 10 / 0  → ZeroDivisionError handle karo
"""
# Soltuion-> 
print("---------------------------")

try:
   n1 =  sys.argv[1]
   op =  sys.argv[2]
   n2 = sys.argv[3]

   if op == "+":
      print(int(n1) + int(n2))
   elif op == "-":
      print(int(n1) - int(n2))
   elif op == "*":
      print(int(n1) * int(n2))
   elif op == "/":
      try :
         print(int(n1) / int(n2))
      except ZeroDivisionError:
         print("Divider should not be zero")
except IndexError:
   print("All values required")


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

from myutils import string_ops as s
from myutils import number_ops as n

s.uppercase("hello")
s.reverse("hello")
s.word_count("hello world")

print(n.factorial(5))
print(n.is_even(5))
print(n.is_prime(5))


# Question-> 
"""
7. os.path use karke:
   - Ek file ka full path nikalo
   - File ka extension nikalo (.txt, .py etc.)
   - File size nikalo bytes mein
   - Check karo file hai ya directory
"""
# Soltuion-> 
print("---------------------------")



# Question-> 
"""
8. Ek "config.py" module banao jisme 
   sirf constants hon:
   DB_NAME = "myapp.db"
   MAX_RETRIES = 3
   DEBUG = True
   Phir main file mein import karke use karo
   aur ek function banao jo config print kare
"""
# Soltuion-> 
print("---------------------------")


#  idhar sahi hai lekin jo file creation hai na usme jo projects / project1.txt hona chahiye .. mene direct kiya is liye wo current me chala gaya.. ya to jo join wala hai na usko ek var me save karke usko hi sidha create karna hai..

# os.mkdir("projects")

# with open("project1.txt","w") as f:
#     f.write("Hello")

# print(os.path.join("projects","project1.txt"))

#  yaha per bas shayd wo if else me problem hai.. len se karna tha direct kiya .. required bhi nahi tha try - except handle karlega



# try:
#    n1 =  sys.argv[1]
#    op =  sys.argv[2]
#    n2 = sys.argv[3]

#    if len(n1) > 1 and len(n2) > 1:
#       if op == "+":
#          print(int(n1) + int(n2))
#       elif op == "-":
#          print(int(n1) - int(n2))
#       elif op == "*":
#          print(int(n1) * int(n2))
#       elif op == "/":
#          try :
#             print(int(n1) / int(n2))
#          except ZeroDivisionError:
#             print("Divider should not be zero")
#    else:
#       print("n1 , n2 and  op not provided ")
# except IndexError:
#    print("All values required")


# modules-packages
# modules-packages.py