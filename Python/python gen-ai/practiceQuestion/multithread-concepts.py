import time
import threading

def task(name):
    print(f"{name} start")
    time.sleep(2)
    print(f"{name} done")

# Thread banana
t1 = threading.Thread(target=task, args=("Thread-1",))
t2 = threading.Thread(target=task, args=("Thread-2",))

t1.start()
t2.start()

t1.join()  # wait karo t1 khatam hone tak
t2.join()




# multithread-concepts.py