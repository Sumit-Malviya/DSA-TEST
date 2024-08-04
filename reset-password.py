username = input("Enter username = ")
password = input("Enter password = ")

if username == "Admin" and password == "Admin":
    print("You can reset your password!")
else:
    print("You cannot reset your password!")
