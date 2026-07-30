# Question-> 
"""
1. Enumerate a List of Cities
cities = ["Delhi", "Mumbai", "Chennai", "Kolkata"]
# Output:
# 0: Delhi
# 1: Mumbai
# ...
"""
# Soltuion-> 
print("---------------------------")
cities = ["Delhi", "Mumbai", "Chennai", "Kolkata"]
for i,v in enumerate(cities):
    print(f"{i}. {v}")



# Question-> 
"""
2. Custom Start Index
Print all items of a list starting index from 101.
"""
# Soltuion-> 
print("---------------------------")
city = ["Delhi", "Mumbai", "Chennai", "Kolkata"]
for i,v in enumerate(city,start=101):
    print(f"{i}. {v}")



# Question-> 
"""
3. Filter List Using Index
Given a list of temperatures, increase values only at even indexes by 2.
"""
# Soltuion-> 
print("---------------------------")
temperatures = [20,30,40,50]

for i,t in enumerate(temperatures,start = 1):
    if i % 2 == 0:
        print(f"{i}. {t}")



# Question-> 
"""
4. Index Matching Characters in a String
Write a program that prints positions of all vowels in a given word.
"""
# Soltuion-> 
print("---------------------------")
word = input("Enter a word to check vowels in word => ")
vowels = ["a","e","i","o","u","A","E","I","O","U"]
print("---------------------------")

for i ,ch in enumerate(word):
    if ch in vowels:
        print(f"vowels with index {ch} =>  {i}")


# Question-> 
"""
5. Replace List Items Based on Position
Replace every item at odd index in a list with "REPLACED".
"""
# Soltuion-> 
print("---------------------------")
city1 = ["Delhi", "Mumbai", "Chennai", "Kolkata"]
print(f"before update =>{city1}")
# replace_city = input("Enter city to replace =>")
replace_city = "REPLACED"

for i , ci in enumerate(city1):
    if i % 2 != 0:
        city1[i] =  replace_city
        
print(f"after update => {city1}")
