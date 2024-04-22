my_dict = {"Goga": 27, "Nika": 44}

for k in my_dict:
    print(k, my_dict[k])
print("-" * 100)
my_dict["Nino"] = 37

for k in my_dict:
    print(k, my_dict[k])
print("-" * 100)

# del my_dict["Goga"]
my_dict.pop("Goga")

for k in my_dict:
    print(k, my_dict[k])
