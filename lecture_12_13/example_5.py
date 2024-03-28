def multiply(first, second, third):
    m = first * second * third

    return first, second, third, m

if __name__ == "__main__":
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    c = int(input("Enter c:"))
    a_1, b_1, c_1, mul = multiply(a, b, c)

    print(f"{a_1}*{b_1}*{c_1}={mul}")
