# მოვძებნოთ კუბური ფესვი 28-დან
n = 28
step = 0.000001
epsilon = 0.001
r = step
counter = 0
while abs(n - r ** 3) > epsilon:
    r += step
    counter += 1

print(f"n = {n}, answer - {r}, {r ** 3} iterations - {counter}")
