def my_abs(number):
    if number < 0:
        return -1 * number
    return number


def main():
    my_list = [2, -4, 12, -1, 0, 1]

    for i in range(len(my_list)):
        my_list[i] = my_abs(my_list[i])
    print(my_list)


if __name__ == "__main__":
    main()
