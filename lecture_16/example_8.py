import random

random_numbers = []
even_numbers = []
odd_numbers = []

for i in range(20):
    number = random.randint(0, 100)
    random_numbers.append(number)

    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print("Random numbers", random_numbers)
print("even numbers", even_numbers)
print("odd numbers", odd_numbers)
