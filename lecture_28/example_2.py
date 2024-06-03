# classic for loops vs list comprehension
# classic for loop

my_list = []
for i in range(10):
    if i % 2 == 0:
        my_list.append(i)
print(my_list)

my_list = [i for i in range(10) if i % 2 == 0]
print(my_list)
