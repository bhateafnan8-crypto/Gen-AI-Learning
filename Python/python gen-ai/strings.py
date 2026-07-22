# Question-> 
'''
1. Given a string "machinelearning", print:
First 5 characters
Last 3 characters
The string in reverse
'''
# Soltuion-> 
print("---------------------------")
word = "machinelearning";
print(f"First 5 characters -> {word[0:5]}")
print(f"Last 3 characters -> {word[-3:]}")
print(f"The string in reverse -> {word[::-1]}")



# Question-> 
'''
2. Ask the user to enter their full name. Then:
Print it in uppercase
Print only the first name (assume it's before the first space)
Count how many times the letter 'a' appears
'''
# Soltuion-> 
print("---------------------------")
fullname =input("Enter your full name ->>> ")
print("---------------------------")
print(f"fullname ->> {fullname.upper()}")
print(f"first name only (before first space) ->> {fullname.split()[0]}")
print(f"number of a presents in fullname ->> {fullname.count('a')}")


# Question-> 
'''
3. Ask the user for a sentence and print each word in a new line using .split().
'''
# Soltuion-> 
print("---------------------------")
sentence = input("Enter a sentence ->> ")
print("---------------------------")
word = sentence.split()
for i in word:
    print(f"{i}")
print("---------------------------")
print(*word,sep="\n")


# Question-> 
'''
4. Replace all spaces in a sentence with dashes (-).
'''
# Soltuion-> 
print("---------------------------")
print(sentence.replace(" ","-"))

# Question-> 
'''
5. Challenge: Ask the user to enter a filename and check if it ends with .py — if yes, print "Python file detected", else "Not a Python file".
'''
# Soltuion-> 
print("---------------------------")
filename = input("Enter your filename ->> ")
print("---------------------------")
extension = filename.endswith(".py")
if extension :
    print("Python file detected")
else:
    print("Not a Python file")
