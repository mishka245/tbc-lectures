my_list = [100, 200, 300, 400, "str is also allowed", 600, 700, 800, 900, 10000]

for item in my_list:
    print(item, type(item))

print("---" * 100)

n = 0
while n < len(my_list):
    print(my_list[n])
    n += 1
