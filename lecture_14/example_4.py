def iter_my_fact(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


def my_fact(n):
    if n == 0:
        # print("DEBUG: Base case: n = 0")
        return 1
    # print(f"DEBUG: return {n} * my_fact({n - 1})")
    return n * my_fact(n - 1)


def main():
    n = int(input("Enter n: "))
    print(my_fact(n))
    print(iter_my_fact(n))


if __name__ == "__main__":
    main()
