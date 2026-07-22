import random

easy_level = ["Abc123", "abc123", "ABC123"]
medium_level = ["aBc232", "ABc444", "bcb566"]
hard_level = ["Abc@333", "Ab#44c", "bh&g232"]

print("Welcome to the Password Guessing Game!")
print("Choose your difficulty level (easy, medium, or hard)")

level = input("Enter your difficulty level: ").lower()

if level == "easy":
    secret = random.choice(easy_level)
elif level == "medium":
    secret = random.choice(medium_level)
elif level == "hard":
    secret = random.choice(hard_level)
else:
    print("Invalid choice > Defaulted to easy level")
    secret = random.choice(easy_level)

attempts = 0
print("\nGuess the password!")

while True:
    guess = input("Enter your guess: ")
    attempts += 1

    if guess == secret:
        print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
        break

    # Generate hint
    hint = ""
    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        else:
            hint += "_"

    print("Hint:", hint)
print("Game Over!") 







"""import random

easy_level = ["Abc123","abc123","ABC123"]
medium_level=["aBc232","ABc444","bcb566"]
Hard_level=["Abc@333","Ab#44c","bh&g232"]

print("Welcome to Password guessing game!")
print("Choose your difficulty level (easy, medium or hard)")

level = input("Enter your difficulty level: ").lower()

if level == "easy":
    secret = random.choice(easy_level)
elif level == "medium":
    secret = random.choice(medium_level)
elif level == "hard":
    secret = random.choice(Hard_level)
else:
    print("Invalid choice > Defulted to easy level")
    secret = random.choice(easy_level)

attempts = 0
print("\n Guess the password")

while True:
    guess = input("Enter you guess:").lower()
    attempts += 1

    if guess == secret:
        print(f"Congratualation! you guessed it in {attempts}  attempts.")
        break
    hint = ""

    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        else:
            hint +="_"

        print("Hint: ",hint)
print("Game Over") """
