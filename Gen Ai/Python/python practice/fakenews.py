import random

subjects = [
    "Riya",
    "Arjun",
    "Sneha",
    "Rohit",
    "Priya",
    "Aman",
    "Kavita",
    "Deepak",
    "Meena",
    "Vikram"
]


Actions = [
    "Eats",
    "Sleep on",
    "Plays",
    "Dance with",
    "Run",
    "Reads",
    "Fight with"

]

Places_Things=[
    "Sation",
    "Fruits",
    "Mumbai",
    "Stage",
    "Station",
    "Bed",
    "Fast",
    "Leader",
    "on track",

]

while True:
    sub = random.choice(subjects)
    act = random.choice(Actions)
    place_thing = random.choice(Places_Things)

    news = f"Breaking News : {sub} {act} {place_thing}"
    print("\n",news)

    user_in = input("DO you want more?(yes/no):").strip().lower()
    if user_in == "no":
        break
    
print("Have a great day!")