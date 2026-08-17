# Question-> 
"""
1. Generator banao jo 1 se n tak 
   sirf even numbers yield kare
"""
# Soltuion-> 
print("---------------------------")
def even(num):
    for i in range(1,num + 1):
        if i % 2 == 0:
            yield i

for num in even(10):
    print(num)


# Question-> 
"""
2. Generator banao jo ek list mein se 
   ek ek element yield kare — 
   manually next() se call karo
"""
# Soltuion-> 
print("---------------------------")

lst = [1,2,3,4,5,6,7,8,9,10]

def counts(lst):
    for i in lst:
        yield i 

gen = counts(lst)
print(next(gen))
print(next(gen))
print(next(gen))


# for i in counts(lst):
#     print(i)



# Question-> 
"""
3. Iterator class banao "Countdown" jo 
   n se 0 tak count kare
"""
# Soltuion-> 
print("---------------------------")


class Countdown:
    def __init__(self,start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current  < 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1 

for num in Countdown(5):
    print(num)



# ite-gen.py


# for loop nahi chahiye tha aur next galat me lagaya .. loop galat lagaya tha usme se elements lena tha numbers le raha tha shuru se aakhir tak ka, aur func call kar ke save karna tha fir usme next lagana tha...


# lst = [1,2,3,4,5,6,7,8,9,10]

# def counts(lst):
#     for i in range(lst[0],len(lst)+1):
#         yield i 

    
# print(next(counts(lst)))


 # yaha pe pura hi galat hai.. 
# class count:
#     def __init__(self,curr):
#         # self.limit = 0
#         self.current = curr

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if 0 >= self.current:
#             raise StopIteration
#         self.current -= 1
#         return self.current 

# for num in count(5):
#     print(num)

 # calling galat hai.. counts nahi likhna tha counts se wo baar baar naya bana raha hai... ek hi baar banake baar baar call karna hai..

# print(next(counts(gen)))
# print(next(counts(gen)))
# print(next(counts(gen)))