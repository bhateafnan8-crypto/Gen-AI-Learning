import os

# Current directory
print(os.getcwd())  # C:\Users\Afnan\projects

# Folder banana
os.mkdir("test_folder")

# Exist check
print(os.path.exists("test_folder"))  # True

# File list karo
print(os.listdir("."))  # current folder ki files

# Folder delete
os.rmdir("test_folder")

# Path join — OS-independent
path = os.path.join("folder", "subfolder", "file.txt")
print(path)  # folder\subfolder\file.txt (Windows pe)

# Environment variable
print(os.environ.get("PATH"))



#  sys 
import sys

# Python version
print(sys.version)  # 3.12.1 ...

# Script path
print(sys.argv[0])  # current file ka path

# Command line arguments
# Terminal mein: python main.py Afnan
print(sys.argv[1])  # "Afnan"

# Python executable path
print(sys.executable)

# Installed modules path
print(sys.path)

# Program band karna
sys.exit("Kuch error aaya")








# modules-packages-concepts.py