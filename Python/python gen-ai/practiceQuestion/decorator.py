# Question-> 
"""
1. Ek decorator banao @timer jo 
   function ka execution time print kare
   (import time use karo)
"""
# Soltuion-> 
print("---------------------------")

import time

def timer(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f"{func.__name__} took{end-start:.4f} sec")
        return result
    return wrapper

@timer
def times():
    print(time.ctime())
    time.sleep(1)

times()
# print(times())


# Question-> 
"""
2. Ek decorator banao @uppercase jo 
   function ka return value 
   uppercase mein convert kare
"""
# Soltuion-> 
print("---------------------------")
def uppercase(func):
    def wrapper(*args,**kwargs):
        result =  func(*args,**kwargs)
        return result.upper()
    return wrapper

@uppercase

def uppercase():
    return "hello, afnan"

print(uppercase())


# Question-> 
"""
3. Ek decorator banao @repeat(n) jo 
   function ko n baar call kare
   (argument wala decorator)
"""
# Soltuion-> 
print("---------------------------")

def repeat(n):
    def decorator(func):
        def wrapper(*args,**kwargs):
            result = None

            for _ in range(n):
                result = func(*args,**kwargs)

            return result

        return wrapper

    return decorator

@repeat(3)
def greet(name):
    print("hello,",name)

greet("Adfar")


"""

"""





# decorator.py



#  galat hai pura hi

# def uppercase(func):
#     def wrapper(*args,**kwargs):
#         return func(args.upper(),kwargs.upper())
#     return wrapper

# @uppercase

# def uppercase(*args,**kwargs):
#     print("hello")

# uppercase("hello","afnan")