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

def load_csv(file_path):
  try:
    if not os.path.exists(file_path):
      print(f"Error: File not found {file_path}")
      return
    
    with open(file_path,"r",encoding='utf-8') as file:
      reader = csv.DictReader(file)

      if reader.fieldnames is None:
        print(f"Error: File is empty {file_path}")

      for row in reader:
        yield row

  except PermissionError:
      print(f"Error: Permission denied -> {file_path}")
  except csv.Error as e:
      print(f"Error: Invalid CSV data in {file_path} -> {e}")
  except UnicodeDecodeError:
      print(f"Error: Encoding issue in {file_path} (not valid utf-8)")
  except Exception as e:
      print(f"Unexpected error while reading {file_path} -> {e}")
  

def analyze(column_name,file_path):
  csvData = list(load_csv(file_path))

  if not csvData:
    return None

  Values = []


  # sums = sum(csvData[inp])
  # average = sum(csvData[inp])/len(csvData[inp])
  # maximum = max(csvData[inp])
  # minimum = min(csvData[inp])

  for row in csvData:
    value = row.get(column_name)

    if value is None:
      continue
    try:
      Values.append(float(value))
    except ValueError:
      continue

  return {
    "sums" : sum(Values) ,
    "average" : sum(Values) / len(Values) , 
    "maximum" : max(Values),
    "minimum": min(Values)
  }

def filter_data(condition,file_path):
  csvData = list(load_csv(file_path))

  return [row for row in csvData if condition(row)]


def save_json(output_file,csvData):
  # csvData = list(load_csv(file_path))

  # data = list(csvData)
  with open(output_file,"w",encoding="utf-8") as file:
    json.dump(csvData,file,indent=4)


def process_file(file_path,output_file,column_name,condition):
  csvData = load_csv(file_path)
  stats = analyze(column_name,file_path)
  save_json(output_file,csvData)
  return filter_data(condition,file_path)

  return stats

def main():
  file_path = input("Enter your csv files : ")+"csv".strip(",")
  condition = input("Enter your condition : ").strip()
  json_file = input("Enter name to savee (only name 'bydefault save on json'): ").strip()+"json"
  column_name = input("Enter your column name for stats : ").strip()
  files = [file_path]

  threads = []

  for file in files:
    t = threading.Thread(target=lambda fp = file : process_file(fp,json_file,column_name,condition))
    threads.append(t)
    t.start()

  for t in threads:
    t.join()

if __name__ == "__main__":
  main()


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


#  wrong 

  # def load_csv(lst):
  #   try:
  #     if not os.path.exists(lst):
  #       print(f"Error: File not found {lst}")
  #       return
      
  #     with open(lst,"r",encoding='utf-8') as file:
  #       reader = csv.DictReader(file)

  #       if reader.fieldnames is None:
  #         print(f"Error: File is empty {lst}")

  #       for row in reader:
  #         yield row

  #   except PermissionError:
  #       print(f"Error: Permission denied -> {lst}")
  #   except csv.Error as e:
  #       print(f"Error: Invalid CSV data in {lst} -> {e}")
  #   except UnicodeDecodeError:
  #       print(f"Error: Encoding issue in {lst} (not valid utf-8)")
  #   except Exception as e:
  #       print(f"Unexpected error while reading {lst} -> {e}")
    

  # def analyze(inp,lst):
  #   csvData = load_csv(lst)

  #   sums = sum(csvData[inp])
  #   average = sum(csvData[inp])/len(csvData[inp])
  #   maximum = max(csvData[inp])
  #   minimum = min(csvData[inp])

  #   return sums , average , maximum , minimum

  # def filter_data(cond,lst):
  #   csvData = load_csv(lst)
  #   lst = [row for row in csvData if cond(row)]

  #   return lst


  # def save_json(inp,lst):
  #   csvData = load_csv(lst)

  #   data = list(csvData)
  #   with open(inp,"w") as file:
  #     json.dump(data,file,indent=4)


  # def process_file(lst):
  #    load_csv(lst)
  #    analyze(lst)
  #    save_json(lst)

  # def main():
  #   inps = input("Enter your csv files ")+"csv".strip(",")

# analyze.py


