import sqlite3

# =========================================================
# Question 1:
# "students.db" banao — students table create karo
# (id, name, marks) — 3 records insert karo,
# phir sab fetch karke print karo
# =========================================================
print("---------------------------")

conn = sqlite3.connect("students00.db")
cursor = conn.cursor()

# Har run pe fresh table banane ke liye (predictable output ke liye)
cursor.execute("DROP TABLE IF EXISTS students00")

cursor.execute("""
   CREATE TABLE IF NOT EXISTS students00(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT,
      marks INTEGER
   )
""")

cursor.execute("INSERT INTO students00 (name, marks) VALUES (?, ?)", ("Adfar", 30))
cursor.execute("INSERT INTO students00 (name, marks) VALUES (?, ?)", ("Safdar", 40))
cursor.execute("INSERT INTO students00 (name, marks) VALUES (?, ?)", ("Asfar", 50))
conn.commit()   # saare inserts ek saath commit

cursor.execute("SELECT * FROM students00")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()


# =========================================================
# Question 2:
# Wahi DB se sirf un students ko fetch karo jinka marks > 40 hai
# =========================================================
print("---------------------------")

conn = sqlite3.connect("students01.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS students01")

cursor.execute("""
   CREATE TABLE IF NOT EXISTS students01(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT,
      marks INTEGER
   )
""")

cursor.execute("INSERT INTO students01 (name, marks) VALUES (?, ?)", ("Adfar", 30))
cursor.execute("INSERT INTO students01 (name, marks) VALUES (?, ?)", ("Safdar", 40))
cursor.execute("INSERT INTO students01 (name, marks) VALUES (?, ?)", ("Asfar", 50))
conn.commit()

cursor.execute("SELECT * FROM students01 WHERE marks > ?", (40,))
toppr = cursor.fetchall()

for top in toppr:
    print(top)

conn.close()


# =========================================================
# Question 3:
# Ek student ka marks update karo (id se — unique target),
# phir delete karo naam se —
# dono ke baad SELECT se verify karo
# =========================================================
print("---------------------------")

conn = sqlite3.connect("students02.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS students2")

cursor.execute("""
   CREATE TABLE IF NOT EXISTS students02(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT,
      marks INTEGER
   )
""")

cursor.execute("INSERT INTO students02 (name, marks) VALUES (?, ?)", ("Adfar", 30))
cursor.execute("INSERT INTO students02 (name, marks) VALUES (?, ?)", ("Safdar", 40))
cursor.execute("INSERT INTO students02 (name, marks) VALUES (?, ?)", ("Asfar", 50))
conn.commit()

# --- UPDATE: id=1 (Adfar, marks=30) ka marks 20 karo ---
cursor.execute("UPDATE students02 SET marks = ? WHERE id = ?", (20, 1))
conn.commit()

cursor.execute("SELECT * FROM students02")
print("After UPDATE:")
for row in cursor.fetchall():
    print(row)

# --- DELETE: naam se (Safdar) ---
cursor.execute("DELETE FROM students02 WHERE name = ?", ("Safdar",))
conn.commit()

cursor.execute("SELECT * FROM students02")
print("After DELETE:")
for row in cursor.fetchall():
    print(row)

conn.close()

# db2.py