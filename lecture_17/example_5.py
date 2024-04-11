def str_to_len(s: str) -> int:
    return len(s)


def main():
    my_list = [
        "ythgji76iuv",
        "ythgiuv",
        "ythgji76iuvaSDasd",
        "iuv",
        "asdaasfasfdasdf",
        "aaaaaaaaaa"
    ]

    sorted_via_function = sorted(my_list, key=str_to_len)
    print(sorted_via_function)
    my_list.sort(key=lambda item: len(item), reverse=True)
    print(my_list)


if __name__ == "__main__":
    main()
