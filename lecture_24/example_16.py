import random


s = set()

# for i in range(50):
#     s.add(random.randint(1, 100))
while len(s) < 50:
    s.add(random.randint(1, 100))

print(len(s))
print(s)