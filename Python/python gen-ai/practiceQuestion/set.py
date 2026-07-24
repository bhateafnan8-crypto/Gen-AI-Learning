# Question-> 
'''
1. Remove Duplicates from a List
nums = [1, 2, 2, 3, 4, 4, 5]
# Write code to remove duplicates and print sorted result
'''
# Soltuion-> 
print("---------------------------")
nums = [1, 2, 2, 3, 4, 4, 5]
print(f"list as a tise ->> {nums}")
numsSet = set([1, 2, 2, 3, 4, 4, 5])
print(f"list to set remove duplicates ->> {numsSet}")
sortedSet = sorted(numsSet)
print(f"list to set sorted ->> {sortedSet}")


# Question-> 
'''
2. Find Common Items Between Two Lists
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
# Use sets to print the common elements
'''
# Soltuion-> 
print("---------------------------")
list1 = set([1, 2, 3, 4])
list2 = set([3, 4, 5, 6])
print(f"list to set convert -> list1:{list1} and list2:{list2}")
commonItems = list1.intersection(list2)
print(f"list to set convert and common items only -> {commonItems}")



# Question-> 
'''
3. Set Difference
a = [1, 2, 3, 4, 5]
b = [3, 4, 6]
# Print elements in a but not in b
'''
# Soltuion-> 
print("---------------------------")
a = set([1, 2, 3, 4, 5])
b = set([3, 4, 6])
print(f"list to set convert -> a:{a} and b:{b}")
commonItems2 = a.difference(b)
print(f"list to set convert and common items only -> {commonItems2}")


# Question-> 
'''
4. Fast Membership Check
words = ["apple", "banana", "grape", "orange"]
# Convert to set and check if "grape" exists
'''
# Soltuion-> 
print("---------------------------")
words = ["apple", "banana", "grape", "orange"]
print(f"list without conversion ->> {words}")
wordsSet = set(["apple", "banana", "grape", "orange"])
print(f"list to set conversion->> {wordsSet}")
fastMembership = "grape" in wordsSet
print(f"membership of grape in set ->> {fastMembership}")
