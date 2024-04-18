import random


def main():
    numbers = tuple()
    for _ in range(20):
        print(numbers)
        numbers = numbers + (random.randint(0, 1000),)
    print(numbers)
    print(sorted(numbers))
    # print(numbers.sort())
    # print(numbers.append())
    # numbers.remove(123)


if __name__ == "__main__":
    main()
