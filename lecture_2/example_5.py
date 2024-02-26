USER_NAME = "admin"
CAPITALISED_USER_NAME = "Admin"
USER_PASSWORD = "password"

user_name = input("Enter user name: ")
password = input("Enter user password: ")

if (user_name == USER_NAME or user_name == CAPITALISED_USER_NAME) and password == USER_PASSWORD:
    print("Log in was successful")
else:
    print("User or password is wrong")

