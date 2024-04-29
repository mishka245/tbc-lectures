import random


def write_in_file(filename, obj):
    file = open(filename, "w")
    file.write(str(obj))
    file.close()


my_list = []

for _ in range(5):
    number = random.randint(10, 100)
    my_list.append(number)

my_tuple = tuple([x ** 4 for x in my_list])
print(my_list)
print(my_tuple)

write_in_file("my_list.txt", my_list)
write_in_file("my_tuple.txt", my_tuple)
