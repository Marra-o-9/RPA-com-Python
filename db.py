import sqlite3

conn = sqlite3.connect("example.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    age INTEGER
                )""")

conn.commit()

cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Rosie meu amor", 31))
conn.commit()

cursor.execute("UPDATE users SET age = ? WHERE name = ?", (32, "Rosie meu amor"))
conn.commit()

cursor.execute("DELETE FROM users WHERE name = ?", ("Rosie"))
conn.commit()

