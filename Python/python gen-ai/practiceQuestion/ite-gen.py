# # Question-> 
# """
# 1. Generator banao jo 1 se n tak 
#    sirf even numbers yield kare
# """
# # Soltuion-> 
# print("---------------------------")
# def even(num):
#     for i in range(1,num + 1):
#         if i % 2 == 0:
#             yield i

# for num in even(10):
#     print(num)


# # Question-> 
# """
# 2. Generator banao jo ek list mein se 
#    ek ek element yield kare — 
#    manually next() se call karo
# """
# # Soltuion-> 
# print("---------------------------")

# lst = [1,2,3,4,5,6,7,8,9,10]

# def counts(lst):
#     for i in lst:
#         yield i 

# gen = counts(lst)
# print(next(gen))
# print(next(gen))
# print(next(gen))


# # for i in counts(lst):
# #     print(i)


# # Question-> 
# """
# 3. Iterator class banao "Countdown" jo 
#    n se 0 tak count kare
# """
# # Soltuion-> 
# print("---------------------------")
# class Countdown:
#     def __init__(self,start):
#         self.current = start

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.current  < 0:
#             raise StopIteration
#         self.current -= 1
#         return self.current + 1 

# for num in Countdown(5):
#     print(num)


# Question-> 
"""
4. Generator banao jo Fibonacci sequence 
   yield kare — n terms tak
"""
# Soltuion-> 
print("---------------------------")
def genfibo(n):
    a,b = 0,1
    count = 0

    while count < n:
        yield a 
        a,b = b , a + b
        count += 1

fibo = genfibo(4)

print(next(fibo))
print(next(fibo))
print(next(fibo))
print(next(fibo))

for num in genfibo(5):
    print(num)

    # for fibo in range(2,n+1):

# Question-> 
"""
5. Generator banao jo ek file ki lines 
   ek ek karke yield kare 
   (pehle ek dummy file banao)
"""
# Soltuion-> 
print("---------------------------")

    
def gens():
    with open("gen.txt","r") as f :
        reads = f.readlines()
        for i in reads:
            yield i

itegen = gens()

print(next(itegen))

# for i in itegen():
#     print(i)


# Question-> 
"""
6. Iterator class banao "EvenNumbers" jo 
   0 se shuru karke sirf even numbers de — 
   infinite iterator (StopIteration kabhi nahi)
   Sirf pehle 5 next() se lo
"""
# Soltuion-> 
print("---------------------------")
class EvenNumbers:
    def __init__(self):
        self.curr = 0

    def __iter__(self):
        return self

    def __next__(self):

        temp = self.curr

        self.curr += 2

        # temp = self.curr

        return temp
        

even = EvenNumbers()

print(next(even))
print(next(even))
print(next(even))
print(next(even))


# Question-> 
"""
7. Generator expression use karo 
   (list comprehension jaisi — but generator):
   squares = (x*x for x in range(10))
   - Pehle 3 next() se lo
   - Phir baaki for loop se print karo
"""
# Soltuion-> 
print("---------------------------")

def gensq():
    squares = (x*x for x in range(10))
    yield from squares

sq = gensq()


print(next(sq))
print(next(sq))
print(next(sq))

for i in sq:
    print(i)

print("\n gen expression 2  \n")

squares = (x*x for x in range(10))

print(next(squares))
print(next(squares))
print(next(squares))

for i in squares:
    print(i)


# Question-> 
"""
8. Ek generator banao "batch(lst, size)" jo 
   list ko chunks mein yield kare:
   batch([1,2,3,4,5,6,7], 3) 
   → [1,2,3] → [4,5,6] → [7]
"""
# Soltuion-> 
print("---------------------------")

def genchunks(lst,size):
    for i in range(0,len(lst),size):
        yield lst[i:i+size]
    
for chunk in genchunks([1,2,3,4,5,6,7,8,9,10],3):
    print(chunk)

for chunk in genchunks([1,2,3,4,5,6,7],3):
    print(chunk)


    #  stop = len(lst)
    #     step = size


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