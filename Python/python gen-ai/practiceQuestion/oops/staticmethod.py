# Question-> 
"""
1. Create a class Geometry with static methods: area_of_circle(radius) and area_of_square(side).
"""
# Soltuion-> 
print("---------------------------")
class Geometry:
    #constructor -> instance method
    def __init__(self):
        self.aoc = Geometry.area_of_circle(4)
        self.aos = Geometry.area_of_square(4)

    @staticmethod
    def area_of_circle(radius):
        return (radius**2)*3.14
    
    def area_of_square(side):
        return side ** 2
    
# print(Geometry.area_of_circle(4))
# print(Geometry.area_of_square(4))
geometry1 = Geometry()
print(f"area of circle => {geometry1.aoc} || area of square => {geometry1.aos}")





# Question-> 
"""
2. Create a class Validator with a static method is_valid_email(email) that checks if @ is present.
"""
# Soltuion-> 
print("---------------------------")

class Validator:
    # instance attribute - constructor
    def __init__(self):
        self.email = Validator.is_valid_email("Adfar@gmail.com")

    @staticmethod
    def  is_valid_email(email):
        if "@" in email:
            return email
        else:
            return "Invalid email"

print(Validator.is_valid_email("Adfargmail.com"))
email1 = Validator()

print(f"Email 1 validation => {email1.email}")




# Question-> 
"""
3. Modify your previous OOP mini project and add one static method for a utility operation (e.g., formatting, cleaning input, etc.).
"""
# Soltuion-> 
print("---------------------------")

class Validators:
    # instance attribute - constructor
    def __init__(self):
        self.email = Validators.is_valid_email(Validators.format_text("Adfar@gmail.com"))
    
    @staticmethod

    def format_text(email):
        text = email.strip()
        lowertext = text.lower()
        return lowertext

    @staticmethod
    
    def  is_valid_email(email):
        if "@" in email:
            return email
        else:
            return "Invalid email"

print(Validators.is_valid_email(Validators.format_text("Adfargmail.com")))
email1 = Validators()

print(f"Email 1 validation => {email1.email}")


