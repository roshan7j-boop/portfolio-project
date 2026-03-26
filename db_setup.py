import sqlite3

DB_NAME = 'mydatabase.db'

conn = sqlite3.connect(DB_NAME)
c = conn.cursor()

# Example table
c.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)
''')

conn.commit()
conn.close()
print("Database created successfully!")