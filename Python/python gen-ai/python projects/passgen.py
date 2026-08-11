"""
=== Password Generator + Strength Checker ===

Features:
  - User parameters se password generate karo
  - Generated password ki strength check karo
  - Result display karo

---- Structure ----

Functions:
  - get_parameters()      → user se length, numbers, special chars lo
  - generate_password()   → parameters ke basis pe password banao
  - check_strength()      → password strength check karo (weak/medium/strong)
  - display_result()      → password aur strength formatted print karo
  - main()                → while loop + menu

---- Topics Covered ----
  - Functions       → har operation alag function
  - Strings         → password build karna, character check
  - Sets            → character pool banana
  - Loops           → password characters pick karna
  - Conditionals    → strength check logic
  - Error handling  → invalid length input
  - import          → random, string modules

---- Menu ----
  1) Generate Password
  2) Exit

---- Flow ----
  main() → user choice → get_parameters() → generate_password() 
         → check_strength() → display_result() → repeat

---- Strength Rules ----
  Weak   → length < 8  ya sirf letters
  Medium → length 8-12, numbers ya special chars mein se ek
  Strong → length > 12, numbers aur special chars dono

---- Validation Rules ----
  Length     → number hona chahiye, minimum 4
  Parameters → kam se kam ek character type selected hona chahiye
"""



import random
import string

# Take Inputs from user as a parameters and check validation
def get_parameters():
    while True:
      try:
        pass_length = int(input("Enter length of password (min-4) => "))

        if pass_length < 4:
            print("Minimum password length required is 4...")
            continue
        break
        
      except ValueError:
         print("Length should be a number...")

    pass_number = input("You want numbers in password?  (y,n) => ").strip().lower() == "y"
    pass_special_char = input("You want special characters in password? (y,n) => ").strip().lower() =="y"

    if  not pass_number and pass_special_char:
      print("Minimum one character type  requied... ")
      return get_parameters()

    return pass_length,pass_number,pass_special_char



# Password genration based on inputs and validation using random and string module

def generate_password(length, pass_number , pass_special_char):
    pass_char = string.ascii_letters

    if pass_number :
       pass_char  += string.digits
    if pass_special_char:
       pass_char += string.punctuation

    password = []

    for _ in range(length):
       password.append(random.choice(pass_char))

    return "".join(password)


# password strength checking - weak , medium , strong 

def check_strength(password):

  # has_letter = any(char.isalpha() for char in password)
  has_number = any(char.isdigit() for char in password)
  has_special_char = any(not char.isalnum() for char in password)

  if len(password) < 8 or (not has_number and not has_special_char):
   return "Weak"

  if  8 <= len(password) <= 12 and (has_number or has_special_char):
   return "Medium"

  if len(password) > 12 and has_number and has_special_char:
   return "Strong"
  
  return "Medium"



# display the passwordd based on inputs and validation

def display_result(password,strength):

   print(f"\n Genrated password => {password} | Strength => {strength}")


# main code execution
def main():
   while True:
      print("""   === Password Generator + Strength Checker ===
                  1) Generate Password
                  2) Exit
      """)

      choice = input("Enter your choice (1-2) => ")

      if choice == "1":
         parameters = get_parameters()
         length,pass_number,pass_special_char = parameters
         password =  generate_password(length, pass_number , pass_special_char)
         strength = check_strength(password)
         display_result(password,strength)
      elif choice == "2":
         print("Exiting program...")
         break
      else:
         print("Invalid choice ... try again!")




# __name__ == "__main__"

if __name__ == "__main__" :
   main()








# galat logic .. password generate ka galat logic
# def generate_password():

  #  letters = string.ascii_letters

  #  numbers = string.digits

  #  special_char = string.punctuation

  #  password = letters + numbers + special_char

  #  pass_gen = random(password)
 

         
         
