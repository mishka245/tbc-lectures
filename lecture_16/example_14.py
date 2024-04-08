def main():
    my_list = [1, 2, 3, 4, 1, 2, 3, 4, 1, 1, 1]

    while 1 in my_list:
        my_list.remove(1)

    print(my_list)


if __name__ == "__main__":
    main()
