my_dict = {"a": ["aardvark"], "b": ["baboon"], "c": ["coati", "cat"], "d": ["donkey", "dog", "dingo"]}

l = [[1, 2], [3, 4], [1, 2, 3, 4]]


def main():
    # print("sum of l", sum(l,))  # DOes not work
    print("list(map(len, l))", list(map(len, l)))
    print("sum(list(map(len, l)))", sum(list(map(len, l))))


if __name__ == "__main__":
    main()
