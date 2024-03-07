tree_size = int(input("Enter tree size - "))

# print the tree
for i in range(1, tree_size):
    spaces = " " * (tree_size - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)

# print the trunk
trunk_size = tree_size // 10
spaces = " " * (tree_size - trunk_size)
for i in range(0, trunk_size):
    print(spaces + "#" * trunk_size)
