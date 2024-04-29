import json

file = open("my_dict.json", "r")
my_dict = json.load(file)
file.close()

print(my_dict)
print(type(my_dict))

