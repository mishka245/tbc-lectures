command = input("Do you agree (yes/no): ")

counter = 1
while command != "yes" and command != "no":
    if counter >= 3:
        print("Do not waste my time :)")
        break
    counter += 1
    command = input("Please enter `yes` or `no` - ")


if command == "yes":
    print("Thanks for yes")
elif command == "no":
    print("Thanks for no")
else:
    print(":(")
