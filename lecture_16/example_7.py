import random

random_numbers = []
even_numbers = []
odd_numbers = []

for i in range(20):
    random_numbers.append(random.randint(0, 100))

for item in random_numbers:
    if item % 2 == 0:
        even_numbers.append(item)
    else:
        odd_numbers.append(item)

print("Random numbers", random_numbers)
print("even numbers", even_numbers)
print("odd numbers", odd_numbers)
