student_grade = { }

def add_student(name,grade):
    student_grade[name] = grade
    print(f"Added {name} with a {grade}")

def update_student(name,grade):
    if name in student_grade:
        student_grade[name]= grade
        print(f"{name} with marks are updated {grade}")
    else:
        print(f"{name} is not found")

def delete_student(name):
    if name in student_grade:
        del student_grade[name]
        print(f"{name} is deleted")

    else:
        print(f"{name} is not found")

def display_all_student():
    if student_grade:
        for name,grade in student_grade.items():
            print(f"{name} : {grade}")

    else:
        print("No student found")

def main():
    while  True:
        print("Student grade management")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View all Student")
        print("5. Exit")

        choice = int (input("Enter your choice = "))

        if choice == 1 :
            name = input("Enter Student name = ")
            grade = int(input("Enter student grade ="))
            add_student(name,grade)
        elif choice == 2:
            name = input("Enter Student name = ")
            grade = int(input("Enter student grade ="))
            update_student(name,grade)  
        elif choice == 3:
            name = input("Enter Student name = ")
            delete_student(name)
        elif choice == 4:
            display_all_student()
        elif choice == 5:
            print("Porgramming is closing")
            break
        else:
            print("Invalid choice")

main()