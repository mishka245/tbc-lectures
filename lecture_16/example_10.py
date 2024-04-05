import random

for i in range(20):
    number = random.randint(0, 100)

    if number % 2 == 0:
        print("even", number)
    else:
        print("odd", number)
