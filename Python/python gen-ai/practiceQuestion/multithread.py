import threading
from datetime import  date , timedelta ,datetime
import time
import multiprocessing
# Question-> 
"""
1. 3 threads banao — har ek alag kaam kare:
   - Thread 1: 1 se 5 print kare
   - Thread 2: A se E print kare
   - Thread 3: "Hello" 3 baar print kare
   Sab simultaneously chalein
"""
# Soltuion-> 
# print("---------------------------")

def numprint():
    for i in range(1,6):
        print(i)

def greetprint():
    for _ in range(3):
        print("Hello")

def alphaprint():
    for i in "ABCDE":
        print(i)




# Question-> 
"""
2. Threading use karke timer banao —
   ek thread countdown kare (5 se 0),
   doosra thread us time mein 
   kuch aur kaam kare
"""
# Soltuion-> 
# print("---------------------------")

def countdown():
    for i in range(5,-1,-1):
        print(i)

def something():
    print("Do anything")


# Question-> 
"""
3. Multiprocessing basics —
   import multiprocessing
   2 processes banao jo alag alag 
   kaam karein — join() se wait karo
"""
# Soltuion-> 
# print("---------------------------")

def sqaures(n):
    print(n**2,flush=True)

def cube(n):
    print(n**3,flush=True)


# Question-> 
"""
4. 5 threads banao — har ek ek number ka 
   square print kare (1 se 5).
   time.sleep(1) add karo har thread mein.
   Dekho order consistent nahi hoga.
"""
# Soltuion-> 
# print("---------------------------")

def sq(n):
    time.sleep(1)
    print(f"square of {n} : {n**2}")





# Question-> 
"""
5. Threading mein Lock use karo —
   2 threads ek shared counter ko 
   100 baar increment karein.
   Pehle bina Lock ke karo (galat result),
   phir Lock ke saath karo (sahi result).
"""
# Soltuion-> 
# print("---------------------------")
lock = threading.Lock()
counter = 0

def incr():
    global counter
    print(counter)

    for _ in range(10000000):
        counter +=1

def incr2():
    global counter
    print(counter)

    for _ in range(10000000):
        counter +=1

def incr_lock():
    global counter
    print(counter)

    for _ in range(10000000):
        with lock:
            counter +=1

def incr2_lock():
    global counter
    print(counter)

    for _ in range(10000000):
       with lock:
          counter +=1



# Question-> 
"""
6. Thread ko daemon banao:
   ek daemon thread banao jo 
   infinite loop mein kuch print kare,
   main thread 3 seconds baad band ho jaye —
   daemon thread automatically band ho jaaye
"""
# Soltuion-> 
# print("---------------------------")




# Question-> 
"""
7. multiprocessing.Pool use karo:
   Pool(4) banao, [1,2,3,4,5] list pe 
   map() se square function apply karo
"""
# Soltuion-> 
# print("---------------------------")




# Question-> 
"""
8. Ek real scenario — 
   3 files simultaneously download 
   simulate karo (time.sleep se):
   Thread 1: "file1.txt downloading... done" (2 sec)
   Thread 2: "file2.txt downloading... done" (3 sec)  
   Thread 3: "file3.txt downloading... done" (1 sec)
   Total time 3 sec hona chahiye, 6 nahi
"""
# Soltuion-> 
# print("---------------------------")





if __name__ == "__main__":
    print("---------------------------")

    t11 = threading.Thread(target=numprint)
    t12 = threading.Thread(target=alphaprint)
    t13 = threading.Thread(target=greetprint)

    t11.start()
    t12.start()
    t13.start()

    t11.join()
    t12.join()
    t13.join()
    print("---------------------------")

    t21 = threading.Thread(target=countdown)
    t22 = threading.Thread(target=something)

    t21.start()
    t22.start()
    t21.join()
    t22.join()

    print("---------------------------")


    m11 = multiprocessing.Process(target=sqaures,args=(5,))
    m12 = multiprocessing.Process(target=cube,args=(5,))

    m11.start()
    m12.start()
    
    m11.join()
    m12.join()
    
    print("---------------------------")

    Threads = []
    for i in range(1,6):
        t41 = threading.Thread(target=sq,args=(i,))
        Threads.append(t41)
        t41.start() 
    for tt in Threads:
        tt.join()

    print("---------------------------")

    t51 = threading.Thread(target=incr)
    t52 = threading.Thread(target=incr2)

    t51.start()
    t52.start()

    t51.join()
    t52.join() 

    t511 = threading.Thread(target=incr_lock)
    t512 = threading.Thread(target=incr2_lock)

    t511.start()
    t512.start()

    t511.join()
    t512.join()

# sahi hai lekin loop thread ke waqt lagega ... aur call wo loop ke hisab se hoga aur wahi jaaygi fir sqaure print hoga
    # def sq(n):
    #     for _ in range(1,5):
    #         print(n**2)



    # t41 = threading.Thread(target=sq,args=(2,))
    # t42 = threading.Thread(target=sq,args=(1,))
    # t43 = threading.Thread(target=sq,args=(3,))
    # t44 = threading.Thread(target=sq,args=(4,))
    # t45 = threading.Thread(target=sq,args=(5,))

    # t41.start()
    # t42.start()
    # t43.start()
    # t44.start()
    # t45.start()

    # t41.join()
    # t42.join()
    # t43.join()
    # t44.join()
    # t45.join()


# multithread.py



