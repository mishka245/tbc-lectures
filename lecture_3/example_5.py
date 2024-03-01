import random
import time

t = time.time()  # datetime.now()
# print("time ", t)
# random.seed(22)  Fixed seed, generates same number on same run
# random.seed(15)  # Fixed seed, generates same number on same run
random.seed(t)  # default behaviour 

print(random.randint(1, 1000))
print(random.randint(1, 1000))
print(random.randint(1, 1000))

