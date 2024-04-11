def main():
    my_list = [2, -4, 12, -1, 0, 1]

    result_of_map = map(lambda a: a ** 2, my_list)

    print(my_list)
    print(result_of_map)

    print(type(my_list))
    print(type(result_of_map))

    list_from_map = list(result_of_map)
    list_from_map = list(map(lambda a: a ** 2, my_list))

    print(list_from_map)
    print(type(list_from_map))


if __name__ == "__main__":
    main()
