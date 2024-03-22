# მიზანია რომ `   mikheil     lomidze   ` -> `M. Lomidze`
name = input("Enter name and surname: ")

# input example - `   mikheil     lomidze   `
name = name.strip()  # -> `mikheil     lomidze`

first_space_index = name.find(" ")  # -> 7
count_of_spaces = name.count(" ")  # -> 5
clean_name = name[0:first_space_index]  # -> mikheil
surname = name[first_space_index + count_of_spaces:]  # -> lomidze
#         "m".upper() -> "M"  ". "   "Lomidze"
print(f"{clean_name[0].upper()}. {surname.capitalize()}")
