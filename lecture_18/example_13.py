def foo(elements: tuple[tuple[str, int]]):
    str_tuple = tuple()
    int_tuple = tuple()
    for str_element, int_element in elements:
        str_tuple += (str_element,)
        int_tuple += (int_element,)
    return int_tuple, str_tuple, len(str_tuple), sum(int_tuple) / len(int_tuple)


def main():
    my_tuple = (("hi", 5), ("no", 8), ("look", 20), ("hi", 1))
    result = foo(my_tuple)
    print(result)


if __name__ == "__main__":
    main()
