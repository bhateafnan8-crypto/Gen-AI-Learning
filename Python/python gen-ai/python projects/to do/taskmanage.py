"""
=== CLI Todo Manager ===

Features:
  - Task add karo (title, priority)
  - All tasks view karo
  - Task complete mark karo
  - Task delete karo
  - Tasks CSV mein export karo

---- Structure ----

Class: Task
  - Attributes: id, title, priority, status (pending/done)
  - Method: display()

Class: TodoManager
  - Attribute: db connection
  - Method: add_task()
  - Method: view_tasks()
  - Method: complete_task()
  - Method: delete_task()
  - Method: export_csv()

Functions:
  - logger decorator → har operation log kare
  - main() → while loop + menu

---- Topics Covered ----
  - OOP         → 2 classes
  - SQLite      → CRUD operations
  - CSV         → export feature
  - Decorators  → @logger
  - Error handling → DB errors
  - List comprehensions → task filtering

---- Menu ----
  1) Add Task
  2) View All Tasks
  3) Complete Task
  4) Delete Task
  5) Export to CSV
  6) Exit

---- DB Schema ----
  tasks (id INTEGER PK, title TEXT, 
         priority TEXT, status TEXT)
"""

import sqlite3
import csv

# Task class handle formating display.. 
class Task:
  def __init__(self,id,title,priority,status="pending"):
    self.id = id
    self.title = title
    self.priority = priority
    self.status = status

  def display(self):
    print(f"{self.id}  {self.title} {self.priority} ({self.status}) ") 


# decorator logger 

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] {func.__name__} called")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} finished")
        return result
    return wrapper
# todo manager class handle all things database set to fetch...
class TodoManager:
  def __init__(self,db_name = "task.db"):
    self.conn = sqlite3.connect(db_name)
    self.cursor = self.conn.cursor()

    self.cursor.execute("""
      CREATE TABLE IF NOT EXISTS tasks (
      id INTEGER PRIMARY KEY AUTOINCREMENT, 
      title TEXT, 
      priority TEXT,
      status TEXT)
  """)


  
# add a task
  @logger
  def add_task(self):
    title = input("Enter your title : ")
    priority = input("Enter your priority :")
    status = "pending"

    self.cursor.execute("INSERT INTO tasks (title,priority,status) VALUES (?,?,?)",(title,priority,status))

    self.conn.commit()

# view all task
  @logger
  def view_tasks(self):
    self.cursor.execute("SELECT * FROM tasks")

    rows = self.cursor.fetchall()

    for row in rows:
      task = Task(row[0],row[1],row[2],row[3])
      task.display()

# complete task marking
  @logger
  def complete_task(self):
    statusid = input("Which task you want to mark as done (id) :")

    self.cursor.execute("UPDATE tasks SET status = ? WHERE id = ?",("done",statusid))
    if self.cursor.rowcount == 0:
      print("Task not found!")
    self.conn.commit()

# delete task
  @logger
  def delete_task(self):
    dltid = input("Which task you want to mark as done (id) :")
    
    self.cursor.execute("DELETE FROM tasks WHERE id = ?",(dltid,))
    if self.cursor.rowcount == 0:
      print("Task not found!")
    self.conn.commit()

#  export to csv
  @logger
  def export_csv(self):
    self.cursor.execute("SELECT * FROM tasks")

    rows = self.cursor.fetchall()

    filename = input("Enter only filname you want save no extension (.csv only set bydefault): ")
    with open(filename+".csv","w",newline="") as file:
      writer =csv.writer(file)
      writer.writerow(["id","title","priority","status"])
      for row in rows:
        writer.writerow(row)

    # self.status = "Done"
    # self.status = status


#  main function running
def main():
  todo = TodoManager()
  while True:
      
    print(""" ======= TODO MANAGER =======
        ---- Menu ----
          1) Add Task
          2) View All Tasks
          3) Complete Task
          4) Delete Task
          5) Export to CSV
          6) Exit
    """)

    choice = input("Enter your choice : ")

    if choice == "1":
      todo.add_task()
    elif choice == "2":
      todo.view_tasks()
    elif choice == "3":
      todo.complete_task()
    elif choice == "4":
      todo.delete_task()
    elif choice == "5":
      todo.export_csv()
    elif choice =="6":
      print("Exitng the program ...")
      break
    else:
      print("Invalid choice. Try again!")


# __name__ == "__main__" calling
if __name__ == "__main__":
  main()

  # taskmanage.py