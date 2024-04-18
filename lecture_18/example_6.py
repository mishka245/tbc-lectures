import random

# Iterables:
# string
# list
# tuple


def main():
    numbers = []
    for _ in range(20):
        numbers.append(random.randint(0, 1000))
    numbers = tuple(numbers)
    print(numbers)

    even = tuple()
    odd = tuple()
    for number in numbers:
        if number % 2 == 0:
            even += (number,)
        else:
            odd += (number,)

    print("Even", even)
    print("Odd", odd)


if __name__ == "__main__":
    main()
