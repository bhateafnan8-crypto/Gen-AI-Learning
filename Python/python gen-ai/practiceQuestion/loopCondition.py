# Question-> 
'''
1. Write a program to check if a number is even or odd using if-else.
'''
# Soltuion-> 
print("---------------------------")
i = 3
if i %2 == 0:
    print(f"even or odd ->> {i} is even")
else:
    print(f"even or odd ->> {i} is odd")


# Question-> 
'''
2. Loop through numbers 1 to 10 and print only even numbers using continue.
'''
# Soltuion-> 
print("---------------------------")
for i in range(1,11):
    if i % 2 !=0:
        continue
    else:
        print(f"even numbers-> {i}")


# Question-> 
'''
3. Ask the user to guess a number between 1–5. Keep asking until the guess is correct (use while and break).
'''
# Soltuion-> 
print("---------------------------")
while True:
    numberInp = int(input("Guess a number between 1-5 to match with fixed number ->>"))
    if numberInp == 5:
        print("---------------------------")
        print(f"You entered {numberInp} is  matched!")
        print("---------------------------")
        break
    print("---------------------------")
    print(f"You entered {numberInp} is not matched try again!")
    print("---------------------------")

    


# Question-> 
'''
4. Use a for loop to calculate the sum of all numbers between 1 and 100.
'''
# Soltuion-> 
print("---------------------------")
add = 0
for i in range(1,101):
    add += i
print(f"sum of all numbers 1-100 ->> {add}")


# Question-> 
'''
5. Write a program to count how many vowels are in a given string using a for loop.
'''
# Soltuion-> 
print("---------------------------")
vowels = ["a","e","i","o","u","A","E","I","O","U"]
string = input("Enter a string ->> ")
count = 0
for i in string:
    if i in vowels:
        count+=1
print(f"count of vowels ->> {count}")



# Question-> 
'''
6. BONUS: Create a simple login system:
Username: "admin"
Password: "1234"
Allow user 3 attempts. If correct, print "Login successful", else "Account locked".
'''
# Soltuion-> 
print("---------------------------")
Username = "admin"
Password = "1234"
attempts = 3
count = 0
print(f"username {Username} and password {Password} and attempts {attempts}")

print("---------------------------")


while True:
    uname = input("Enter username ->>")
    passw = input("Enter password ->>")
    unameLenght = len(uname)
    passwLenght = len(passw)
    if uname != Username and passw != Password:
        count +=1
        if count == attempts:
            print(f"your account blocked!") 
            break
    else:
        print(f"Succesfull login!")
        break
   
