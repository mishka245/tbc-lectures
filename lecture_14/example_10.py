from example_8 import iter_fib, fib
from example_9 import measure_performance

"""
Refactor example_9
"""
NUMBER_OF_ITERATIONS = 100


def main():
    i = int(input("Enter i: "))
    print("Iterative calculations take %.10f" % measure_performance(iter_fib, i))
    print("Recursive calculations take %.10f" % measure_performance(fib, i))


if __name__ == "__main__":
    main()
