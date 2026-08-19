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

def greets():
    return "hello, afnan"

print(greets())


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


# Question-> 
"""
1. Ek decorator banao @logger jo 
   function ka naam aur arguments 
   call hone pe print kare:
   "Calling greet with args: ('Afnan',)"
"""
# Soltuion-> 
print("---------------------------")






# Question-> 
"""
2. Ek decorator banao @validate_positive jo 
   function ke arguments check kare — 
   agar koi argument negative ho toh 
   ValueError raise kare
"""
# Soltuion-> 
print("---------------------------")






# Question-> 
"""
3. Do decorators stack karo:
   @timer + @logger dono ek saath 
   ek function pe lagao aur dekho 
   order mein kya hota hai
"""
# Soltuion-> 
print("---------------------------")






# Question-> 
"""
4. Ek decorator banao @cache jo 
   function ka result store kare — 
   same arguments dobara aaye toh 
   function call na kare, cached result do
   (dict use karo store karne ke liye)
"""
# Soltuion-> 
print("---------------------------")






# Question-> 
"""
5. Ek decorator banao @retry(n) jo 
   agar function exception throw kare 
   toh n baar retry kare — 
   sab fail ho jaaye toh finally raise kare
"""
# Soltuion-> 
print("---------------------------")






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