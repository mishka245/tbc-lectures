def foo():
    print("Else statement")

try:
    # a = int(input("Enter first number:"))
    # b = int(input("Enter first number:"))
    # x = a / b

    file = open("test.txt", "r")
    content = file.read()
    print("Finish file reading")

except ZeroDivisionError:
    print("Cant divide by zero!")
except FileNotFoundError:
    print("File can't be open")
except ValueError:
    print("You must enter integer value")
else:
    foo()  # raise FileNotFoundError
finally:
    print("Final block")
    # file.close()