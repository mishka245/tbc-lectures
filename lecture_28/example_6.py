# classic for loops vs dict comprehension
# classic for loop

my_dict = set()
for i in range(10):
    my_dict.add(i)
print(my_dict)

my_dict = {i: i for i in range(10) if i != 0}
print(my_dict)
