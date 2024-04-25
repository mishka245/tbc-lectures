my_dict = {"Goga": "555123123", "Nino": "551123987"}
print(my_dict)

names = tuple(my_dict.keys())
numbers = tuple(my_dict.values())

print(names)
print(numbers)

names = list(names)
numbers = list(numbers)

print(names)
print(numbers)

again_dict = {}

for i in range(len(names)):
    again_dict[names[i]] = numbers[i]

print(again_dict)