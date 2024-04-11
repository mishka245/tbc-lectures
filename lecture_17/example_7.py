def main():
    my_list =   [2, -4, 12, -1, 0, 1]
    your_list = [-2, 4, -12, 1, 0, -1]

    results = []
    for x in map(lambda a, b: a * b, my_list, your_list):
        results.append(x)
    print(my_list)
    print(results)

    results = []
    for x in map(min, my_list, your_list):
        results.append(x)
    print("all negative? ")
    print(results)


if __name__ == "__main__":
    main()
