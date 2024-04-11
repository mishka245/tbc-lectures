def main():
    my_list = [2, -4, 12, -1, 0, 1]
    your_list = [-2, 4, -12, 1, 0, -1, 1, 2, 3, 4, 5]

    for x in map(min, your_list, my_list):
        print(x)


if __name__ == "__main__":
    main()
