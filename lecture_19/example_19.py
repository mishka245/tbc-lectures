my_dict = {"John": 90, "Jane": 95, "Jack": 85, "Jill": 80}


val = my_dict.get("Goga", 0)
if val is not None:
    print(val)
else:
    print("Key 'Goga' not found")
