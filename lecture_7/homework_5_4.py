n = int(input("Enter number [0, 10): "))

if n < 0 or n >= 10:
    print("Enter number [0, 10)")
    exit(1)

for i in range(0, n + 1):
    print(" " * (n - i) * 2, end="")
    for l in range(-i, i + 1):
        print(abs(l), end=" ")
    print()
for i in range(n-1, -1, -1):
    print(" " * (n - i) * 2, end="")
    for l in range(-i, i + 1):
        print(abs(l), end=" ")
    print()


