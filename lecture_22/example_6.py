file = open("../hi.txt", "r")
counter = 0
for line in file:
    count = line.count(" ") + 1
    counter += count
print("Number of words", counter)
file.close()

