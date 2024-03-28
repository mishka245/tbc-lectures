def multiply(first, second, third):
    mul = first * second * third

    print(f"{first}*{second}*{third}={mul}")

if __name__ == "__main__":
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    c = int(input("Enter c:"))
    multiply(a, b, c)
