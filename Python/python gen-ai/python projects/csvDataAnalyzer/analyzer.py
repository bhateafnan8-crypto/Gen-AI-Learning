"""
=== CSV Data Analyzer ===

Features:
  - CSV file lo user se
  - Data analyze karo (average, max, min, filter)
  - Results JSON mein save karo
  - Multiple files threading se process karo

---- Structure ----
  - load_csv()        → CSV file read karo, generator se
  - analyze()         → avg, max, min calculate karo
  - filter_data()     → condition se filter — list comprehension
  - save_json()       → results JSON mein save
  - process_file()    → ek file ka poora flow
  - main()            → multiple files threading se

---- Topics Covered ----
  - CSV         → read with DictReader
  - JSON        → results save
  - Generators  → rows ek ek yield karo
  - List comprehensions → filter
  - Threading   → multiple files simultaneously
  - os          → file exist check
  - Error handling → file not found, invalid data
"""

#  code start here

# all modules importing

import os
import csv 
import json
import math
import threading

def load_csv():
    try:

      found = False
      max_attempts = 5

      while max_attempts:
        filename = input("Enter filename for analyzer (without extension) only csv file : ").strip()+".csv"

        if filename == "exit.csv":
          print("Exiting...")
          return
        
        if os.path.exists(filename):
          found = True
          break

        print(f"File not found . attempts left {max_attempts - 1}")

        max -= 1

      if not found:
        print("Max attempts rached ...")
        return
 
      with open(filename,"r") as f:
        for row in csv.DictReader(f):
          yield row
          
    except FileNotFoundError:
      print("File not found!")
      

    

# Features:
#   - CSV file lo user se
#   - Data analyze karo (average, max, min, filter)
#   - Results JSON mein save karo
#   - Multiple files threading se process karo

# ---- Structure ----
#   - load_csv()        → CSV file read karo, generator se
#   - analyze()         → avg, max, min calculate karo
#   - filter_data()     → condition se filter — list comprehension
#   - save_json()       → results JSON mein save
#   - process_file()    → ek file ka poora flow
#   - main()            → multiple files threading se





# galat hai
  # import os
  # import csv 
  # import json
  # import math
  # import threading

  # def load_csv():
  #     try:
  #       max = 5
  #       while max:
  #         filename = input("Enter filename for analyzer (without extension) only csv file : ").strip()+".csv"
  #         if filename == "exit.csv":
  #           break
  #         if os.path.exists(filename):
  #           break

  #         max -= 1
  #       if filename == "exit.csv":
  #         print("Break")
  #         return
  #       elif os.path.exists(filename):
  #         files = [filename]
  #       else:
  #         print("File not found")
  #         return

  #       for file in files:
  #         with open(file,"r") as f:
  #           for row in csv.DictReader(f):
  #             yield row
  #     except FileNotFoundError:
  #       print("File not found!")

# analyzer.py