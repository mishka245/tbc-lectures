import random

my_dict = {}

for _ in range(5):
    key = random.randint(10, 100)
    value = key ** 4
    my_dict[str(key)] = value
print(my_dict)

file = open("my_dict.txt", "w")
file.write(str(my_dict))
file.close()
