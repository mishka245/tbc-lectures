def remove_duplicates(elements: list) -> list:
    return list(set(elements))


def main():
    l = [1, 2, 3, 1, 2, 3, 1, 2, 3]
    print(remove_duplicates(l))


if __name__ == "__main__":
    main()
