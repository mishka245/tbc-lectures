x = int(input("Please, enter positive X: "))

if x <= 0:
    print("Please enter positive number")
    exit(1)

# t * t * t = x
# 0 < t < x
found = False
for t in range(0, x):
    if t * t * t == x:
        print(x, t)
        found = True
        break
if not found:
    print(f"{x} does not have integer qubic root")
