my_dict = {"John": 90, "Jane": 95, "Jack": 85, "Jill": 80}

print(max(my_dict.items(), key=lambda key_value_pair: key_value_pair[1]))
print(min(my_dict.items(), key=lambda key_value_pair: key_value_pair[1]))
