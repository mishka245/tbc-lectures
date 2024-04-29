filename = input("Please enter file name: ")
filename = f"{filename}.txt"

file = open(filename, "w")
for _ in range(5):
    text = input("Please enter some text: ")
    file.write(text + "\n")

# file.write("Finished")

file.close()
