import random

left = random.randint(0,10)
right = random.randint(0, 10)

print("left", left, "right", right)
s = 0
if left > right:
    for i in range(right, left):
        s = s + i
else:
    for i in range(left, right):
        s = s + i

print("sum", s)
