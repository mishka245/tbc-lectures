n = int(input("Enter tree size: "))
# pint n-i" " და i"*"
for i in range(n):
    line = (" " * (n - i)) + ((i * 2 + 1) * "*")
    print(line)

t = n // 10
# if t == 0:
#     t = 1
t = t if t != 0 else 1
#
t = t or 1


for i in range(t):
    line = (" " * (n - t)) + ("#" * t)
    print(line)

