def main():
    l1 = [1, 2, 5, 12]
    l2 = [0, 4, 10, 10]

    for t in filter(lambda x: x != 0, l2):
        print(t)


if __name__ == "__main__":
    main()
