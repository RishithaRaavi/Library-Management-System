def login():

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username == "admin" and password == "1234":
        print("\nLogin Successful\n")
        return True
    else:
        print("\nInvalid Username or Password")
        return False