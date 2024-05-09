s = {"Goga", "Nino", "Zezva"}

print(s)

# s[1]  # Does not support
while True:
    user_input = input("Enter name: ")
    if user_input in s:  # O(1)
        print("Exists")
    else:
        print("Does not exist")
