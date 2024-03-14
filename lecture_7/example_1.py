a = int(input("Enter a: "))
# n = a * a
# n = 4 * 4 = 4 + 4 + 4 + 4
positive_a = abs(a)  # abs(-4) -> 4 , abs(4) -> 4, abs(0) -> 0
counter = 0
result = 0
while counter < positive_a:
    result += positive_a

    counter += 1

print(f"{a} * {a} = {result}")
