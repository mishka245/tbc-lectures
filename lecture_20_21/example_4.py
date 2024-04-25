my_dict = {"a": ["aardvark"], "b": ["baboon"], "c": ["coati", "cat"], "d": ["donkey", "dog", "dingo"]}

# l = [[1, 2], [3, 4]]
# l = [["aardvark"], ["baboon"], ["coati", "cat"], ["donkey", "dog", "dingo"]] - d.values()
# l = [["aardvark"], ["baboon"], ["coati", "cat"], ["donkey", "dog", "dingo"]] - d.values()
# # ?
# len(l)
# len(my_dict.values())


def how_many(d):
    s = 0
    for v in d.values():
        s += len(v)
    return s


def how_many_using_map_and_sum(d):
    # return sum(list(map(len, d.values())))
    return sum(map(len, d.values()))


def main():
    print("Number of animals", how_many(my_dict))
    print("Number of animals map and sum", how_many_using_map_and_sum(my_dict))


if __name__ == "__main__":
    main()
