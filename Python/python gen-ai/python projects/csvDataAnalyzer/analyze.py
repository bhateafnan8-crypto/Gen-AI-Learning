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

def load_csv(lst):
  try:
    with open(lst,"r",encoding='utf-8') as file:
      # read = csv.DictReader(file)
      for row in csv.DictReader(file)
        yield row
  except FileNotFoundError:
    print(f"File not found")
    




# analyze.py