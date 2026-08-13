# Question-> 
"""
1. Shape class banao with method area().
   Circle aur Rectangle — dono inherit karein 
   aur apna apna area() calculate karein.
"""
# Soltuion-> 
print("---------------------------")

class shape:
    def area(self):
        return "shape area"

class circle(shape):
    def area(self,r):
        return f"circle area => {r*r*3.14}"

class rectangle(shape):
    def area(self,side):
        return f"rectangle area => {side*side}"

shapes = [circle(),rectangle()]

for shape1 in shapes:
    print(shape1.area())

    
# Question-> 
"""
2. Animal class banao with method sound().
   Dog, Cat, Cow — teeno override karein.
   Ek loop mein sab ka sound print karo.
"""
# Soltuion-> 
print("---------------------------")



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