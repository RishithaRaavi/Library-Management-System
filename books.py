import sqlite3
def add_book():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    name = input("Enter Book Name: ")
    author = input("Enter Author Name: ")
    cursor.execute(
        "INSERT INTO books(name, author) VALUES(?, ?)",
        (name, author)
    )
    conn.commit()
    conn.close()
    print("Book Added Successfully")
def view_books():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    if books:
        print("\n------ Books List ------")
        for book in books:
            print("ID:", book[0], "| Name:", book[1], "| Author:", book[2])
    else:
        print("No Books Available")
    conn.close()
def search_book():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    name = input("Enter Book Name: ")
    cursor.execute("SELECT * FROM books WHERE name=?", (name,))
    book = cursor.fetchone()
    if book:
        print("\nBook Found")
        print("ID:", book[0])
        print("Name:", book[1])
        print("Author:", book[2])
    else:
        print("Book Not Found")
    conn.close()
def delete_book():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    name = input("Enter Book Name to Delete: ")
    cursor.execute("DELETE FROM books WHERE name=?", (name,))
    conn.commit()
    if cursor.rowcount > 0:
        print("Book Deleted Successfully")
    else:
        print("Book Not Found")
    conn.close()
def update_book():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    old_name = input("Enter Old Book Name: ")
    cursor.execute("SELECT * FROM books WHERE name=?", (old_name,))
    book = cursor.fetchone()
    if book:
        new_name = input("Enter New Book Name: ")
        new_author = input("Enter New Author Name: ")
        cursor.execute(
            "UPDATE books SET name=?, author=? WHERE name=?",
            (new_name, new_author, old_name)
        )
        conn.commit()
        print("Book Updated Successfully")
    else:
        print("Book Not Found")
    conn.close()