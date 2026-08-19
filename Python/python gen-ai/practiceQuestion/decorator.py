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
4. Ek decorator banao @logger jo 
   function ka naam aur arguments 
   call hone pe print kare:
   "Calling greet with args: ('Afnan',)"
"""
# Soltuion-> 
print("---------------------------")

def logger(func):
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        args_value = ", ".join(str(arg) for arg in args)
        print(f"Calling {func.__name__} with args: ('{args_value}',) ")
        return result
    return wrapper

@logger
def greet(name):
    return name

greet("Afnan")


# Question-> 
"""
5. Ek decorator banao @validate_positive jo 
   function ke arguments check kare — 
   agar koi argument negative ho toh 
   ValueError raise kare
"""
# Soltuion-> 
print("---------------------------")

def validate_positive(func):
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)

        try:
            args_value = ", ".join(str(arg) for arg in args)

            if int(args_value) < 0:
                raise ValueError("Number should not be negative")
                return
            if int(args_value) == 0:
                raise ValueError("Number should not be zero,null,empty,undefined ...")
            print(f"Calling {func.__name__} with your positivie number : {args_value}")
            return result
        except ValueError as e:
            print(f"Error: {e}")

    return wrapper

@validate_positive
def check(n):
    return n

check(2)
check(0)
check(-1)


# Question-> 
"""
6. Do decorators stack karo:
   @timer + @logger dono ek saath 
   ek function pe lagao aur dekho 
   order mein kya hota hai
"""
# Soltuion-> 
print("---------------------------")

@timer
@logger
def stack(name):
    time.sleep(2)
    return name

stack("Aadfar")

# running order ->  logger then timer 


# Question-> 
"""
7. Ek decorator banao @cache jo 
   function ka result store kare — 
   same arguments dobara aaye toh 
   function call na kare, cached result do
   (dict use karo store karne ke liye)
"""
# Soltuion-> 
print("---------------------------")
def cache(func):
    cache_value = {}
    print(cache_value)
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper

@cache
def cache_store(a,b):
    time.sleep(2)
    return a + b


print(cache_store(1,2))
print(cache_store(2,3))
print(cache_store(1,2))

@cache
def cache_name(name):
    time.sleep(4)
    return name

print(cache_name("Afnan"))
print(cache_name("Adfar"))
print(cache_name("Afnan"))


# Question-> 
"""
8. Ek decorator banao @retry(n) jo 
   agar function exception throw kare 
   toh n baar retry kare — 
   sab fail ho jaaye toh finally raise kare
"""
# Soltuion-> 
print("---------------------------")
def retry(n):
    def decorators(func):
        def wrapper(*args,**kwargs):
            attempts = 0
            final_err = None
            while attempts < n:
                try:
                    result = func(*args,**kwargs)
                    return result
                except Exception as error:
                    attempts+=1
                    final_err = error
                    print(f"error: (Attempt {attempts} failed : {error})")
            print(f"All {n} attempts failed. Final error: {final_err}")
            raise final_err 
        return wrapper
    return decorators

@retry(5)
def ret_exec(a,b):
    return a/b

print(ret_exec(2,4))
print(ret_exec(4,2))
try:
    print(ret_exec(2,0))
except Exception as e:
    print(f"caught : {e}")





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



# code pura sahi lekin traceback de raha hai meko only error message print chahiye..

    # def validate_positive(func):
    #     def wrapper(*args,**kwargs):
    #         result = func(*args,**kwargs)
    #         args_value = ", ".join(str(arg) for arg in args)

    #         if int(args_value) < 0:
    #             raise ValueError("Value should not be negative")
    #             return
    #         if int(args_value) == 0:
    #             raise ValueError("Number should not be zero,null,empty,undefined ...")
    #         print(f"Calling {func.__name__} with your positivie number : {args_value}")
    #         return result

    #     return wrapper

    # @validate_positive
    # def check(n):
    #     return n

    # check(2)
    # check(0)
    # check(-1)



# kuch to galat hai yaha -- yaha galti main func means simple function ko print nahi kiya aur .. aur string aur tuple ka short ho raha hai..
# Issue: {} is printed when the decorator is created, before cache_store() is called; additionally, the cache key is checked as a string but stored as a tuple, so caching fails.
    # def cache(func):
    #     cache_value = {}
    #     print(cache_value)
    #     def wrapper(*args,**kwargs):
    #         if args in cache_value:
    #             return cache_value[args]
    #         result = func(*args,**kwargs)
    #         # args_value = ", ".join(str(arg) for arg in args)
    #         # kwargs_value = ", ".join(f"{k} : {v}" for k , v in kwargs)

    #         # if args_value in cache_value:
            
    #         cache_value[args] = result
    #         return result
    #     return wrapper

    # @cache
    # def cache_store(name):
    #     return name

    # cache_store("Afnan")
    # cache_store("Adfar")
    # cache_store("Afnan")

#  yaha pe pehle mene return ko try except ke bahar kiya tha jisse value return hi nahi ho raha hai jo sahi hai... aur pura Exception ki bajaye zero le raha tha ab pura liya hu niche aur return bhi try ke andar hai niche ke usme abhi bhi bugs hai... ab retry ke liye meko jab error aaye to usko error dene ke bajaye retry karna chahiye matlab ke attempt ko increment karna chahiye lekin mene waha pehle error diya fir increment jo galat hai waha retry hua nahi error de raha hai pehle fir waps chal raha meko last wala dikhana tha to usko loop ke bahar chahiye tha lekin andar rakh diya.. aur error print karana tha failed attempt ke sath lekin mene wo Exception isko return karaya lekin meko isko raaise karna tha aur wo error jo meko jaisa chahiye usko bhejna tha

    # def retry(n):
    #     def decorators(func):
    #         def wrapper(*args,**kwargs):
    #             attempts = 0
    #             while attempts < n:
    #                 try:
    #                     result = func(*args,**kwargs)
    #                     return result
    #                 except Exception:
    #                     print("error")
    #                     attempts+=1
    #                 return Exception
    #         return wrapper
    #     return decorators

    # @retry(5)
    # def ret_exec(a,b):
    #     return a/b

    # print(ret_exec(2,4))
    # print(ret_exec(4,2))
    # print(ret_exec(2,0))
    # print(ret_exec(2,0))
    # print(ret_exec(2,0))
    # print(ret_exec(2,0))
    # print(ret_exec(2,0))
    # print(ret_exec(2,0))


#  abhi ke isme last waala hat ja raha hai to usko ek var me safe karke usko return karana hai.. 


    # def retry(n):
    #     def decorators(func):
    #         def wrapper(*args,**kwargs):
    #             attempts = 0
    #             while attempts < n:
    #                 try:
    #                     result = func(*args,**kwargs)
    #                     return result
    #                 except Exception as error:
    #                     attempts+=1
    #                     print(f"error: (Attempt {attempts} failed : {error})")
    #             raise error
    #         return wrapper
    #     return decorators

    # @retry(5)
    # def ret_exec(a,b):
    #     return a/b

    # print(ret_exec(2,4))
    # print(ret_exec(4,2))
    # print(ret_exec(2,0))
    # print(ret_exec(2,0))
    # print(ret_exec(2,0))
    # print(ret_exec(2,0))
    # print(ret_exec(2,0))
    # print(ret_exec(2,0))


#  niche wala code sahi hai abhi pure.. pehle galat tha.. baar baar call karne se repeat ho raha tha wo retry(5) ka 5 baar baar ja raha tha.. aur aise ke bajaye return kiya jo sawal se ulta tha.. matlab sawal me raise bola tha mene return kiya tha... aur final err dikaha jo last me bataye ke saara fail hogaya.. aur jaha error aayga usko try me liya call karte waqt fir finally jo main error hai wo dikhaya end ex. division by zero isko pehle 5 attempts se dikhaya fir final me dikahaya aisa ke 5 attempts finished-failed all failed.. and last me jo error aaya tha jaise "division by zero" ye hai to sirf "division by zero" isko print karwaya..

    # def retry(n):
    #     def decorators(func):
    #         def wrapper(*args,**kwargs):
    #             attempts = 0
    #             final_err = None
    #             while attempts < n:
    #                 try:
    #                     result = func(*args,**kwargs)
    #                     return result
    #                 except Exception as error:
    #                     attempts+=1
    #                     final_err = error
    #                     print(f"error: (Attempt {attempts} failed : {error})")
    #             print(f"All {n} attempts failed. Final error: {final_err}")
    #             raise final_err 
    #         return wrapper
    #     return decorators

    # @retry(5)
    # def ret_exec(a,b):
    #     return a/b

    # print(ret_exec(2,4))
    # print(ret_exec(4,2))
    # try:
    #     print(ret_exec(2,0))
    # except Exception as e:
    #     print(f"caught : {e}")