def my_abs(number):
    if number < 0:
        return -1 * number
    return number


def main():
    my_list = [2, -4, 12, -1, 0, 1]

    results = []
    for x in map(my_abs, my_list):
        results.append(x)
    print(my_list)
    print(results)



if __name__ == "__main__":
    main()
