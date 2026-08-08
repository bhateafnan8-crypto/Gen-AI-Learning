"""
=== Student Grade Manager ===

Features:
  - Add student (naam + marks multiple subjects)
  - View all students (naam, average, pass/fail)
  - View single student detail
  - Save to file
  - Load from file on startup

---- Structure ----

Class: Student
  - Attributes: name, marks (list)
  - Method: calculate_average()
  - Method: is_pass()  → average >= 40 pass

Functions:
  - add_student()      → input naam + marks, Student object banao, list mein add karo
  - view_all()         → sab students loop karo, formatted print karo
  - view_student()     → naam se search, detail dikhao
  - save_to_file()     → file mein write karo
  - load_from_file()   → startup pe file se load karo
  - main()             → while loop + menu

---- Topics Covered ----
  - OOP         → Student class, methods
  - Lists       → marks list, students list
  - Dicts       → file save ke liye
  - Loops       → view, save, load
  - Conditionals → pass/fail
  - File handling → read/write
  - Error handling → invalid marks, file not found
  - String formatting → report display

---- Menu ----
  1) Add Student
  2) View All Students
  3) View Student Detail
  4) Save Data
  5) Exit

---- Flow ----
  Start → load_from_file() → main loop → user choice → action → repeat
  Exit pe automatically save karo ya option 4 se manually

---- Pass/Fail Rule ----
  Average >= 40 → Pass
  Average < 40  → Fail

"""



#code start here

# class creation

class Student:
    #instance attributes - constructor
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

# total marks calculation
    
    def totalmarks(self):
      totalmarksobtained = sum( mark["marks"] for mark in self.marks)
      return totalmarksobtained

# avrage marks calculation
     
    def averagemarks(self):
      max_marks = 75
      allsub_maxmarks = max_marks * 5

      total = self.totalmarks()
      average =( total / allsub_maxmarks ) * 100

      return average

# pass / fail checking

    def is_pass(self):
      avg = self.averagemarks()

      if avg < 40 :
          return "Fail"
      else:
          return "Pass"



# student list - empty list
students = []


# add student

def addstudent():

        name = input("Enter your full name => ").strip()

        if not name or name.isdigit():
            print("name should not be empty or numeric!!!")
            return

        marks_details = []

        for i in range(5):
            sub = input(f"Enter your sub #{i+1} => ").strip()
            if  not sub or sub.isdigit():
                print("sub should not be empty or numeric!!!")
                return
            try :
                    marks = int(input(f"Enter your marks for ({sub}) => "))
                    
            except ValueError:
                print("Marks should be a number!!")
                return

            marks_detail ={
                "subject":sub,
                "marks":marks
            }


            marks_details.append(marks_detail)

        details = Student(name,marks_details)

        students.append(details)
        
# View all student

def viewallstudent():
  if not students:
    print("There is no data to display!!")
    return

  for i,s in enumerate(students,start=1):
      print(f"student {i} : {s.name} ")
      for mark in s.marks:
          print(f"{mark['subject']} => {mark['marks']}")
      print(f"total => {s.totalmarks()} | average => {s.averagemarks()} | {s.is_pass()}")



# view student bye searchname
def viewsinglestudent():
    searchname = input("Enter name to search").strip()

    if not searchname or searchname.isdigit():
        print("name should not be empty or number !!!")
        return

    for i , s in enumerate(students,start= 1):
      if searchname.lower() == s.name.lower():
          print(f"student {i} : {s.name} ")
          for mark in s.marks:
            print(f"{mark['subject']} => {mark['marks']}")
          print(f"total => {s.totalmarks()} | average => {s.averagemarks()} | {s.is_pass()}")


# file save
     
def save_to_file():

    with open("student.txt","w") as file:

      for i , s in enumerate(students , start = 1 ):
        file.write(f"{i}. {s.name} |")

        for mark in s.marks:
          file.write(f"{mark['subject']} => {mark['marks']}")
        file.write(f"total => {s.totalmarks()} | average => {s.averagemarks()} | {s.is_pass()}")

        file.write("\n")
      
# file load

# def load_from_file():
#    try: 
#     with open("student.txt","r") as file:
#       content = file.read()
#       line =content.splitlines()
#       print(f"{line}")
#    except FileNotFoundError:
#       print("No saved file found. Starting fresh. ")


def load_from_file():
    try:
        with open("student.txt", "r") as file:
            content = file.read()
            lines = content.splitlines()

            for line in lines:
                if not line:
                    continue

                parts = line.split("|")
                name = parts[0].split(". ", 1)[1].strip()

                marks_data = []
                subject_marks = parts[1].split(" | ")

                for item in subject_marks:
                    if "total" in item or "average" in item or "Pass" in item or "Fail" in item:
                        continue

                    if " => " in item:
                        subject, mark = item.split(" => ")
                        marks_data.append({
                            "subject": subject.strip(),
                            "marks": int(mark.strip())
                        })

                student = Student(name, marks_data)
                students.append(student)

            print("Saved data loaded.")
    except FileNotFoundError:
        print("No saved file found. Starting fresh.")


# main execution
def main():
  load_from_file()
  while True:
      print("""
              === Student Grade Manager ===
              1) Add Student
              2) View All Students
              3) View Student Detail
              4) Save Data
              5) Exit
        """)

      choice = input("Enter your choice (1-5)=> ")

      if choice == "1":
          addstudent()
      elif choice == "2":
          viewallstudent()
      elif choice == "3":
          viewsinglestudent()
      elif choice == "4":
          save_to_file()
      elif choice == "5":
          print("Exiting the program!!")
          break
      else:
          print("Invalid choice!! , try again....")
  


# __name__ ==  "__main__"

if __name__  == "__main__":
    main()