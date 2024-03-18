n = int(input("Enter the number: "))

while not(n > 0 and n <10):
    n = int(input("Number should be between 0 and 10. Enter again: "))

a = 0
b = n
while a < n + 1:
    space = " " * b
    print(space, end = " ")

    j = a
    while j > 0:
        print(j, end = "")
        j -= 1

    print(0, end= "" )

    j = 0
    while j < a:
        print(j + 1, end = "")
        j += 1

    print()
    a += 1
    b -= 1


#     0
#    101
#   21012