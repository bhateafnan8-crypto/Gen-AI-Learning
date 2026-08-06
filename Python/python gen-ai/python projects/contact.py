"""
    === Contact manager Application ===
        - Where we can 
            - Add Contact
            - View Contact
            - Delete Contact
            - Search Contact

"""

# code start here 


#Define list - empty list
Contacts = []

#1. Add contact
def add_contact():
    name = input("Enter your name ->>")
    phone = int(input("Enter your phont number ->>"))
    email =  input("Enter your email-id ->>")

    contact_info ={
        "name": name,
        "phone":phone,
        "email":email
    }

    Contacts.append(contact_info)

    print(f"your {name} - details added successfully!!\n")



#2. View contact
def view_contact():
    if not Contacts:
        print("Contact not found to show !\n")
        return
    print("\n==== Contact List ====")
    for i,c in enumerate(Contacts,start=1):
        print(f"{i}. {c["name"]}  | {c["phone"] } | {c["email"]}")



#3. Delete contact
def delete_contact(searchname):
    if searchname.isdigit():
        print("Invalid name only string name -->\n")
        return
    for member in Contacts:
        if member["name"].lower() == searchname.lower():
            Contacts.remove(member)
            print(f"contact {searchname} -> deleted succesfully !!\n")
            return
    print(F"contact for {searchname} not found !!\n")




#4 .Search contact
def search_contact(searchname):
    if searchname.isdigit():
        print("Invalid name only string name -->\n")
        return
    for member in Contacts:
        if member["name"].lower() == searchname.lower():
            print(f"found {member["name"]} | {member["phone"]} | {member["email"]}\n")
            return
    print(F"contact for {searchname} not found !!\n")



# main execution
while True:
    print("""
        === Contact Manager Application ===
        1. Add Task
        2. View Task
        3. Delete Task
        4. Search Task
        5. Exit
    """  )

    choice = input("Enter your choice ->>")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contact()
    elif choice == "3":
        searchname = input("Enter name to delete ->> ")
        delete_contact(searchname)
    elif choice == "4":
        searchname = input("Enter name to search ->> ")
        search_contact(searchname)
    elif choice == "5":
        print("Exiting Application -> Good Bye!!")
        break
    else:
        print("Invalide choice -> try again!!")