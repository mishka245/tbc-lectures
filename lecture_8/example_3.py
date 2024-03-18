user_input = input("Please enter text: ")

for i in range(len(user_input)):
    if user_input[i] != "e" and user_input[i] != "E":
        print(user_input[i], end="")

print()
