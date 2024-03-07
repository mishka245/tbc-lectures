a = int(input("Enter side a: "))
b = int(input("Enter side b: "))

"""
input - 2 3
|^|
|_|
-----------------------------------
input - 4 4
|^^|
|  |
|  |
|__|
cmd + shift + 8 - columnar selection
cmd + shift + v - extract to variable
"""
side = input("enter side symbol: ")
bottom = "-"
top = "-"

for i in range(a):
    for j in range(b):
        if i == 0:
            if j == 0 or j == b - 1:
                print(side, end='')
            else:
                print(top, end="")
        elif i == a - 1:
            if j == 0 or j == b - 1:
                print(side, end='')
            else:

                print(bottom, end="")
        else:
            if j == 0 or j == b - 1:
                print(side, end='')
            else:
                print(" ", end="")
    print()
