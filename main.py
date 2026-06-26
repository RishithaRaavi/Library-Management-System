from login import login
from books import (
    add_book,
    view_books,
    search_book,
    delete_book,
    update_book
)
from members import (
    add_member,
    view_members,
    search_member
)
from issue_book import issue_book
from return_book import return_book
from reports import report
if login():
    while True:
        print("\n===== Library Management System =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Delete Book")
        print("5. Update Book")
        print("6. Add Member")
        print("7. View Members")
        print("8. Search Member")
        print("9. Issue Book")
        print("10. Return Book")
        print("11. Reports")
        print("12. Exit")
        choice = input("Enter Choice: ")
        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            update_book()
        elif choice == "6":
            add_member()
        elif choice == "7":
            view_members()
        elif choice == "8":
            search_member()
        elif choice == "9":
            issue_book()
        elif choice == "10":
            return_book()
        elif choice == "11":
            report()
        elif choice == "12":
            print("Thank You!")
            break
        else:
            print("Invalid Choice")