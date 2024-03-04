import random

left = random.randint(0,10)
right = random.randint(0, 10)

print("left", left, "right", right)

if left > right:
    print("swap")
    left, right = right, left

s = 0
for i in range(left, right):
    s = s + i

print("sum", s)
