user_input = input("Please enter text: ")

counter = 0

for i in range(len(user_input)):
    if user_input[i] == "a":
        counter += 1

print("Count of a - ", counter)
