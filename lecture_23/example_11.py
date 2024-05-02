t = input("Please enter a digit:")
if not t.isdigit():
    # raise ValueError("You must enter a digit")
    # raise Exception("You must enter a digit")
    raise RuntimeError("You must enter a digit")
else:
    print("You entered a digit")

