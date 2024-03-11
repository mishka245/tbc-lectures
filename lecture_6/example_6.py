import random

left = random.randint(0, 10)
right = random.randint(10, 20)

s = 0
counter = left
while counter < right:
    s += counter
    counter += 1

print(f"left - {left}, right - {right}, sum = {s}")
