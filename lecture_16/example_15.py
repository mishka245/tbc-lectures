
def main():
    my_list = [1, 1, 2, 3, 4, 1, 2, 3, 4, 1, 1, 1]

    # not recommended
    # for c in my_list:
    # okay version
    for c in my_list.copy():
        if c == 1:
            my_list.remove(c)

    print(my_list)


if __name__ == "__main__":
    main()
