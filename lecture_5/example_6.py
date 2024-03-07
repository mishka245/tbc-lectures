a = int(input("Enter side a: "))
b = int(input("Enter side b: "))

"""
input - 2 3
***
***

input - 4 4
****
****
****
****
cmd + shift + 8 - columnar selection
"""

for i in range(a):  # print rows
    print("*" * b)
