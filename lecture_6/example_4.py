import random

rand_number = random.randint(1, 100)

i = 0
while True:
    print("hello", i)
    i += 2  # i = i + 2
    if i >= rand_number:
        break

print("Random number - ", rand_number)
print("End of the program!!!")
