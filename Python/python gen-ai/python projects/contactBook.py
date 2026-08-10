"""
=== Contact Book ===

Features:
  - Add contact (naam, phone, email)
  - View all contacts
  - Search contact by name
  - Delete contact by name
  - Save to file
  - Load from file on startup

---- Structure ----

Class: Contact
  - Attributes: name, phone, email
  - Method: display()  → formatted print kare

Functions:
  - add_contact()       → input lo, Contact object banao, list mein add karo
  - view_all()          → sab contacts loop karo, formatted print karo
  - search_contact()    → naam se search, detail dikhao
  - delete_contact()    → naam se search, list se remove karo
  - save_to_file()      → file mein write karo
  - load_from_file()    → startup pe file se load karo
  - main()              → while loop + menu

---- Topics Covered ----
  - OOP         → Contact class, display method
  - Lists       → contacts list
  - Loops       → view, search, delete
  - Conditionals → search/delete match check
  - File handling → read/write
  - Error handling → empty input, file not found
  - String formatting → display output

---- Menu ----
  1) Add Contact
  2) View All Contacts
  3) Search Contact
  4) Delete Contact
  5) Save Data
  6) Exit

---- Flow ----
  Start → load_from_file() → main loop → user choice → action → repeat

---- Validation Rules ----
  Name   → empty nahi, digits nahi
  Phone  → empty nahi, digits only (isdigit())
  Email  → empty nahi, "@" hona chahiye
"""



# Code start here

# class creation
class ContactBook:
    # instance attribute - Constuctor
    def __init__(self,name,phone,email):
        self.name = name
        self.phone = phone
        self.email = email

    # method to display contact details - Helper method
    def display(self):
        print(f"{self.name} => {self.phone} | {self.email}")

# functions - to perform operations or main tasks 


# list creation to store contact details - empty list

contacts = []

# add contact 

def add_contact():
  name = input("Enter your name => ").strip()
  phone = input("Enter your phone number => ").strip()
  email = input("Enter your email id => ").strip()

  if not name or any(ch.isdigit() for ch in name):
      print("name should not be empty or number...")
      return
  if not phone or not phone.isdigit():
      print("phone number should not be empty not character...")
      return
  if not email or email.isdigit() or "@" not in email:
      print("email should not be empty or number or @ required...")
      return
  
  if any(c.phone == phone for c in contacts):
    print("phone number already exist...") 
    return
  if  any(c.email == email for c in contacts):
    print("email id  already exist...")
    return
      
  contacts.append(ContactBook(name,phone,email))


# view all contact

def viewall_contact():
  if not contacts:
        print("There is no data to display.....")
        return

  for i , c in enumerate(contacts, start=1):
     print(f"{i}. ",end="")
     c.display()

# Search contact by name

def search_contact():
  searchcontact = input("Enter name to search contact => ").strip()

  if not searchcontact or searchcontact.isdigit():
      print("searchcontact should not be empty or numeric...")
      return

  for i , c in enumerate(contacts,start=1):
    if searchcontact.lower() == c.name.lower():
       print(f"{i}. ",end="")
       c.display()
       break
  else:
     print("Contact not found")

# Delete contact by name

def delete_contact():
  searchcontact = input("Enter name to search contact => ").strip()

  if not searchcontact or searchcontact.isdigit():
      print("searchcontact should not be empty or numeric...")
      return

  for i , c in enumerate(contacts,start=1):
    if searchcontact.lower() == c.name.lower():
       contacts.remove(c)
       print(f"{i}.{searchcontact} delted successfully... ")
       break
  else:
     print("Contact not found....")

# save to file

def save_to_file():
   with open("contact.txt","w") as file:
    for i , c in enumerate(contacts,start=1):
      file.write(f"{i}. {c.name} => {c.phone} | {c.email}\n")
   print("Contacts Saved successfully...")

# load data from file

def load_from_file():
  try:
    with open("contact.txt","r") as file:
        content = file.read()
        lines = content.splitlines()

        for line in lines:
           if not line:
              continue

           parts = line.split(" => ")

           name = parts[0].split(". ", 1)[1].strip()

           phone, email = parts[1].split(" | ",1)

           phone = phone.strip()
           email = email.strip()

           contacts.append(ContactBook(name,phone,email))

  except FileNotFoundError:
      print("No saved file found. Starting fresh.")
  else:
    print("Contacts Load successfully...")
     
# main program execution
def main():
  load_from_file()
  while True:
      print("""
              === Cotact Book Manager ===
               1) Add Contact
               2) View All Contacts
               3) Search Contact
               4) Delete Contact
               5) Save Data
               6) Exit
        """)

      choice = input("Enter your choice (1-6)=> ")

      if choice == "1":
          add_contact()
      elif choice == "2":
          viewall_contact()
      elif choice == "3":
          search_contact()
      elif choice == "4":
          delete_contact()
      elif choice == "5":
         save_to_file()
      elif choice == "6":
          print("Exiting the program!!")
          break
      else:
          print("Invalid choice!! , try again....")
    
  
# __name__ == "__main__" .. calling 

if __name__ == "__main__":
   main()









# galat logic mene socha tha lekin galat nikla 
# 1. loop for contact view all -  isme mene classname se call kardiya jo galat hai meko object se call karna tha jisse wo self chale aur data show ho sake
  # for i , c in enumerate(contacts, start=1):
  #    print(f"{i}. {ContactBook.display()}") 
  
# 2. 

  # Functions:
  # - add_contact()       → input lo, Contact object banao, list mein add karo
  # - view_all()          → sab contacts loop karo, formatted print karo
  # - search_contact()    → naam se search, detail dikhao
  # - delete_contact()    → naam se search, list se remove karo
  # - save_to_file()      → file mein write karo
  # - load_from_file()    → startup pe file se load karo
  # - main()