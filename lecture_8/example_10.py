user_input = input("Enter text please: ")
new_word = ""

# for i in range(len(user_input)):
#     if user_input[i] != "e":
#         new_word = new_word + user_input[i]

for c in user_input:
    if c != "e":
        new_word = new_word + c

print(new_word)
