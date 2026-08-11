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
      search_book = input("Enter a book title to issue => ").strip()

      if not search_book or search_book.isdigit():
          print("search_book should not be empty or number ...")
          return
      for i , b in enumerate(self.books , start=1):
        if search_book.lower() == b.title.lower():
            print(f"{i}. ", end="")
            if b.is_available == True:
              b.is_available = False
              b.display()
              print("Book issued successfully")
            else:
                print("Book already issued")
            break
      else:
        print("Book not found...")

  # return book 
  def return_book(self):
      search_book = input("Enter a book title to return => ").strip()

      if not search_book or search_book.isdigit():
          print("search_book should not be empty or number ...")
          return
      for i , b in enumerate(self.books , start=1):
        if search_book.lower() == b.title.lower():
            print(f"{i}. ", end="")
            if b.is_available == False:
              b.is_available = True
              b.display()
              print("Book returned successfully")
            else:
                print("Book already returned")
            break
      else:
        print("Book not found...")

  # save to file
  def save_to_file(self):

    with open("library.txt","w") as file:
      for i , b in enumerate(self.books,start=1):
        file.write(f"{i}. {b.title} written by {b.author} availability : {b.is_available}\n")
    print("Books Saved successfully...")

  # load from file

  def load_from_file(self):
      try:
          with open("library.txt", "r") as file:
              lines = file.read().splitlines()

              loaded = 0
              for line in lines:
                  if not line:
                      continue

                  parts = line.split(" written by ", 1)
                  title = parts[0].split(". ", 1)[1].strip()

                  author_part = parts[1].split(" availability : ", 1)
                  author = author_part[0].strip()
                  is_avail_text = author_part[1].strip()
                  is_available = is_avail_text == "True"

                  self.books.append(Book(title, author, is_available))
                  loaded += 1

              if loaded > 0:
                  print("Books Loaded successfully...")
              else:
                  print("File empty. Starting fresh.")
      except FileNotFoundError:
          print("No saved file found. Starting fresh.")



# main execution here

def main():
    library = Library()
    library.load_from_file()
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
            library.issue_book()
        elif choice == "4":
            library.return_book()
        elif choice == "5":
            library.save_to_file()
        elif choice == "6":
            print("Exiting from program...")
            break
        else :
            print("Invalid choice , try again...")

# __name__ == "__main__"

# if __name__ == "__main__":
#     main()






# extra ya galat ..

    # 1.
    # book = {
    #     title,
    #     author,
    #     is_available
    # }
    
    #  2. 
    #  parts = line.split(". ")
    #  title = parts[0].split(" written by ", 1)[1].strip()
    #  rest = parts[1]
    #  author = parts[0].split(" availability : ", 1)[1].strip()
    #  is_avail = parts[1]


    #  3.
    # def load_from_file(self):
    #       try:
    #         with open("library.txt","r") as file:
    #             content = file.read()
    #             lines = content.splitlines()

    #             loaded = 0
    #             for line in lines:
    #               if not line:
    #                   continue

    #               parts = line.split(" written by ", 1)

    #               title = parts[0].split(". ", 1)[1].strip()
                  
    #               author = parts[0].split(" availability : ", 1)[1].strip()
    #               is_avail = parts[1]


    #               self.books.append(Book(title,author,is_avail))
    #               loaded += 1
    #             if loaded > 0:
    #               print("Books Loaded successfully...")
    #             else:
    #               print("File empty. Starting fresh.")
    #       except FileNotFoundError:
    #           print("No saved file found. Starting fresh.") 
    # same logic alag lekin long version 

    # if is_available in ("yes","y","true","1"):
    #     availablity = True
    # else:
    #     availablity = True