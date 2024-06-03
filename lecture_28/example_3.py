# classic for loops vs list comprehension
# classic for loop

my_list = []
for i in range(10):
    if i == 0:
        continue
    # if i % 2 == 0:
    #     my_list.append(i)
    # else:
    #     my_list.append('odd')
    my_list.append(i if i % 2 == 0 else "odd")
print(my_list)

#          | post proccesing          |    loop         |  filter   |
my_list = [i if i % 2 == 0 else "odd" for i in range(10) if i != 0]
print(my_list)

my_list = [i % 2 == 0 for i in range(10)]
print(my_list)
