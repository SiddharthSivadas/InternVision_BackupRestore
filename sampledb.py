import sqlite3

print(" Creating sample database...")

conn = sqlite3.connect('app.db')
cursor = conn.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)')
cursor.execute('INSERT INTO users (name) VALUES ("Siddharth")')
conn.commit()
conn.close()

print(" Sample database created successfully → app.db")

