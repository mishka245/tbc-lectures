import random
import json

my_dict = {}

for _ in range(5):
    key = random.randint(10, 100)
    value = key ** 4
    my_dict[str(key)] = value
print(my_dict)

my_dict["new_key"] = {"myls": [1,2,3,["oh no"]]}

file = open("my_dict.json", "w")
json.dump(my_dict, file, indent=4)
file.close()

