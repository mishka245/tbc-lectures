def exists_in(elements, item):
    for x in elements:
        if x == item:
            return True
    return False


def main():
    my_list = [1, 2, 3, 4, 1, 2, 3, 4, 1, 1, 1]

    while exists_in(my_list, 1):
        my_list.remove(1)

    print(my_list)


if __name__ == "__main__":
    main()
