from helpers import circle_perimeter, circle_area


def main():
    try:
        user_input = input("Please enter circle radius: ")
        r = float(user_input)
    except Exception as ex:
        print(f"Invalid input for circle radius {user_input}. Exception:", ex)
        return
    area = circle_area(r)
    perimeter = circle_perimeter(r)
    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")


if __name__ == "__main__":
    main()
