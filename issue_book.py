import sqlite3
def issue_book():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    book = input("Enter Book Name: ")
    member = input("Enter Member Name: ")
    cursor.execute("SELECT * FROM books WHERE name=?", (book,))
    book_data = cursor.fetchone()
    if book_data is None:
        print("Book Not Available")
        conn.close()
        return
    cursor.execute("SELECT * FROM members WHERE name=?", (member,))
    member_data = cursor.fetchone()
    if member_data is None:
        print("Member Not Found")
        conn.close()
        return
    cursor.execute("SELECT * FROM issue WHERE book_name=?", (book,))
    issued = cursor.fetchone()
    if issued:
        print("Book Already Issued")
        conn.close()
        return
    cursor.execute(
        "INSERT INTO issue(book_name, member_name) VALUES(?, ?)",
        (book, member)
    )
    conn.commit()
    conn.close()
    print("Book Issued Successfully")