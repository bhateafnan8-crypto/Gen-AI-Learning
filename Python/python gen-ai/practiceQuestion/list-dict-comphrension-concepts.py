print("====  list comphrension ==== \n \n ")

li = []

for i in range(20):
    li.append(i * i)

print(f"\nfirst list simple for loop => {li}\n")


li1 = [i * i for i in range(10)]

print(f"\nsecond list using list comphrension => {li1} \n")


a = []

for i in range(10):
    if i % 2 == 0:
        a.append(i)

print(f"\nthird list even number using simple for loop => {a}\n")

b = [i for i in range(20) if i % 2 == 0]
print(f"\nthird list even number using list comphrension => {b}\n")




print("\n \n ====  dictionary comphrension ====\n \n")


dic = {x: x * x for x in range(10)}

print(f"dict comphrension for square => {dic}\n")