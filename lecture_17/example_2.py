def my_abs(number):
    if number < 0:
        return -1 * number
    return number


def my_square(x):
    return x ** 2


def apply_to_each(elements, func):  # func -> 76uyg76uyg8
    for i in range(len(elements)):
        elements[i] = func(elements[i])


def main():
    my_list = [2, -4, 12, -1, 0, 1]

    apply_to_each(my_list, my_abs)  # my_abs -> 76uyg76uyg8
    print(my_list)
    apply_to_each(my_list, my_square)
    print(my_list)
    apply_to_each(my_list, str)
    print(my_list)


if __name__ == "__main__":
    main()
