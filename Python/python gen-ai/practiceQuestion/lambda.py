from functools import reduce
# Question-> 
"""
1. Write a lambda function to calculate cube of a number.
# Expected output: 27 for input 3
"""
# Soltuion-> 
print("---------------------------")
cube = lambda num,exp : num ** exp
print(f"cube of number => {cube(3,3)}")



# Question-> 
"""
2. Use lambda and filter() to extract only names starting with “A”.
names = ["Alice", "Bob", "Alex", "David"]
# Output: ['Alice', 'Alex']
"""
# Soltuion-> 
print("---------------------------")
names = ["Alice", "Bob", "Alex", "David"]
filter_names = list(filter(lambda name : name.startswith('A'),names))
print(f"filtered name with startwith => {filter_names}")



# Question-> 
"""
3. Sort a list of dictionaries by the 'age' key using lambda.
people = [{'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 20}]
# Output: [{'name': 'Jane', 'age': 20}, {'name': 'John', 'age': 25}]
"""
# Soltuion-> 
print("---------------------------")
people = [{'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 20}]
sorted_list = list(sorted(people,key=lambda peoples: peoples["age"]))

print(f"sorted using age => {sorted_list}")




# Question-> 
"""
4. Use lambda with map() to convert all strings in a list to uppercase.
words = ['hello', 'world']
# Output: ['HELLO', 'WORLD']
"""
# Soltuion-> 
print("---------------------------")
words = ['hello', 'world']
map_words = list(map(lambda word : word.upper(),words))
print(f"map for lower to upper => {map_words}")

# Question-> 
"""
5. Bonus: Use reduce() and lambda to find the maximum value in a list.
from functools import reduce
nums = [4, 7, 2, 9, 1]
# Output: 9
"""
# Soltuion-> 
print("---------------------------")
nums = [4, 7, 2, 9, 1]
reduce_nums = reduce(lambda x , y : max(x,y) ,nums)
print(f"reduce to max number => {reduce_nums}")

