"""
    === Student management Application ===
        - Where we can 
            - Add Student
            - View Student
            - Delete task (optional)
            - Search task (optional)
            - Compare marks

"""
#    code start here

# === class definition
class studentManager():
    # instance attributes
    def __init__(self,name,roll_no ,marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks


    # magic - dunder methods
    def __str__(self):
        return f"{self.name} => roll_no : ({self.roll_no}) => marks : {self.marks}"
    
    def __lt__(self, other):
        return self.marks < other.marks

    def __eq__(self, other):
        return self.marks == other.marks


# list creation for store student detaisls

students_details = []

# add student 

def addStudent():
    name = input("Enter name =>")
    roll_no = input("Enter roll no =>")
    try:
        marks = float(input("Enter marks =>"))
    except ValueError:
        print("marks should be only number!!")
        return
    student = studentManager(name,roll_no,marks);
    students_details.append(student)



# display student 
    
def displayStudent():
    if not students_details:
        print("students not found !!")
        return

    for s in students_details:
        print(s)

    print()

def compareStudent():
    if len(students_details) < 2:
        print("minimum 2 Students should be added !!\n" )
        return

    else:
        print("\n!! Comparing students marks !!\n")
        s1,s2 = students_details[0],students_details[1]

        print(f"student 1 => {s1}")
        print(f"student 2 => {s2}")

        if s1 > s2 :
            print (f"\n{s1.name} has scored more than {s2.name}")
        elif s2 > s1:
            print (f"\n{s2.name} has scored more than {s1.name}")
        else:
            print (f"\n{s2.name} and {s1.name} has scored equal marks")
            

def menu():
    while True:
        print("""
    === Student management Application ===
            1. Add Student
            2. View Student
            3. Compare marks
            4. Exit
""")
        print("type exit to quit the program !!")

        choice = input("Enter your choice =>")

        if choice == "1":
            addStudent()
        elif choice == "2":
            displayStudent()
        elif choice == "3":
            compareStudent()
        elif choice == "4":
            print("\n Exiting program ! Good bye")
            break
        else:
            print(" ! Invalid choice ! , try again!")


#menu call here or run
if  __name__ =="__main__" :
    menu()

