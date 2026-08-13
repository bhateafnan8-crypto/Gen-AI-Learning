# Question-> 
"""
1. Shape class banao with method area().
   Circle aur Rectangle — dono inherit karein 
   aur apna apna area() calculate karein.
"""
# Soltuion-> 
print("---------------------------")
print("\nsol-1\n")

class shape:
    def area(self):
        return "shape area"

class circle(shape):
    def area(self):
        return f"circle area"

class rectangle(shape):
    def area(self):
        return f"rectangle area "

shapes = [circle(),rectangle()]

for shape1 in shapes:
    print(shape1.area())


print("\nsol-2\n")

class Shapes:
    def area(self):
        return "shape area"

class circles(Shapes):
    def area(self,r):
        return f"circle area => {r*r*3.14}"

class rectangles(Shapes):
    def area(self,l,w):
        return f"rectangle area => {l*w}"

s,c,r = Shapes(),circles(),rectangles(),

print(s.area())
print(r.area(2,4))
print(c.area(4))

print("\nsol-3\n")

class shape1:
    def area(self):
        pass

class circle1(shape1):
    def __init__(self,r):
        self.r = r
    def area(self):
        return f"circle area : {3.14*self.r*self.r}"

class rectangle1(shape1):
    def __init__(self,l,w):
        self.l = l
        self.w = w
    def area(self):
        return f"rectangle area : {self.l*self.w} "

shapes = [circle1(2),rectangle1(4,8)]

for s in shapes:
    print(s.area())
# Question-> 
"""
2. Animal class banao with method sound().
   Dog, Cat, Cow — teeno override karein.
   Ek loop mein sab ka sound print karo.
"""
# Soltuion-> 
print("---------------------------")

class Animals:
    def sound(self):
        return "sound"

class Dog:
    def sound(self):
        return "woof"

class Cat:
    def sound(self):
        return "Meow"

class Cow:
    def sound(self):
        return "Wooow"

animals = [Animals(),Dog(),Cat(),Cow()] 

for animal in animals:
    print(animal.sound())


# Question-> 
"""
3. Duck typing — do alag classes banao 
   Payment aur Refund, dono mein process() method ho.
   Ek function execute(obj) banao jo 
   sirf obj.process() call kare — 
   bina type check kiye.
"""
# Soltuion-> 
print("---------------------------")

class Payment:
    def process(self):
        return "payment process"

class Refund:
    def process(Self):
        return"refund process"

def execute(obj):
    return obj.process()

print(f"{execute(Payment())} | {execute(Refund())}")


# Question-> 
"""
4. Vehicle class banao with method fuel_type().
   Car, Bike, Truck — teeno override karein.
   Loop mein sab ka fuel_type() print karo.
"""
# Soltuion-> 
print("---------------------------")

class Vehichle:
    def fuel_type(self):
        pass

class Car(Vehichle):
    def __init__(self,f):
        self.fuel = f

    def fuel_type(self):
        return f"Car => {self.fuel}" 

class Bike(Vehichle):
    def __init__(self,f):
        self.fuel = f

    def fuel_type(self):
        return f"Bike => {self.fuel}" 

class Truck(Vehichle):
    def __init__(self,f):
        self.fuel = f

    def fuel_type(self):
        return f"Truck => {self.fuel}" 

vehicles = [Car("E50"), Bike("E30"), Truck("E20")]

for veh in vehicles:
    print(veh.fuel_type())


# Question-> 
"""
5. Employee class banao with method salary().
   FullTime aur PartTime — dono inherit karein.
   FullTime ko fixed 50000, 
   PartTime ko hours * rate calculate kare.
   Constructor mein values lo.
"""
# Soltuion-> 
print("---------------------------")

class Employee:
    def salary(self):
        pass


class FullTime(Employee):
    def __init__(self):
        self.sal = 50000

    def salary(self):
        return f"Full Time sal => {self.sal}"

class PartTime(Employee):
    def __init__(self,hours,rate):
        self.hours = hours
        self.rate = rate

    def salary(self):
        return f"Part Time sal using sal amnt per hour => {self.hours*self.rate}"

salaries = [FullTime(),PartTime(4,2000)]

for sal in salaries:
    print(sal.salary())


# Question-> 
"""
6. Notification class banao with method send().
   Email, SMS, Push — teeno override karein.
   Ek function notify(obj) banao jo 
   sirf obj.send() call kare — duck typing.
"""
# Soltuion-> 
print("---------------------------")

class Notification:
    def send(self):
        pass

class Email(Notification):
    def __init__(self,email):
        self.email = email

    def send(self):
        return f"Your Mail => {self.email}"


class SMS(Notification):
    def __init__(self,sms):
        self.sms = sms

    def send(self):
        return f"Your sms => {self.sms}"

class Push(Notification):
    def __init__(self,push):
        self.push = push

    def send(self):
        return f"Your push / update msg => {self.push}"


def notify(obj):
    return obj.send()

print(f"{notify(Email("Interview date"))} , {notify(SMS("Book delivered"))}, {notify(Push("Vs code Update"))}")

# Question-> 
"""
7. Shape se teen classes banao —
   Triangle, Circle, Rectangle.
   Teeno ka area() constructor mein values lo.
   List mein sab daalo, loop mein 
   sabse bada area wala print karo.
   (Hint: max() use karo)
"""
# Soltuion-> 
print("---------------------------")
print("\nsol-1\n")

class Shape:
    def area(self):
        pass

class Triangle(Shape):
    def __init__(self,areas):
        self.areas = areas

    def area(self):
        return self.areas

class Circle(Shape):
    def __init__(self,areas):
        self.areas = areas

    def area(self):
        return self.areas

class Rectangle(Shape):
    def __init__(self,areas):
        self.areas = areas

    def area(self):
        return self.areas

shapes = [Triangle(230),Circle(203),Rectangle(304)]

area_value = [s.area() for s in shapes]

print(max(area_value))

# for s in shapes:
#     print(s.area())


print("\nsol-2\n")

class Shape:
    def area(self):
        pass

class Triangle(Shape):
    def __init__(self,base,height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self,heigth,width):
        self.heigth = heigth
        self.width = width

    def area(self):
        return self.heigth * self.width

shapes1 = [Triangle(2,4),Circle(4),Rectangle(3,5)]

max_value = max(shapes1, key=lambda s : s.area())

print(f"max value 1 => {max_value.area()}")

area_values = [s.area() for s in shapes1]
print(f"max value 2 => {max(area_values)}")


# Question-> 
"""
8. BankAccount class banao with method 
   transaction_info().
   SavingsAccount aur CurrentAccount inherit karein.
   SavingsAccount mein interest_rate = 4%,
   CurrentAccount mein overdraft_limit = 10000.
   Dono apna apna transaction_info() print karein.
"""
# Soltuion-> 
print("---------------------------")

class BankAccount:
    def transaction_info(self):
        pass


class SavingsAccount(BankAccount):
    def __init__(self):
        self.interest_rate = "4%"
    def transaction_info(self):
        return f"interest_rate : {self.interest_rate}"


class CurrentAccount(BankAccount):
    def __init__(self):
        self.overdraft_limit = 10000
    def transaction_info(self):
        return f"overdraft_limit : {self.overdraft_limit}"

account_details = [SavingsAccount(),CurrentAccount()]

for acc in account_details:
    print(acc.transaction_info())