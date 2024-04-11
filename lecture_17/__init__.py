l1 = [1,2,3,4]
l2 = [0,12,13,14]

for item in map(min, l1, l2):
    print(item)

print("---")
for item in map(lambda x, y: x * y, l1, l2):
    print(item)

t = map(lambda x, y: x * y, l1, l2)
print(t)
print(type(t))