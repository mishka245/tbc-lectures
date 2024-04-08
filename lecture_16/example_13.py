
def main():
    my_list = [1, 1, 2, 3, 4, 1, 2, 3, 4, 1, 1, 1]  # len -> 11
    #                |
    #                i
    # my_list.remove(1)
    # my_list = [2, 3, 4, 1, 2, 3, 4, 1, 1, 1]  # len -> 10
    #            |
    #            i

    # misbehaves, not recommended
    i = 0
    while i < len(my_list):
        if my_list[i] == 1:
            my_list.remove(my_list[i])
        else:
            i += 1

    # does not work. not recommended
    # for c in my_list:
    #     if c == 1:
    #         my_list.remove(c)

    print(my_list)


if __name__ == "__main__":
    main()
