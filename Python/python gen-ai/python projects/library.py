"""
=== Library Book Manager ===

Features:
  - Book add karo library mein
  - All books view karo
  - Book issue karo (available → issued)
  - Book return karo (issued → available)
  - Save to file
  - Load from file on startup

---- Structure ----

Class: Book
  - Attributes: title, author, is_available (True/False)
  - Method: display()  → formatted print kare

Class: Library
  - Attribute: books (list)
  - Method: add_book()      → Book object banao, list mein add karo
  - Method: view_books()    → sab books dikhao
  - Method: issue_book()    → title se search, is_available = False karo
  - Method: return_book()   → title se search, is_available = True karo
  - Method: save_to_file()  → file mein write karo
  - Method: load_from_file() → file se load karo

Functions:
  - main()  → while loop + menu

---- Topics Covered ----
  - OOP         → 2 classes, methods, attributes
  - Encapsulation → data aur methods ek class mein
  - Abstraction  → Library class andar ka logic hide karta hai
  - Lists        → books collection
  - Loops        → view, search
  - Conditionals → available check, search match
  - File handling → read/write
  - Error handling → file not found, book not found

---- Menu ----
  1) Add Book
  2) View All Books
  3) Issue Book
  4) Return Book
  5) Save Data
  6) Exit

---- Flow ----
  Start → load_from_file() → main loop → user choice → action → repeat

---- Validation Rules ----
  Title  → empty nahi, digits nahi
  Author → empty nahi, digits nahi
  Issue  →
"""