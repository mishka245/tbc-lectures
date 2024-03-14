x = int(input("Please, enter non-negative X: "))

if x < 0:
    print("Please enter non-negative number")
    exit(1)

# t * t * t = x
# 0 < t < x
# x = 15, t = ~2.4
t = 0
step = 1
while t * t * t != x:
    t += step

print(x, t)


