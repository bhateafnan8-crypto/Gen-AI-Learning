# Question-> 
'''
1. __str__ Practice -> Create a Movie class that returns a nice string like:
    movie = Movie("Inception", "Sci-Fi")
    print(movie)  # Inception (Sci-Fi)
'''
# Soltuion-> 
print("---------------------------")
class Movie():
    # instence attributes
    def __init__(self,title,genre):
        self.title = title
        self.genre = genre

    # dunder method - magic method
    def __str__(self):
        return f"{self.title} ({self.genre})"

movie = Movie("Inception", "Sci-Fi")
print(movie)




# Question-> 
'''
2. __add__ Practice -> Create a Time class with hours and minutes. Use __add__ to add two time objects properly.
'''
# Soltuion-> 
print("---------------------------")
class Time():
    #instence attributes
    def __init__(self,H,M):
        self.H = H
        self.M = M


    # dunder method - magic method
    def __add__(self, other):
        total_H = self.H + other.H
        total_M = self.M + other.M

        if total_M >= 60:
            total_H += total_M // 60
            total_M += total_M % 60

        return Time(total_H,total_M)

    def __str__(self):
        return f"{self.H} hours : {self.M} minutes"

t1 = Time(2,10)
t2 = Time(1,35)

print(t1+t2)



# Question-> 
'''
3. __len__ and __getitem__ -> Create a ShoppingList class with items. Implement:

__len__() so len(shopping_list) works
__getitem__() so shopping_list[0] works
'''
# Soltuion-> 
print("---------------------------")

class ShoppingList():
    #instence attributes
    def __init__(self):
        self.items = ["Car","Bag","Pencil","Compass"]

    # dunder method - magic method
    def __len__(self):
        return len(self.items)

    def __getitem__(self, key):
        return self.items[key]

    def __str__(self):
        return f"list {self.items} || lenght => {len(self)} || index => {self[0]}"

cart1 = ShoppingList()

print(f"Cart => {cart1}")