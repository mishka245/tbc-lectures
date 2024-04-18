import random


# Iterables:
# string
# list
# tuple


def main():
    numbers = tuple()
    for _ in range(20):
        numbers = numbers + (random.randint(0, 1000),)
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
