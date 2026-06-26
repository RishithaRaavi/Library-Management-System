import sqlite3
def report():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    print("\nBooks")
    cursor.execute("SELECT * FROM books")
    print(cursor.fetchall())
    print("\nMembers")
    cursor.execute("SELECT * FROM members")
    print(cursor.fetchall())
    print("\nIssued Books")
    cursor.execute("SELECT * FROM issue")
    print(cursor.fetchall())
    conn.close()