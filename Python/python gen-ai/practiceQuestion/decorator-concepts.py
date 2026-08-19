# Decorator — ek function jo doosre function ko wrap karta hai
def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@my_decorator
def greet():
    print("Hello")

greet()
# Before
# Hello
# After


# decorator-concepts.py