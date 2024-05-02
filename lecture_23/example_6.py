try:
    a = int(input("Enter first number:"))
    b = int(input("Enter first number:"))

    x = a / b

    # file = open("hi.txt")

    print(x)
except ZeroDivisionError:
    print("Cant divide by zero!")
except FileNotFoundError:
    print("File can't be open")
except ValueError:
    print("You must enter integer value")
finally:
    print("Final block")