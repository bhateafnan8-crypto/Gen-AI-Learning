def task():
    tasks = []
    print("-------Task Management------")

    totaltasks=int(input("Enter how many tasks you want to add ="))
    for i in range(1,totaltasks+1):
        taskname= input(f"Enter task {i} =")
        tasks.append(taskname)

    print(f"Today's tasks are \n{tasks}")

    while True:
        operation =int(input("Enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop/"))
        if operation == 1 :
            add = int(input("Enter your task ="))
            tasks.append(add)
            print(f"Task {add} Succesfully!!!")
        
        elif operation == 2:
            updated_value= input("Enter task you want to update =")
            if updated_value in tasks:
                up = input("Enter new task =")
                ind = tasks.index(updated_value)
                tasks[ind] = up
                print(f"Your Updated task {up}")

        elif operation == 3:
            del_value = input("Which task you want to delete =")
            if del_value in tasks:
                ind = tasks.index(del_value)
                del tasks[ind]
                print(f"Task {del_value} has been deleted...")

        elif operation == 4:
            print(f"Total tasks = {tasks}")
        
        elif operation == 5:
            print("Closing the program...")
            break
        else:
            print("Invalid Input")

task()