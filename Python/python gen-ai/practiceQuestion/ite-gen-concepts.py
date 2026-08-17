# Iterator — manually
class Counter:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.limit:
            raise StopIteration
        self.current += 1
        return self.current

for num in Counter(3):
    print(num)  # 1, 2, 3

# Generator — yield use karta hai, simple aur clean
def counter(limit):
    for i in range(1, limit + 1):
        yield i

for num in counter(3):
    print(num)  # 1, 2, 3



# ite-gen-concepts.py