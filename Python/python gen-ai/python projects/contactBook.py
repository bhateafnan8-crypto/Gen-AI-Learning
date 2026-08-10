"""
=== Contact Book ===

Features:
  - Add contact (naam, phone, email)
  - View all contacts
  - Search contact by name
  - Delete contact by name
  - Save to file
  - Load from file on startup

---- Structure ----

Class: Contact
  - Attributes: name, phone, email
  - Method: display()  → formatted print kare

Functions:
  - add_contact()       → input lo, Contact object banao, list mein add karo
  - view_all()          → sab contacts loop karo, formatted print karo
  - search_contact()    → naam se search, detail dikhao
  - delete_contact()    → naam se search, list se remove karo
  - save_to_file()      → file mein write karo
  - load_from_file()    → startup pe file se load karo
  - main()              → while loop + menu

---- Topics Covered ----
  - OOP         → Contact class, display method
  - Lists       → contacts list
  - Loops       → view, search, delete
  - Conditionals → search/delete match check
  - File handling → read/write
  - Error handling → empty input, file not found
  - String formatting → display output

---- Menu ----
  1) Add Contact
  2) View All Contacts
  3) Search Contact
  4) Delete Contact
  5) Save Data
  6) Exit

---- Flow ----
  Start → load_from_file() → main loop → user choice → action → repeat

---- Validation Rules ----
  Name   → empty nahi, digits nahi
  Phone  → empty nahi, digits only (isdigit())
  Email  → empty nahi, "@" hona chahiye
"""