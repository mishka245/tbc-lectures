counter = 0
cache = {}


def fib(n):
    global counter
    counter += 1
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


def cached_fib(n):
    global counter

    if n in cache:  # O(1)
        return cache[n]
    counter += 1
    if n <= 1:
        result = n
    else:
        result = cached_fib(n - 2) + cached_fib(n - 1)
    cache[n] = result

    return result


def main():
    global counter
    global cache
    print("without cache", fib(5), counter)
    counter = 0
    print("with cache", cached_fib(5), counter)
    counter = 0
    print("without cache", fib(10), counter)
    counter = 0
    print("with cache", cached_fib(10), counter)
    counter = 0
    print("without cache", fib(20), counter)
    counter = 0
    print("with cache", cached_fib(20), counter)
    counter = 0


if __name__ == "__main__":
    main()
