
file = open("example_list.txt", "r")
content = file.read()
content = content.strip("[").strip("]")
result = []
for number in content.split(","):
    number = number.strip()
    number = int(number)
    result.append(number)
file.close()

print(result)

