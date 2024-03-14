x = int(input("Please, enter X: "))

positive_x = abs(x)
# t * t * t = x
# 0 < t < x
t = 0
step = 1
while t * t * t < positive_x:
    t += step
sign = x / positive_x
print(x, int(sign * t))

