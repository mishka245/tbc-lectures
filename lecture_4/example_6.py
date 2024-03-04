import random

left = random.randint(0,10)
right = random.randint(10, 20)

print("left", left, "right", right)
s = 0
for i in range(left, right):
    s = s + i

print("sum", s)
