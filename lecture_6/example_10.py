DB_PASSWORD = "Georgia"
MAX_TRIES = 3

input_password = input("Please enter password: ")

tries = 1

# Not recommended
while DB_PASSWORD != input_password:
    if tries == MAX_TRIES:
        print("You are blocked!!!")
        break
    tries += 1
    input_password = input("Password was not correct. Try again - ")
else:  # Not recommended
    print("Hello from Georgia")
