import sqlite3
# Question-> 
"""
1. "students.db" banao — students table create karo
   (id, name, marks) — 3 records insert karo,
   phir sab fetch karke print karo
"""
# Soltuion-> 
print("---------------------------")

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
   CREATE TABLE IF NOT EXISTS students(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT,
      marks INTEGER
   )
""")

cursor.execute("INSERT INTO students (name,marks) VALUES (?,?)",("Adfar",30))
conn.commit()

cursor.execute("INSERT INTO students (name,marks) VALUES (?,?)",("Safdar",40))
conn.commit()

cursor.execute("INSERT INTO students (name,marks) VALUES (?,?)",("asfar",50))
conn.commit()



cursor.execute("SELECT * FROM students")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()


# Question-> 
"""
2. Wahi DB se sirf un students ko 
   fetch karo jinka marks > 40 hai
"""
# Soltuion-> 
print("---------------------------")

conn = sqlite3.connect("students1.db")
cursor = conn.cursor()

cursor.execute("""
   CREATE TABLE IF NOT EXISTS students1(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT,
      marks INTEGER
   )
""")

cursor.execute("INSERT INTO students1 (name,marks) VALUES (?,?)",("Adfar",30))
conn.commit()

cursor.execute("INSERT INTO students1 (name,marks) VALUES (?,?)",("Safdar",40))
conn.commit()

cursor.execute("INSERT INTO students1 (name,marks) VALUES (?,?)",("asfar",50))
conn.commit()

cursor.execute("SELECT * FROM students1 WHERE marks > ?",(40,))

toppr = cursor.fetchall()

for top in toppr:
    print(top)

conn.close()


# Question-> 
"""
3. Ek student ka marks update karo naam se,
   phir delete karo naam se —
   dono ke baad SELECT se verify karo
"""
# Soltuion-> 
print("---------------------------")

conn = sqlite3.connect("students2.db")
cursor = conn.cursor()

cursor.execute("""
   CREATE TABLE IF NOT EXISTS students2(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT,
      marks INTEGER
   )
""")

cursor.execute("INSERT INTO students2 (name,marks) VALUES (?,?)",("Adfar",30))
conn.commit()

cursor.execute("INSERT INTO students2 (name,marks) VALUES (?,?)",("Safdar",40))
conn.commit()

cursor.execute("INSERT INTO students2 (name,marks) VALUES (?,?)",("asfar",50))
conn.commit()


cursor.execute("UPDATE students2 SET marks = ? WHERE name = ?",(20,"Adfar"))
conn.commit()

cursor.execute("SELECT * FROM students2")

toppr1 = cursor.fetchall()

for top in toppr1:
    print(top)

cursor.execute("DELETE FROM students2 WHERE name = ?",("Safdar",))
conn.commit()

cursor.execute("SELECT * FROM students2")

toppr1 = cursor.fetchall()

for top in toppr1:
    print(top)

conn.close()






# db.py