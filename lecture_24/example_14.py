l = [1, 2, 3, 1, 2, 3, 1, 2, 3]

s = set()

for item in l:
    if item not in s:
        s.add(item)

result = list(s)
print(result)
