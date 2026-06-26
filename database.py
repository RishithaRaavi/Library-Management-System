import sqlite3
conn = sqlite3.connect("library.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS books(
    id INTEGER PRIMARY KEY,
    name TEXT,
    author TEXT
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS members(
    id INTEGER PRIMARY KEY,
    name TEXT,
    phone TEXT
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS issue(
    id INTEGER PRIMARY KEY,
    book_name TEXT,
    member_name TEXT
)
""")
conn.commit()
conn.close()
print("Database Created Successfully")