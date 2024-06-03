# classic for loops vs list comprehension
# classic for loop
import random

my_list = []
for i in range(10):
    my_list.append(i)
print(my_list)

my_list = [i for i in range(10)]
print(my_list)

my_list = [random.randint(10, 10000) for _ in range(10)]
print(my_list)
