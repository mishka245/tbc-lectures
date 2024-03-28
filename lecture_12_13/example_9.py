def convert_to_bin(num):
    if num == 0:
        return "0"

    b = ""
    while num >= 1:
        b = str(num % 2) + b
        num //= 2

    return b

if __name__ == "__main__":
    n = int(input("Enter number: "))

    binary = convert_to_bin(n)

    print(f"{n} to binary is {binary}")
