import sqlite3

# Add Member
def add_member():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    name = input("Enter Member Name: ")
    phone = input("Enter Phone Number: ")

    cursor.execute(
        "INSERT INTO members(name, phone) VALUES(?, ?)",
        (name, phone)
    )

    conn.commit()
    conn.close()

    print("Member Added Successfully")


# View Members
def view_members():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM members")
    members = cursor.fetchall()

    if members:
        print("\n------ Members List ------")
        for member in members:
            print("ID:", member[0], "| Name:", member[1], "| Phone:", member[2])
    else:
        print("No Members Found")

    conn.close()


# Search Member
def search_member():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    name = input("Enter Member Name: ")

    cursor.execute("SELECT * FROM members WHERE name=?", (name,))
    member = cursor.fetchone()

    if member:
        print("\nMember Found")
        print("ID:", member[0])
        print("Name:", member[1])
        print("Phone:", member[2])
    else:
        print("Member Not Found")

    conn.close()