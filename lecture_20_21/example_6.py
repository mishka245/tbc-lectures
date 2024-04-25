my_dict = {"a": ["aardvark"], "b": ["baboon"], "c": ["coati", "cat"], "d": ["donkey", "dog", "dingo"]}


def find_max_value_key(d):
    max_value = []
    max_value_key = None
    for k, v in d.items():
        if len(v) > len(max_value):
            max_value = v
            max_value_key = k
    return max_value_key


def main():
    print("Max value key", find_max_value_key(my_dict))
    print("Max value key", max(my_dict.items(), key=lambda item: len(item[1]))[0])


if __name__ == "__main__":
    main()
