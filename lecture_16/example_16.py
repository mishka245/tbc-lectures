
def main():
    my_list = [1, 23, 12, 0, 11, 10]
    # new_list = [0, 1, ...]

    # my_list.sort()  # in place
    # print(len(my_list))
    sorted_array = sorted(my_list, reverse=True)  # new_list = [0, 1, ...]
    print(my_list)
    print(sorted_array)


if __name__ == "__main__":
    main()
