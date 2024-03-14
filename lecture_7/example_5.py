x = 27
for t in range(0, x):
    if t * t * t == x:
        print(x, t)
        break
else:
    print(f"{x} does not have integer qubic root")
