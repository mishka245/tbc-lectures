try:
    a = int(input("Enter first number:"))
    b = int(input("Enter first number:"))
    x = a / b  # raise ZeroDivisionError
    print(x)

except ArithmeticError as zde:
    print("Can't divide by zero!", zde)
    print(type(zde))
    raise zde
except FileNotFoundError as fnfe:
    print("File can't be open", fnfe)
    raise fnfe
except Exception as e:
    print("Generic exception", e)
    raise e


