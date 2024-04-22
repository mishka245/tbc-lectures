my_dict = {"one": 1, "two": 2, "three": 3, "five": 5}

my_key = "four"

if my_key not in my_dict:
    my_dict[my_key] = 4

# found = False
# for k in my_dict:
#     if k == my_key:
#         found = True
#         break
# if not found:
#     my_dict[my_key] = 4

# val = my_dict.get(my_key)
# if val is None:
#     my_dict[my_key] = 4

# if my_key not in my_dict.keys():
#     my_dict[my_key] = 4
