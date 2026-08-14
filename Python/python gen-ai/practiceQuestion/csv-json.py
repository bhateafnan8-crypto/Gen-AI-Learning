import csv
import json
import os
# Question-> 
"""
1. Ek list of dicts hai —
   students = [
     {"name": "Ali", "marks": 45},
     {"name": "Sara", "marks": 32}
   ]
   Ise CSV file mein save karo, 
   phir wapas read karke print karo.
"""
# Soltuion-> 
print("---------------------------")

students = [
    {"name": "Ali", "marks": 45},
    {"name": "Sara", "marks": 32}
]

with open("student.csv","w",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name" ,  "marks"])
    for s in students:
        writer.writerow([s["name"] , s["marks"]])

with open("student.csv","r",newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)



# Question-> 
"""
2. Wahi students data JSON mein save karo,
   phir read karke sirf un students ka 
   naam print karo jinka marks > 35 hai.
"""
# Soltuion-> 
print("---------------------------")


with open("student.json","w",newline="") as f:
    json.dump(students,f)

with open("student.json","r",newline="") as f:
    load = json.load(f)

    filtered_student = [s['name'] for s in load if s['marks'] > 35 ]
    print(filtered_student)



# Question-> 
"""
3. User se naam aur phone input lo,
   existing contacts.json mein append karo
   (file pehle se exist kar sakti hai ya nahi bhi).
   Phir poori file read karke print karo.
"""
# Soltuion-> 
print("---------------------------")


name = input("Enter your name => ")
phone = input("Enter your phone => ")

contacts = []

if os.path.exists("contacts.json"):
    with open("contacts.json","r") as f:
        try:
            data = json.load(f)
            if isinstance(data,list):
                contacts = data
            elif data:
                contacts = [data]
        except json.JSONDecodeError:
            contacts = []

contacts.append({"name" : name , "phone" : phone})

with open("contacts.json","w") as f:
    json.dump(contacts,f,indent=2)

with open("contacts.json","r") as f:
    loadContacts = json.load(f)
    print(loadContacts)


# Question-> 
"""
4. Ek CSV file "products.csv" banao with columns:
   name, price, quantity
   3-4 products add karo, phir read karke 
   total inventory value nikalo 
   (price * quantity har product ka, sab ka sum)
"""
# Soltuion-> 
print("---------------------------")

with open("products.csv","w",newline="") as f:
    writers = csv.writer(f)
    writers.writerow(["name","price","quantity"])
    writers.writerow(["Bread",40,2])
    writers.writerow(["Ice-cream",90,4])
    writers.writerow(["Cake",500,1])

with open("products.csv","r",newline="") as f:
    dictread = csv.DictReader(f)

    total_value = 0

    for row in dictread:
        price = int(row["price"])
        quantity = int(row["quantity"])

        total_value += price * quantity

    print(f"Total Inventory value : {total_value}")

with open("products.csv","r",newline="") as f:
    readcontact = csv.reader(f)

    header = next(readcontact)

    print("Header : ",header)

    for row in readcontact:
        if not row:
            continue

        name = row[0]
        price = int(row[1])
        quantity = int(row[2])

        total = price * quantity

    print(total)


# Question-> 
"""
5. Ek JSON file "settings.json" mein 
   app settings save karo:
   {"theme": "dark", "language": "en", "font_size": 14}
   Phir read karke sirf "theme" update karo "light" mein,
   aur wapas save karo.
"""
# Soltuion-> 
print("---------------------------")

setting = {"theme": "dark", "language": "en", "font_size": 14}
with open("settings.json","w") as f:
    json.dump(setting,f)

with open("settings.json","r") as f:
    load = json.load(f)
    print(load)
    setting["theme"] = "light"

with open("settings.json","w") as f:
    json.dump(setting,f)

with open("settings.json","r") as f:
    load = json.load(f)
    print(load)


# Question-> 
"""
6. CSV file "employees.csv" read karo,
   sirf un employees ki list nikalo 
   jinka salary > 50000 hai,
   aur unhe "high_earners.json" mein save karo.
   (Pehle CSV mein dummy data likhke shuru karo)
"""
# Soltuion-> 
print("---------------------------")

# employee = [{"name":"Adfar","sal":40000},{"name":"Safdar","sal":30000},{"name":"Jafar","sal":50000},{"name":"Jabbar","sal":70000},{"name":"Afsar","sal":80000}]

with open("employees.csv","w",newline="") as f:
    writer1 = csv.writer(f)

    writer1.writerow(["name","sal"])
    writer1.writerow(["Adfar",40000])
    writer1.writerow(["Safdar",70000])


with open("employees.csv","r",newline="") as f:
    reader1 = csv.DictReader(f)

    # print(reader1)

    high_earners = []

    for row in reader1 :
        if int(row["sal"]) > 50000:
            high_earners.append({
                "name" : row["name"],
                "sal" : int(row["sal"])
            })

print("value - 1",high_earners)

with open("high_earners.json","w") as f:
    json.dump(high_earners,f,indent=2)


with open("employees.csv","r",newline="") as f:
    reader1 = csv.DictReader(f)
    high_earner = [{"name":row["name"],"sal":int(row["sal"])} for row  in reader1 if int(row["sal"]) > 50000]

print("value - 2",high_earner)

with open("high_earners.json","w") as f:
    json.dump(high_earner,f,indent=2)


# Question-> 
"""
7. User se marks input lo 5 subjects ke liye,
   results.csv mein save karo with columns:
   subject, marks, pass/fail (40 se kam = fail)
   Phir read karke summary print karo —
   kitne pass, kitne fail.
"""
# Soltuion-> 
print("---------------------------")




# Question-> 
"""
8. Do JSON files hain —
   "male_students.json" aur "female_students.json"
   Dono ko merge karke "all_students.json" mein save karo.
   Phir read karke total student count print karo.
   (Dummy data khud banao dono files mein)
"""
# Soltuion-> 
print("---------------------------")











# sahi hai but thoda issue de raha hai

# students = [
#     {"name": "Ali", "marks": 45},
#     {"name": "Sara", "marks": 32}
# ]

# with open("student.csv","w",newline="") as f:
#     for s in students:
#         writer = csv.writer(f)
#         writer.writerow(["name","marks"])
#         writer.writerow([s["name"],s["marks"]])

# with open("student.csv","r") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)



# sahi hai but thoda issue de raha hai .. single object ke liye sahi hai bas

# name = input("Enter your name => ")
# phone = input("Enter your phone => ")

# contact = {"name":name , "phone" : phone}


# with open("contact.json","a") as f:
#     json.dump(contacts,f)

# with open("contact.json","r") as f:
#     loadContact = json.load(f)
#     print(loadContact)


# sahi hai but thoda issue de raha hai .. list ko dict me convert karna hai


# with open("products.csv","w",newline="") as f:
#     writers = csv.writer(f)
#     writers.writerow(["name","price","quantity"])
#     writers.writerow(["Bread",40,2])
#     writers.writerow(["Ice-cream",90,4])
#     writers.writerow(["Cake",500,1])


# with open("products.csv","r",newline="") as f:
#     readers = csv.reader(f)
#     for row in readers:
#         print(f" {row} : total = {row["price"] * row["quantity"]} ")


 # isme pehli value jo hai wo strings hai is liye issue kar raha hai
# with open("products.csv","r",newline="") as f:
#     readcontact = csv.reader(f)

#     for row in readcontact:
#         price = row[1]
#         quantity = row[2]

#         total = price * quantity

#     print(total)

# with open("products.csv","w",newline="") as f:



# yaha per list direct nahi bhej sakte aur values string me hi jaati hai int me convert - casting karna padta hai..


# employee = [{"name":"Adfar","sal":40000},{"name":"Safdar","sal":30000},{"name":"Jafar","sal":50000},{"name":"Jabbar","sal":70000},{"name":"Afsar","sal":80000}]

# with open("employees.csv","w",newline="") as f:
#     writer1 = csv.writer(f)

#     writer1.writerow(["name","sal"])
#     writer1.writerow(["Adfar",40000])
#     writer1.writerow(["Safdar",70000])


# with open("employees.csv","r",newline="") as f:
#     reader1 = csv.DictReader(f)

#     print(reader1)

#     high_earner = [{"name":name,"sal":sal} for name , sal in reader1 if sal > 50000]

# with open("high_earners.json","w") as f:
#     json.dump(high_earner,f)