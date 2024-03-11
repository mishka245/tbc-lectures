i = 0
j = 0
while i < 4:
    while j < 4:
        print(i, j)
        j += 1
    print("i=", i, "j=", j)
    i += 1


"""output
0 0
0 1
0 2
0 3
i= 0 j= 4
i= 1 j= 4
i= 2 j= 4
i= 3 j= 4
"""