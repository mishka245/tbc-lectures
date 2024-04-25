counter = 0


def foo():
    print(counter)

def bar():
    counter = counter + 2
    print(counter)


def fib(n):
    global counter
    counter += 1
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


def main():
    foo()
    # print(fib(8))
    # print(fib(10))


if __name__ == "__main__":
    main()
