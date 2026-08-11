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


# code start here


# class creation - Book

class Book:
  # isntance attribute - Constructor

  def __init__(self,title , author , is_available ):
      self.title = title
      self.author = author
      self.is_available = is_available

  # method - to display formatted text 

  def display(self):
      print(f"{self.title} written by {self.author} availability : {self.is_available}")

# class creation - Library

class Library:
  # isntance attribute - Constructor

  def __init__(self):
      self.books = []
    
  # methods - to pefrom operations 

  # add book
  def add_book(self):
    title = input("Enter book title => ").strip()
    author = input("Enter book author => ").strip()
    is_available = input("Enter book availability (yes/no) => ").strip().lower() in ("yes", "y", "true", "1")

    
    if not title or title.isdigit():
        print("Title should not be empty or number ...")
        return
    if not author or author.isdigit():
        print("Autor should not be empty or number ...")
        return
    

    self.books.append(Book(title,author,is_available))

  #  view all books
  def view_books(self):
      if not self.books:
          print("There is no books ")
          return

      for i , b in enumerate(self.books,start=1):
          print(f"{i}. ",end="")
          b.display()

  # issue a book 
  def issue_book(self):
      pass


  
# Class: Library
#   - Attribute: books (list)
#   - Method: add_book()      → Book object banao, list mein add karo
#   - Method: view_books()    → sab books dikhao
#   - Method: issue_book()    → title se search, is_available = False karo
#   - Method: return_book()   → title se search, is_available = True karo
#   - Method: save_to_file()  → file mein write karo
#   - Method: load_from_file() → file se load karo


# main execution here

def main():
    library = Library()
    while True:
        print("""
                === Library Book Manager ===
                  1) Add Book
                  2) View All Books
                  3) Issue Book
                  4) Return Book
                  5) Save Data
                  6) Exit
        """)

        choice = input("Enter your choice (1-6) => ")

        if choice == "1":
            library.add_book()
        elif choice == "2":
            library.view_books()
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "6":
            print("Exiting from program...")
            break
        else :
            print("Invalid choice , try again...")

# __name__ == "__main__"

# if __name__ == "__main__":
#     main()






# extra ya galat ..


    # book = {
    #     title,
    #     author,
    #     is_available
    # }


# same logic alag lekin long version 

    # if is_available in ("yes","y","true","1"):
    #     availablity = True
    # else:
    #     availablity = True