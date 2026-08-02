# Question-> 
'''
🔹 1. Create a Movie class
Attributes: title, genre, rating
Method: display_info() → prints movie details
'''
# Soltuion-> 
print("---------------------------")
class movie():
    # instence attirbutes
    def __init__(self,title, genre, rating):
        self.title = title
        self.genre = genre
        self.rating = rating
        

    # methods
    def display_info(self):
        print(f"Title: {self.title} :: genre: {self.genre} :: rating: {self.rating}")

movie1 = movie("Dhamaal","Comedy",5)
movie2 = movie("Family Star","Money",4.5)

movie1.display_info()
movie2.display_info()




# Question-> 
'''
🔹 2. Create a TemperatureConverter class
Attribute: celsius
Methods: to_fahrenheit(), to_kelvin()
'''
# Soltuion-> 
print("---------------------------")
class TemperatureConverter():
    #instence attributes
    def __init__(self,celsius):
        self.celsius = celsius


    # methods
    def to_fahrenheit(self):
        F = (self.celsius * 1.8) + 32
        print(f"celcius to fahrenheit => {self.celsius}°C to {F}°F")
    
    def to_kelvin(self):
        K = self.celsius + 273.15
        print(f"celcius to Kelvin => {self.celsius }°C to {K}°K")
temp1 = TemperatureConverter(20)
temp2 = TemperatureConverter(30)

temp1.to_fahrenheit()
temp2.to_fahrenheit()
temp1.to_kelvin()
temp2.to_kelvin()




# Question-> 
'''
🔹 3. Create a ShoppingItem class
Attributes: name, price, quantity
Method: total_price() → returns price * quantity
'''
# Soltuion-> 
print("---------------------------")

class ShoppingItem():
    #instence attributes
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


    # methods
    def total_price(self):
        return  self.price * self.quantity

cart1  = ShoppingItem("Bags",1400,2)

print(f"cart1 => {cart1.name} <=> {cart1.price} * {cart1.quantity} <=>{cart1.total_price()}")