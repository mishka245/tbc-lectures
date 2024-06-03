# classic for loops vs set comprehension
# classic for loop

my_set = set()
for i in range(10):
    my_set.add(i)
print(my_set)

my_set = {i for i in range(10)}
print(my_set)

my_set = {i for i in range(10) if i != 0}
print(my_set)

my_set = {i ** 2 for i in range(10) if i != 0}
print(my_set)


