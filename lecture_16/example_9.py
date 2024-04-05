import random

even_numbers = []
odd_numbers = []

for i in range(20):
    number = random.randint(0, 100)

    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print("even numbers", even_numbers)
print("odd numbers", odd_numbers)
