import sqlite3

# Connect / create DB
conn = sqlite3.connect("mydb.db")
cursor = conn.cursor()

# Table create
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT
    )
""")

# Insert
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Afnan", "a@gmail.com"))
conn.commit()

# Select
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close
conn.close()

# db-concept.py