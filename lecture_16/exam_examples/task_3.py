"""
დაწერეთ პროგრამა რომელიც მიიღებს ორ ნატურალურ რიცხვს a და b,
სადაც 0 < a,b < 10000 და ეკრანზე გამოიტანს ამ ორი რიცხვის უდიდეს საერთო გამყოფს.
 გადაჭერით ეს პრობლემა რეკურსიული მეთოდით

"""


def greatest_common_divisor(a, b, gcd):
    if a % gcd == 0 and b % gcd == 0:
        return gcd
    return greatest_common_divisor(a, b, gcd - 1)


def main():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    if not 0 < a < 10000 or not 0 < b < 10000:
        print("Please enter a and b in range (0, 10000)")
        return
    gcd = greatest_common_divisor(a, b, b)
    print("GCD: ", gcd)


if __name__ == "__main__":
    main()
