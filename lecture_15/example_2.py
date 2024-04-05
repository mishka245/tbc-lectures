

def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return gcd(b, a % b)


def main():
    a = int(input("Enter a number: "))
    b = int(input("Enter b number: "))
    print("gcd", a, b, "-", gcd(a, b))


if __name__ == "__main__":
    main()
