my_dict = {"John": 90, "Jane": 95, "Jack": 85, "Jill": 80}

for item in my_dict.items():
    print(item)

print("-" * 100)

for key, value in my_dict.items():
    print(key, value)

print("-" * 100)


# for key in my_dict:
for key in my_dict.keys():
    print(key)

print("-" * 100)

for key in my_dict.values():
    print(key)

print("-" * 100)
