import sqlite3
# Question-> 
"""
1. "contacts.db" banao — contacts table (id, name, phone, email)
   CLI se user input lo aur insert karo,
   phir sab fetch karke print karo
"""
# Soltuion-> 
print("---------------------------")

conn = sqlite3.connect("contacts.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS contacts")

cursor.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            phone INTEGER,
            email TEXT
        )
""")

def insertion(name,phone,email):
    cursor.execute("INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)", (name, phone,email))
    conn.commit()
name = input("Enter your name : ")
phone = input("Enter your phone number : ")
email = input("Enter your email id : ")

insertion(name,phone,email)

cursor.execute("SELECT * FROM contacts")

rows = cursor.fetchall()
for row in rows:
    print(row)

# conn.close()


# Question-> 
"""
2. Wahi DB mein search feature add karo —
   naam se search karo, 
   agar nahi mila toh "Not found" print karo
"""
# Soltuion-> 
print("---------------------------")

search = input("Enter name to search : ")

def findcontact(search):
    cursor.execute(f"SELECT * FROM contacts WHERE name == ?",(search,))
    foundcontact = cursor.fetchall()

    if not foundcontact:
        print("Not Found!")
    for found in foundcontact:
        print(found)

findcontact(search)

# conn.close()


# Question-> 
"""
3. executemany() use karo —
   ek list of tuples se 5 records 
   ek saath insert karo
"""
# Soltuion-> 
print("---------------------------")

contacts_data = [
    ("Haider", 90822, "Haider@gmail.com"),
    ("Jafar", 80837, "Jafar@gmail.com"),
    ("Sadik", 60783, "Sadik@gmail.com"),
    ("Kasim", 89322, "Kasim@gmail.com"),
    ("Kadar", 90783, "Kadar@gmail.com"),
    ("Sameer", 783822, "Sameer@gmail.com"),
]

cursor.executemany("INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)", contacts_data)
conn.commit()

cursor.execute("SELECT * FROM contacts")

added = cursor.fetchall()
for row in added:
    print(row)


# Question-> 
"""
4. DB mein products table banao 
   (id, name, price, stock) —
   stock = 0 wale products fetch karo,
   phir unhe DELETE karo,
   verify karo SELECT se
"""
# Soltuion-> 
print("---------------------------")

cursor.execute("DROP TABLE IF EXISTS products")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        price INTEGER,
        stock INTEGER
    )
""")

product_data = [
    ("Banana",50,2),
    ("DryFruits",650,0),
    ("Apple",520,2),
    ("Guava",150,0),
]

cursor.executemany("INSERT INTO products (name,price,stock) VALUES (?,?,?)",product_data)
conn.commit()

cursor.execute("SELECT * FROM products")
prods = cursor.fetchall()

print("ALl products : ")

for pros in prods:
    print(pros)

cursor.execute("SELECT * FROM products WHERE stock == ?",(0,))

zerostockprods = cursor.fetchall()

print("zero stock products : ")

for pros in zerostockprods:
    print(pros)

cursor.execute("DELETE  FROM products WHERE stock == ?",(0,))
conn.commit()
cursor.execute("SELECT * FROM products")

zerostockprodsdlt = cursor.fetchall()

print("zero stock products DELETED : ")

for pros in zerostockprodsdlt:
    print(pros)


# Question-> 
"""
5. try-except ke saath DB operations karo —
   duplicate entry, connection error 
   properly handle karo
"""
# Soltuion-> 
print("---------------------------")

try:
    conn2 = sqlite3.connect("user.db")
    cursor1 = conn2.cursor()

    cursor1.execute("DROP TABLE IF EXISTS user")
    cursor1.execute("""
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER
        )
    """)

    cursor1.execute("INSERT INTO user (name,age) VALUES (?,?)",("Haider",20))
    cursor1.execute("INSERT INTO user (name,age) VALUES (?,?)",("Kasim",23))
    conn2.commit()

    cursor1.execute("SELECT * FROM user")
    users = cursor1.fetchall()

    for user in users:
        print(user)

    conn2.close()


except sqlite3.IntegrityError:
    print("Aready exist.. dont be duplicate..")

except sqlite3.OperationalError:
    print("Not connected..")

except sqlite3.Error as e:
    print("Error",e)

# db3.py


#  syntax error aagaya.. tuple banake fir dena tha direct de diya..


    # cursor.executemany("""
    #     INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)", (Haider, 90822,Haider@gmail.com))
    #     INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)", (Jafar, 80837,Jafar@gmail.com))
    #     INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)", (Sadik, 60783,Sadik@gmail.com))
    #     INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)", (Kasim, 89322,Kasim@gmail.com))
    #     INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)", (Kadar, 90783,Kadar@gmail.com))
    #     INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)", (Sameer, 783822,Sameer@gmail.com))
    # """)