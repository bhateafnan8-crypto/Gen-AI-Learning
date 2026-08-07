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