# Question-> 
"""
1 . [1, 2, 3, 4, 5] se sirf odd numbers ki list banao
"""
# Soltuion-> 
print("---------------------------")

li = [1, 2, 3, 4, 5]

print(f"\n list li => {li}\n")
odd = [i for i in li if i % 2 != 0]

print(f"\nodd from list li => {odd}\n")


# Question-> 
"""
2 . ["apple", "banana", "cherry"] se {word: length} dict banao
"""
# Soltuion-> 
print("---------------------------")

fruits = ["apple", "banana", "cherry"]
print(f"\nfruits list => {fruits}\n")

length = {"word" : len(fruits) }

print(f"\nlength of fruit list => {length}\n")

length = {word : len(word) for word in fruits}

print(f"\nlength of fruit list each and every elements => {length}\n")


# Question-> 
"""
3 . [1, 2, 3, 4, 5] se sirf even numbers ko square karke list banao
"""
# Soltuion-> 
print("---------------------------")

b = [1, 2, 3, 4, 5]

print(f"\n list b => {b}\n")
even_square = [i * i for i in b if i % 2 == 0 ]
print(f"\n even_square list from list b => {even_square}\n")


# Question-> 
"""
4. Ek list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] se sirf 
   un numbers ki list banao jo 3 se divisible hain.
"""
# Soltuion-> 
print("---------------------------")
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"list l1  => {l1}\n")

db3 = [i for i in l1 if i % 3 == 0]

print(f"division by 3 list from list l1 => {db3}\n")


# Question-> 
"""
5. Ek list ["hello", "world", "python", "code"] se 
   har word ko uppercase mein convert karo — list comprehension se.
"""
# Soltuion-> 
print("---------------------------")
l2 = ["hello", "world", "python", "code"]

print(f"\nlist l2 => {l2}\n")

uc = [i.upper() for i in l2]

print(f"\nuppercase list from list l2 => {uc}\n")


# Question-> 
"""
6. Do lists hain:
   keys = ["name", "age", "city"]
   values = ["Afnan", 22, "Mumbai"]
   Inhe combine karke ek dict banao — dict comprehension se.
   (Hint: zip() use karo)
"""
# Soltuion-> 
print("---------------------------")
keys = ["name", "age", "city"]
values = ["Afnan", 22, "Mumbai"]

print(f"\n({keys}):({values})\n")
key_value = {key:value for key, value in zip(keys , values) }

print(f"key:value pair from keys , values list using zip and dict comphrension => {key_value}")


# Question-> 
"""
7. [1, 2, 3, 4, 5] se ek dict banao jahan:
   - key = number
   - value = "even" ya "odd"
   Output: {1: "odd", 2: "even", 3: "odd", 4: "even", 5: "odd"}
"""
# Soltuion-> 
print("---------------------------")
num = [1, 2, 3, 4, 5]

print(f"\n num list => {num}\n")
even_odd = {i:("even" if i % 2 == 0 else "odd" )  for i in num }

print(f"\neven odd list with value (even - odd ) using condition in values section  => {even_odd}\n")


# Question-> 
"""
8. Ek list of dicts hai:
   students = [
     {"name": "Ali", "marks": 45},
     {"name": "Sara", "marks": 32},
     {"name": "Raj", "marks": 78}
   ]
   Sirf un students ke naam ki list banao 
   jinka marks 40 se zyada hai — list comprehension se.
"""
# Soltuion-> 
print("---------------------------")

students = [
   {"name": "Ali", "marks": 45},
   {"name": "Sara", "marks": 32},
   {"name": "Raj", "marks": 78}
]

print(f"\nstudent list of dict => {students} \n")


toppers = [s["name"] for s in students if s["marks"] > 40]

print(f"\ntopper students list => {toppers} ")