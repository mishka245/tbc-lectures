"""
მიმდევრობა
fib(0) -> 1
fib(1) -> 1
fib(2) = fib(1) + fib(0)
fib(i) = fib(i - 1) + fib(i - 2)
ფიბონაჩის მმიმდევრობა
"""


def fib(i):
    if i == 0 or i == 1:
        return 1
    return fib(i - 1) + fib(i - 2)


def iter_fib(i):
    if i == 0 or i == 1:
        return 1
    fib_previous = 1  # n(0)
    fib_current = 1  # n(1)

    for t in range(2, i + 1):
        temp = fib_previous + fib_current
        fib_previous = fib_current
        fib_current = temp

    return fib_current


def main():
    i = int(input("Enter i: "))
    print(iter_fib(i))
    print(fib(i))


if __name__ == "__main__":
    main()
