import time
"""
დავწეროთ პროგრამა რომელიც გადაწოდებული რიცხვისთვის იპოვის ფიბონაჩის მიმდევრობის წევსრ იტერაციულად და რეკურსიულად:
პროგრამამ უნდა დაბეჭდოს 100 100 იტერაციის ჯამური შედეგები
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
    iter_result = 0  # იტერაციულად შესრულებული გამოთვლისთვის საჭირო დრო
    for t in range(100):
        start_time = time.time()
        result = iter_fib(i)
        end_time = time.time()
        elapsed_time = end_time - start_time
        iter_result += elapsed_time

    recursive_result = 0  # რეკურსიულად შესრულებული გამოთვლისთვის საჭირო დრო
    for t in range(100):
        start_time = time.time()
        result = fib(i)
        end_time = time.time()
        elapsed_time = end_time - start_time
        recursive_result += elapsed_time
    print("Iterative calculations take %.10f" % iter_result)
    print("Recursive calculations take %.10f" % recursive_result)


if __name__ == "__main__":
    main()
