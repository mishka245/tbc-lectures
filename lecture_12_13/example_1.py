# გადაყავს რიცხვი ორობითში
n = int(input("enter number: "))
initial_n = n

b = ""
while n >= 1:
    b = str(n % 2) + b
    n //= 2

print(f"{initial_n} to binary: {b}")