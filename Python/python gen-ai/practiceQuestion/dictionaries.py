# Question-> 
'''
1. Create a dictionary called employee with the following keys:
name, id, position, salary
Print each key-value pair using a loop
'''
# Soltuion-> 
print("---------------------------")
dict = {"name":"Alice","id":1,"position":"HR","salary":24000}
print(f"all items in dict -->> {dict}")
for k,v in dict.items():
    print(f"key : value via loop ->> {k} : {v}")




# Question-> 
'''
2. Write a program to store marks of 3 subjects in a dictionary. Then:
Add the total and average as new keys
Print the updated dictionary
'''
# Soltuion-> 
print("---------------------------")
marks = {"Math":20,"Science":33,"English":40}
print(f"all subjects marks ->> {marks}")
marksvalue = marks.values()
print(f"marksvalue ->> {marksvalue}")
lenght = len(marks)
print(f"lenght ->> {lenght}")
total = sum(marksvalue)
print(f"sum of marks ->> {total}")
average = total / lenght
print(f"average of marks ->> {average}")
marks.update({"total":total})
marks.update({"average":average})
print(f"after add two new keys and values (total and average) ->> {marks}")


# Question-> 
'''
3. Create a contact book where:
Keys are names
Values are phone numbers
Let user enter a name and fetch phone number using .get() safely
'''
# Soltuion-> 
print("---------------------------")
contactBook = {"Alice":9987773,"John":86666,"Doe":87664664}
print(f"all contactBook details ->> {contactBook}")
nameInp = input("Enter your name -->> ")
print("---------------------------")
getContact = contactBook.get(nameInp,"Not found!")
print(f"Get contact if match otherwise shows(Not found!) ->> {getContact}")



# Question-> 
'''
4. Use a loop to count frequency of each character in a given string using dictionary.
Input: "apple"
Output: {'a': 1, 'p': 2, 'l': 1, 'e': 1}
'''
# Soltuion-> 
print("---------------------------")
fruitInp = input("Enter your fruit -->> ")
print("---------------------------")
print(f"You entered --> {fruitInp}")
frequencyCount = {}
for i in fruitInp:
    frequencyCount[i] = fruitInp.count(i)
print(f"count --> {frequencyCount}")



# Question-> 
'''
5. Bonus Challenge:
Write a program that stores student IDs as keys and nested dictionaries (with name and score) as values. 
Then print all student names who scored above 80.
'''
# Soltuion-> 
print("---------------------------")

studentScore = {"1":{"Name":"Alice","Marks":40},"2":{"Name":"John","Marks":90},"3":{"Name":"Doe","Marks":86},"4":{"Name":"Merry","Marks":76}}
print(f"All student details -->> {studentScore}")

studentItems = studentScore.items()

for key,value in studentItems:
    if value["Marks"] > 80:
        print(f"All students names who scored above 80 ->> {value["Name"]}")
