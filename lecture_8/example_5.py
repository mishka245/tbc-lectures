user_input = input("Please enter text: ")

found = False

for i in range(len(user_input)):
    if user_input[i] == "a":
        found = True
        break

if found:
    print("არის")
else:
    print("არ არის")
