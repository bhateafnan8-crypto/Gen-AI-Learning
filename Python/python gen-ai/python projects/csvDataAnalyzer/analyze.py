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
    if not os.path.exists(lst):
      print(f"Error: File not found {lst}")
      return
    
    with open(lst,"r",encoding='utf-8') as file:
      reader = csv.DictReader(file)

      if reader.fieldnames is None:
        print(f"Error: File is empty {lst}")

      for row in reader:
        yield row

  except PermissionError:
      print(f"Error: Permission denied -> {lst}")
  except csv.Error as e:
      print(f"Error: Invalid CSV data in {lst} -> {e}")
  except UnicodeDecodeError:
      print(f"Error: Encoding issue in {lst} (not valid utf-8)")
  except Exception as e:
      print(f"Unexpected error while reading {lst} -> {e}")
  

def analyze(inp,lst):
  csvData = load_csv(lst)

  sums = sum(csvData[inp])
  average = sum(csvData[inp])/len(csvData[inp])
  maximum = max(csvData[inp])
  minimum = min(csvData[inp])

  return sums , average , maximum , minimum

def filter_data(cond,lst):
  csvData = load_csv(lst)
  lst = [row for row in csvData if cond(row)]

  return lst


def save_json(inp,lst):
  csvData = load_csv(lst)

  data = list(csvData)
  with open(inp,"w") as file:
    json.dump(data,file,indent=4)


def process_file(lst):
   load_csv(lst)
   analyze(lst)
   save_json(lst)

def main():
  inps = input("Enter your csv files ")+"csv".strip(",")



# galat hai

  # def load_csv(lst):
  #   try:
  #     with open(lst,"r",encoding='utf-8') as file:
  #       # read = csv.DictReader(file)
  #       for row in csv.DictReader(file):
  #         if os.path.exists(row):
  #           yield row
  #   except FileNotFoundError:
  #     print(f"File not found")



# analyze.py


