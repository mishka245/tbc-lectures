def multiply(first, second):
    return first * second

def multiply_3_numbers(first, second, third):
    # return multiply(multiply(first, second), third)
    mul = multiply(first, second)
    return multiply(mul, third)

if __name__ == "__main__":
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    c = int(input("Enter c:"))

    mul = multiply_3_numbers(a, b, c)

    print(f"{a}*{b}*{c}={mul}")
