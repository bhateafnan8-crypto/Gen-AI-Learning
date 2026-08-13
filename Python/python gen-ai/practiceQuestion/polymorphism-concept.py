# Same method naam, alag alag class mein alag behaviour
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

# Polymorphism — same function call, alag output
animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())