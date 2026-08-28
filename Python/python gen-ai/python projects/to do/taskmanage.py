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

