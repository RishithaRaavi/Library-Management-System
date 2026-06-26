import sqlite3
def return_book():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    book = input("Enter Book Name: ")
    cursor.execute(
        "DELETE FROM issue WHERE book_name=?",
        (book,)
    )
    conn.commit()
    conn.close()
    print("Book Returned Successfully")