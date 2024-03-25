# მოვძებნოთ კუბური ფესვი 28-დან
n = 1
epsilon = 0.001

low = 0
high = n
counter = 0
r = (high + low) / 2

while abs(n - r ** 3) > epsilon:
    if r ** 3 < n:
        high = r
    else:
        low = r
    r = (high + low) / 2
    counter += 1

print(f"n = {n}, answer - {r}, {r ** 3} iterations - {counter}")
