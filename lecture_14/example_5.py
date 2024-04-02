
def iter_my_power(a: int, exp: int) -> int:
    result = 1
    while True:
        if exp == 0:
            break
        exp = exp - 1
        result = result * a
    return result


def my_power(a: int, exp: int) -> int:
    if exp == 0:
        return 1
    return a * my_power(a, exp - 1)


def main():
    a = int(input("Enter a: "))
    exp = int(input("Enter exp: "))
    result = my_power(a, exp)
    print(result)
    print(iter_my_power(a, exp))


if __name__ == "__main__":
    main()
