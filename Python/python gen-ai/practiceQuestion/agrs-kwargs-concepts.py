# Normal function — fixed arguments
def add(a, b):
    return a + b

print(add(10,20))
# *args — kitne bhi positional arguments lo
def add(*args):
    return sum(args)

print(add(1, 2, 3, 4) ) # → 10

# **kwargs — kitne bhi keyword arguments lo
def show(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} => {value}")

show(name="Afnan", city="Mumbai")