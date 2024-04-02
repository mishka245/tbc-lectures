def my_mult(a, b):
    result = 0
    for i in range(b):
        result += a
    return result


def main():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print(my_mult(a, b))


if __name__ == "__main__":
    main()
