# Question-> 
'''
1. Create a list of 5 cities. Then:
Add a new city at the end
Insert one at the 2nd position
Remove the last city and print it
'''
# Soltuion-> 
print("---------------------------")
lst = ["Mumbai","Chennai","Banglore","Nagpur","Nashik"]
print(f"All list content ->> {lst}")
lst.append("Satara")
print(f"After add a city to end in list  ->> {lst}")
lst.insert(2,"Belguim")
print(f"After add a city to 2 position in list  ->> {lst}")
lst.pop()
print(f"After remove a city from end in list  ->> {lst}")



# Question-> 
'''
2. Create a list of numbers: [3, 1, 4, 1, 5, 9]. Then:
Count how many times 1 appears
Sort the list
Reverse the list
'''
# Soltuion-> 
print("---------------------------")
numbers = [3, 1, 4, 1, 5, 9]
print(f"All numbers list content ->> {numbers}")
count1=numbers.count(1)
print(f"count of 1 in numbers list  ->> {count1}")
numbers.sort()
print(f"All numbers list sort content ->> {numbers}")
numbers.reverse()
print(f"All numbers list reverse content ->> {numbers}")


# Question-> 
'''
3. Ask the user to enter 3 favorite foods (one by one), store them in a list, and print the final list.
'''
# Soltuion-> 
print("---------------------------")
foods = []
print(f"your favorite foods list before add all foods -->>> {foods}")
print("---------------------------")
food1= input("Enter your favorite food 1->>")
food2= input("Enter your favorite food 2->>")
food3= input("Enter your favorite food 3->>")
print("---------------------------")
foods.extend([food1,food2,food3])
print(f"your favorite foods listt after add all foods -->>> {foods}")


# Question-> 
'''
4. Create a list of 4 student names and:
Print the list in reverse (using slicing)
Check if "John" is in the list
'''
# Soltuion-> 
print("---------------------------")
students = ["John","Doe","Alice","Herry"]
print(f"All students list ->>> {students}")
students.reverse()
print(f"All students list in reverse using reverse method ->>> {students}")
students[::-1]
print(f"All students list in reverse using slicing  ->>> {students}")
Find_item= "John" in students
print(f"Check is john in students list or not  ->>> {Find_item}")




# Question-> 
'''
5. Challenge:
Create a list of even numbers from 2 to 20 using list repetition or a loop (if already covered).
Store multiple student records in a nested list (e.g., ["Alice", 90])
'''
# Soltuion-> 
print("---------------------------")

evenNumbers = []
print(f"Before append even number list -->> {evenNumbers}")

for i in range(2,21):
    if i % 2 == 0:
        evenNumbers.append(i)

print(f"After append even number list -->> {evenNumbers}")

print("---------------------------")
nestedlist = [["Alice",90],["John",20],["Doe",33]]
print(f"Nested list of student record -->> {nestedlist} ")