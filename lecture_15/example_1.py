def gcd(a: int, b: int) -> int:
    # x, x <= a, x >= 1
    m = min(a, b)  # +1
    for x in range(m, 0, -1):
        if a % x == 0 and b % x == 0:
            return x


def gcd_student_version(a: int, b: int) -> int:
    for x in range(a, 0, -1):
        if a % x == 0 and b % x == 0:
            return x


def main():
    a = int(input("Enter a number: "))
    b = int(input("Enter b number: "))
    print("gcd", a, b, "-", gcd(a, b))
    print("gcd-student", a, b, "-", gcd_student_version(a, b))


if __name__ == "__main__":
    main()
