# Question-> 
'''
1. Create a tuple of 5 numbers and print:
First and last element
Middle 3 elements using slicing
'''
# Soltuion-> 
print("---------------------------")
numbers = (2,3,4,5,6)
print(f"All numbers tuple content -> {numbers}")
firstelement = numbers[0] 
print(f"First element in numbers tuple -> {firstelement}")
lastelement = numbers[-1]
print(f"Last element in numbers tuple -> {lastelement}")
middle3elements = numbers[1:4]
print(f"Middle 3 element in numbers tuple -> {middle3elements}")




# Question-> 
'''
2. Write a tuple of fruits. Try:
Counting how many times 'apple' appears
Finding the index of 'banana'
'''
# Soltuion-> 
print("---------------------------")
fruits = ("apple","apple","mango","banana","mango")
print(f"all fruits in tuple ->> {fruits}")
appleCount =fruits.count("apple")
print(f"apple count  in fruits tuple ->> {appleCount}")
bananaIndex = fruits.index("banana")
print(f"banana index  in fruits tuple ->> {bananaIndex}")




# Question-> 
'''
3. Create a student tuple: ("Alex", 23, "B.Tech")
Unpack and print: "Name: Alex | Age: 23 | Course: B.Tech"
'''
# Soltuion-> 
print("---------------------------")
studentDetails =("Alex", 23, "B.Tech")
print(f"all  details in studentdetail tuple ->> {studentDetails}")
name,age,course = studentDetails
print(f"unpack  details in studentdetail tuple ->> Name : {name} | Age : {age} | Course : {course}")




# Question-> 
'''
4. Ask the user to enter 3 favorite movies (one by one), store them in a tuple, and print the result.
'''
# Soltuion-> 
print("---------------------------")
movies = ()
print(f"Before adding favorite movies to tuple ->> {movies}")
movie1 = input("Enter your favorite movie 1->>")
movie2 = input("Enter your favorite movie 2->>")
movie3 = input("Enter your favorite movie 3->>")
print("---------------------------")
movies = tuple(list(movies) + [movie1] + [movie2] + [movie3])
print(f"After add favorite movies in tuple ->> {movies}")



# Question-> 
'''
5. Challenge:
You have a tuple of numbers. Without converting it to a list:
Loop through the items
Print only the even numbers
'''
# Soltuion-> 
print("---------------------------")
numbers1 = (0,1,2,3,4,5,6,7,8,9)
print(f"Before loop -->> {numbers1}")
for i in numbers1:
    if i % 2 == 0:
        print(i)