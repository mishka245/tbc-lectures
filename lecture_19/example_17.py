my_dict = {"John": 90, "Jane": 95, "Jack": 85, "Jill": 80}

names = []
values = []

for k, v in my_dict.items():
    names.append(k)
    values.append(v)

print("Names", names)
print("Values", values)
