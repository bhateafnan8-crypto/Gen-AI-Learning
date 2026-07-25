"""
    === To Do  List / Task manager Application ===
        - Where we can 
            - Add task
            - View task
            - Delete task
            - Search task
            - Status update (completed - pending)

"""

# code start here 

# Define list & set - empty list & set
Tasks = []
Completed_task = set()

# 1. add task
def add_task():
    task = input("Enter your task here to add ->>")
    Tasks.append(task)
    print(f"your task <- {task} -> added successfully!!\n")

# 2.  View task
def view_task():
    if not Tasks:
        print("Tasks not found to display\n")
        return
    print("\n===== TO-DO LIST =====")
    for i,t in enumerate(Tasks, start=1):
        status = "✅ Completed" if t in Completed_task else "Pendng"
        print(f"{i}. {t} - {status}\n")

# 3. Status update (completed - pending)
def completed_task(task_id):
    if 1 <= task_id <= len(Tasks):
        task = Tasks[task_id - 1]
        Completed_task.add(task)
        print(f"Task  ' {task} ' marked as Completed ✅\n")
    else:
        print("Invalid task_id , try again!")

# 4 .Delete task
def delete_task(task_id):
    if 1 <= task_id <= len(Tasks):
        task = Tasks.pop(task_id - 1)
        Completed_task.discard(task)
        print(f"Task ' {task} ' deleted successfully!!\n")
    else:
        print("Invalid task_id , try again!")

# 5. Search task
def search_task(task_id):
    if 1 <= task_id <= len(Tasks):
        task = Tasks[task_id - 1]
        status = "✅ Completed" if task in Completed_task else "Pendng"
        print(f"{task_id}. {task} - {status}\n")


# main execution --
while True:
    print("""
        === Task Manager Application ===
        1. Add Task
        2. View Task
        3. Status update(completed)
        4. Delete Task
        5. Search Task
        6. Exit
    """  )

    choice = input("Enter your choice (1-6) ->> ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_task()
    elif choice == "3":
        task_id = int(input("Enter your task id ->> "))
        completed_task(task_id)
    elif choice == "4":
        task_id = int(input("Enter your task id ->> "))
        delete_task(task_id)
    elif choice == "5":
        task_id = int(input("Enter your task id ->> "))
        search_task(task_id)
    elif choice == "6":
        print("Exiting application - Good Bye !")
        break
    else:
        print("Invalid choice , try again")