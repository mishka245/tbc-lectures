
def convert_to_binary(n):
    return bin(n)

def convert_to_10(binary):
    return int(binary)

def main():
    n = int(input("Enter number: "))

    binary = convert_to_binary(n)
    print(f"{n} -> {binary}")

    binary = binary[2:]
    print(f"new binary is: {binary}")

    num = convert_to_10(binary)
    print(type(num))
    print(f"{binary} -> {num}")


if __name__ == "__main__":
    main()
