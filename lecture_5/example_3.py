
for a in range(1, 10):
    for b in range(1, 10):
        result = a * b
        extra = ""
        if result < 10:
            extra = " "
        print(f"{a} * {b} = {result}{extra}", end=" ")
    print()
