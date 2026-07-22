"""
menu = []

user = input("Enter stock: ")

# Add stock to the list
menu.append(user)

# Check if list is full
if len(menu) > 5:
    print("There is no space left")
else:
    print("Current menu:", menu)

    menu = []

while len(menu) < 5:
    user = input("Enter stock (or type 'stop' to finish): ")
    if user.lower() == 'stop':
        break
    menu.append(user)

if len(menu) >= 5:
    print("There is no space left!")

print("Final menu:", menu)
"""

my_contact = {
    "Afnan":90822,
    "iesa":99665
}

print(my_contact)

my_contact[input("Enter Name:")] = input("Enter Number")
print(my_contact)

del my_contact[input("Enter Name or number:")]
if my_contact == my_contact:
    print("deleted succesfully!")
else:
    print("Invalid Name or number ")   