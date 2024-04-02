import time

"""
Refactor example_8
"""
NUMBER_OF_ITERATIONS = 100


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


def measure_performance(func, argument):
    total_time = 0
    for t in range(NUMBER_OF_ITERATIONS):
        start_time = time.time()
        func(argument)
        end_time = time.time()
        elapsed_time = end_time - start_time
        total_time += elapsed_time
    return total_time


def main():
    i = int(input("Enter i: "))
    print("Iterative calculations take %.10f" % measure_performance(iter_fib, i))
    print("Recursive calculations take %.10f" % measure_performance(fib, i))


if __name__ == "__main__":
    main()
