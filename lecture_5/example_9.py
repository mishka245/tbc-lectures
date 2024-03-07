import random

n = int(input("Enter tree size: "))
# pint n-i" " და i"*"
toys = ["@", "$", "$", "X"]
for i in range(n):
    line = (" " * (n - i)) + ((i * 2 + 1) * "*")
    loc = random.randint(0, (i * 2 + 1))
    loc = loc + (n - i)
    toy = random.choice(toys)
    new_line = ""
    for ii, c in enumerate(line):
        if ii == loc:
            new_line += toy
        else:
            new_line += c
    print(new_line)

t = n // 10
for i in range(t):
    line = (" " * (n - t)) + ("#" * t)
    print(line)

