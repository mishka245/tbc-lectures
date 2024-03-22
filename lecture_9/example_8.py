import random

user_input = input("Please enter some text: ")
# user_input = "my random text here"

random_number = random.randint(0, 8)
print("random_number", random_number)
if random_number == 0:
    print(user_input.count("a"))
elif random_number == 1:
    print(user_input.find("b"))
elif random_number == 2:
    print(user_input.replace("c", "*"))
elif random_number == 3:
    print(user_input.upper())
elif random_number == 4:
    print(user_input.lower())
elif random_number == 5:
    print(user_input.capitalize())
elif random_number == 6:
    print(user_input.swapcase())
elif random_number == 7:
    # print("found d" if user_input.find("d") != -1 else "not found d")  # option 1
    print("found d" if "d" in user_input else "not found d")  # option 2
else:
    print(user_input.replace("e", ""))

