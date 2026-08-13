# Question-> 
"""
1. Ek function banao jo kitne bhi numbers lo 
   aur unka average return kare — *args use karo
"""
# Soltuion-> 
print("---------------------------")
def average(*args):
    return sum(args)/len(args)

print(f"\naverage => {average(1,2,3,4,5)}\n")

import statistics

def average1(*args):
    return statistics.mean(args)

print(f"\naverage using statistics method (statistics.mean())  => {average(1,2,3,4,5)}\n")


# Question-> 
"""
2. Ek function banao jo **kwargs lo aur 
   har key-value pair print kare — 
   "Key: name, Value: Afnan" format mein
"""
# Soltuion-> 
print("---------------------------")

def showname(**kwargs):
    for key,value  in kwargs.items():
        print(f"\nkey : '{key}' , value : '{value}' \n")

showname(name="Afnan")


# Question-> 
"""
3. Dono combine karo — ek function jo 
   *args mein numbers lo aur **kwargs mein 
   label lo, aur print kare:
   "Total of [label] => [sum]"
"""
# Soltuion-> 
print("---------------------------")

def show(*args,**kwargs):
    print(f"\ntotal of {kwargs['label']} : {sum(args)}\n")

show(1,2,3,4,label="Science")


# Question-> 
"""
4. Ek function banao jo *args mein strings lo 
   aur sabko ek saath join karke return kare 
   (separator space ho)
"""
# Soltuion-> 
print("---------------------------")

print("\nsol - 1\n")
def joins(*args):
    return " ".join(args)

print(f'\njoint of strings with space separator => {joins("Hello","Good","Morning")}\n')

print("\nsol - 2\n")

def joint(*args):
   sentence = ""

   for i , w in enumerate(args):
      if i > 0:
         sentence += " "
      sentence += w

   return sentence

print(f'\njoint of strings with space separator => {joint("Hello","Good","Morning")}\n')

print("\nsol - 3\n")

def word_join(*args):
   return " ".join(str(item) for item in args)

print(f'\njoint of strings with space separator => {word_join("Hello","Good","Morning")}\n')


print("\nsol - 4\n")

def sentence_word(*args):
   return " ".join(map(str,args))
print(f'\njoint of strings with space separator => {sentence_word("Hello","Good","Morning")}\n')

print("\nsol - 5\n")

from functools import reduce
def senword_join(*args):
   return reduce(lambda a , b:  f"{a} {b}" , args)
print(f'\njoint of strings with space separator => {senword_join("Hello","Good","Morning")}\n')

print("\nsol - 6\n")

def simple_join(*args):
   print(*args,sep=" ")
print(f'\njoint of strings with space separator =>',end="")
simple_join("Hello","Good","Morning")
print("\n")


# Question-> 
"""
5. Ek function banao jisme default arguments hon:
   greet(name, msg="Hello") 
   — agar msg na do toh "Hello" use ho,
   — agar do toh woh use ho
"""
# Soltuion-> 
print("---------------------------")

print("\nsol - 1\n")

def greet(name, msg="Hello"):
   return f"{msg}, {name}"

print(f'default arguments => {greet("Afnan","Good Morning")}')

print("\nsol - 2\n")

def greets(name,msg = None):
   if msg is None:
      msg = "Hello"
   return f"{msg}, {name}"

print(f'default arguments => {greets("Afnan","Good Morning")}')

print("\nsol - 3\n")

def greet1(name,msg=None):
   return f"{msg or 'Hello'}, {name}"

print(f'default arguments => {greet("Afnan","Good Morning")}')


print("\nsol - 4\n")

def greet2(name, *,msg="Hello"):
   return f"{msg}, {name}"


print(f'default arguments => {greet2("Afnan",msg="Good Morning")}')


# Question-> 
"""
6. Ek function banao jo *args aur **kwargs dono le.
   *args mein numbers, **kwargs mein "operation" key ho
   — "sum" ho toh total print karo
   — "avg" ho toh average print karo
"""
# Soltuion-> 
print("---------------------------")

print("\nsol - 1\n")

def argkwarg(*args,**kwargs):
   if kwargs['label'] == "sum":
      return sum(args)
   if kwargs['label'] == "avg":
      return sum(args) / len(args)

print(f"combination of args and kwargs for operations and text => {argkwarg(1,2,3,4 , label = "avg")}")

print("\nsol - 2\n")

def sumavg(*args,**kwargs):
   op = kwargs.get("operation","sum")

   if not args:
      print("No numbers provided")
      return

   if op == "sum":
      print(f"sum => {sum(args)}")

   elif op == "avg":
      print(f"average => {sum(args) / len(args)}")

   else:
      print(f"Unknown operations: {op}")

sumavg(1,20,30,2,operation = "avg")

print("\nsol - 3\n")


def avgsum(*args,operation = "sum"):
   if not  args:
      print("No numbers provided")
      return

   if operation == "sum":
      print(f"sum => {sum(args)}")
   elif operation == "avg":
      print(f"average => {sum(args) / len(args)}")
   else:
      print(f"Unknown operations: {operation}")

avgsum(10,20,30,40)

print("\nsol - 4\n")

import statistics

ops = {

   "sum" : lambda nums : sum(nums),
   "avg" : lambda nums : statistics.mean(nums)
}
def ak_args(*args,operation = "sum"):
   if not args:
      print("No numbers provided")
      return
   fnc = ops.get(operation)
   if not fnc:
      print(f"Unknown operation : {operation}")
      return
   print(f"operation of sum or avg => {fnc(args)}")

ak_args(1,2,3,4)

print("\nsol - 5\n")

def avgsumak(*args, operation = "sum"):
   nums = []

   for x in args:
      try:
          nums.append(float(x))
      except (ValueError , TypeError):
         print(f"Non numbers provided => {x}")
         return

   if not nums:
      print(f"No numbers provided ")
      return

   if operation  == "sum":
      print(f"sum => {sum(nums)} ")
   elif operation == "avg":
      print(f"average => {sum(nums) / len(nums)}")
   else:
      print(f"Unknown operation => {operation}")

avgsumak(1,2,3,4,90,operation="avg")


# Question-> 
"""
7. Positional + keyword + default — teeno ek saath:
   def order(item, quantity, price=100)
   — call karo different ways se:
     order("Pen", 5)
     order("Book", quantity=3, price=250)
"""
# Soltuion-> 
print("---------------------------")
print("\nsol - 1\n")

def order(item,quantity,price = 100):
   return f"{item} - {quantity} - {price}"

print(f"order 1 => {order('Pen', 5)}")
print(f"order 2 => {order('Book', quantity=3, price=250)}")

print("\nsol - 2\n")

def orders(item,quantity,price=None):
   if price is None:
      price = 100
   else:
      price

   if quantity < 0:
      raise ValueError("Quantity must be > 0") 
   else:
      return f"{item} - {quantity} - {price}"

print(f"orders 1 => {orders('Pen', 5)}")
print(f"orders 2 => {orders('Book', quantity=3, price=250)}")


print("\nsol - 3\n")

def order1(item,quantity, *, price = 100):
   return f"{item} - {quantity} - {price}"

print(f"order 1 => {order1('Pen', 5)}")
print(f"order 2 => {order1('Book', quantity=3, price=250)}")

print("\nsol - 4\n")

def order2(item,quantity,price = 100 ,**kwargs):
   return f"{item} - {quantity} - {price}"
print(f"order 1 => {order2('Pen', 5)}")
print(f"order 2 => {order2('Book', quantity=3, price=250)}")

print("\nsol - 5\n")

from dataclasses import dataclass

@dataclass
class Order:
   item:str
   quantity:int
   price:float = 100.0

def order3(item : str , quantity : int , price : float = 100.0) -> Order:
   if quantity < 0:
      raise ValueError("Quantity must be > 0")
   return Order(item= item , quantity= int(quantity) , price=float(price))


print(f"order 1 => {order3('Pen', 5)}")
print(f"order 2 => {order3('Book', quantity=3, price=250)}")
print(f"order 3 => {order3('Book', quantity=3, price=250)}")
params = {'item': 'Pencil', 'quantity': 2, 'price': 15}
print(f"order 4 => {order3(**params)}")


# Question-> 
"""
8. Ek function banao jo **kwargs mein 
   student details lo (name, marks, grade)
   aur formatted print kare — 
   agar koi key missing ho toh 
   "N/A" print kare uski jagah
   (Hint: kwargs.get() use karo)
"""
# Soltuion-> 
print("---------------------------")

print("\nsol - 1\n")

def showstudent(**kwargs):
   name =  kwargs.get("name","N/A")
   marks = kwargs.get("marks","N/A")
   grade = kwargs.get("grade","N/A") 
   print(f"Name : {name}\nMarks : {marks}\nGrade : {grade}")

showstudent(name= "Afnan" , marks= 80 , grade="A")


print("\nsol - 2\n")

def showstudent1(**kwargs):
   for k in ("name","marks","grade"):
      print(f"{k.capitalize()} : {kwargs.get(k,"N/A")}")
showstudent1(name= "Afnan" , marks= 80 , grade="A")


print("\nsol - 3\n")

def showstudent2(**kwargs):
   for k in ("name","marks","grade"):
      print(f"{k.capitalize()} : {kwargs.setdefault(k,"N/A")}")

showstudent2(name= "Afnan" , marks= 80 , grade="A")


print("\nsol - 4\n")

@dataclass
class Student:
   name:str = "N/A"
   marks:object = "N/A"
   grade:str = "N/A"
def showstudent3(**kwargs):
   s = Student(**{k:v for k , v in kwargs.items() if k in Student.__annotations__})
   print(s)
showstudent3(name= "Afnan" , marks= 80 , grade="A")


print("\nsol - 5\n")

from typing import Optional
@dataclass
class Student:
   name:str = "N/A"
   marks:Optional[float] = None
   grade:str = "N/A"

def showstudent4(**kwargs):
   s = Student(**{k:v for k , v in kwargs.items() if k in Student.__annotations__})
   print(s)

showstudent4(name= "Afnan" , marks= 80 , grade="A")


print("\nsol - 6\n")

from typing import Union
@dataclass
class Student:
   name:str = "N/A"
   marks:Union[int,float,str] = "N/A"
   grade:str = "N/A"

def showstudent5(**kwargs):
   s = Student(**{k:v for k , v in kwargs.items() if k in Student.__annotations__})
   print(s)

showstudent5(name= "Afnan" , marks= 80 , grade="A")

print("\nsol - 7\n")

from typing import Any
@dataclass
class Student:
   name:str = "N/A"
   marks:Any = "N/A"
   grade:str = "N/A"

def showstudent6(**kwargs):
   s = Student(**{k:v for k , v in kwargs.items() if k in Student.__annotations__})
   marks_display = "N/A" if s.marks is None else s.marks
   print(f"Name: {s.name}\nMarks: {marks_display}\nGrade: {s.grade}\n")

showstudent6(name= "Afnan" , marks= 80 , grade="A")

showstudent6(name= "Afnan")







# wrong solution of Q-8

# def showstudent(**kwargs):
#    for key , value in kwargs.items():
#       key = kwargs.get(key,"N/A")
#       print(f"student details => {key} : {value} ")

# showstudent(name="Afnan",marks=40,grade="A+")


