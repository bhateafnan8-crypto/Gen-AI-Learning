import threading
from datetime import datetime ,  date , timedelta
import time 
# Question-> 
"""
1. Create a script that uses two threads: one prints even numbers and one prints odd numbers.
"""
# Soltuion-> 
print("---------------------------")
def even():
    for i in range(1,11):
        if i % 2 == 0:
            print(i)


def odd():
    for i in range(1,11):
        if i % 2 != 0:
            print(i)


t1 = threading.Thread(target=even)
t2 = threading.Thread(target=odd)

t1.start()
t2.start()
t1.join()
t2.join()



# Question-> 
"""
2. Simulate downloading 5 files using threads (just use time.sleep()).
"""
# Soltuion-> 
print("---------------------------")
def download(fileName):
    print(f"{fileName} downloading....")
    time.sleep(2)
    print(f"{fileName} downloaded!!")

threads =[]

for i in range(1,6):
    fileName = f"fileName{i}.text"
    t = threading.Thread(target=download,args=(fileName,))

    threads.append(t)

    t.start()

for t in threads:
    t.join()


# Question-> 
"""
3. Use threading.Lock() to safely update a global counter in multiple threads.
"""
# Soltuion-> 
print("---------------------------")


counter = 0

lock = threading.Lock()

def increment():
    global counter
    for _ in range(1000):
        with lock:
            counter += 1

t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start()
t2.start()
t1.join()
t2.join()

print(counter)