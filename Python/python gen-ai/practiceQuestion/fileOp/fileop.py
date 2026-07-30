from datetime import datetime
# Question-> 
"""
1. Write a To-Do List
Ask user to input 3 tasks
Save them to todo.txt (one task per line)
"""
# Soltuion-> 
print("---------------------------")
print("---------------------------")
print("---------------------------")
list1= input("Enter task for add to list  =>") 
list2= input("Enter task for add to list  =>") 
list3= input("Enter task for add to list  =>") 
print("---------------------------")


file = open("todo.txt","w")
file.write(f"{list1}\n{list2}\n{list3}")
file.close()



# Question-> 
"""
2. Append Timestamped Logs
Append 3 lines of log messages to log.txt with timestamps (use datetime.now())
"""
# Soltuion-> 
print("---------------------------")
# file1 = open("log.txt" ,"a")
file1 = open("log.txt" ,"w")
for i in range(1,4):
    file1.write(f"Timestamped {datetime.now()}\n")
file1.close()



# Question-> 
"""
3. File Analyzer
Read a file
Count number of lines and characters
Print them
"""
# Soltuion-> 
print("---------------------------")
file2 = open("todo.txt","r")
lines = file2.readlines()


print(f"count of lines = {len(lines)}")

print(f"count of characters => {sum(len(line) for line in lines)}")
file2.close()


# Question-> 
"""
4. Reverse File Content
Read content from story.txt
Write reversed content to story_reversed.txt
"""
# Soltuion-> 
print("---------------------------")

story = open("story.txt","w")
story.write("hellllllo")
story_content = story.write("hellllllo")

story = open("story.txt","r")
story_content = story.read()

reversedContent = story_content[::-1]

story = open("story.txt","a")
story.write(f"\n{reversedContent}")


story.close()




# Question-> 
"""
5. Word Frequency Counter
Read from a file
Count how many times each word occurs (use dictionary)
"""
# Soltuion-> 
print("---------------------------")

freq = open("todo.txt","r")
freqContent = freq.read()

words = freqContent.split()

word = {}

for ch in words:
    word[ch] = word.get(ch,0) + 1
print(f"count of word => {word}")
freq.close()
