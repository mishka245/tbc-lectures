"""

თუ ფუნქციას გადავეცით სიები
[1,  3, 10]
[0, 4, 7, 9]
უნდა დააბრუნოს
[0, 1, 3, 4, 7, 9, 10]

"""


def merge(list_1, list_2):
    i = 0
    j = 0
    result = []
    while i < len(list_1) and j < len(list_2):
        if list_1[i] < list_2[j]:
            result.append(list_1[i])
            i += 1
        else:
            result.append(list_2[j])
            j += 1

    while i < len(list_1):
        result.append(list_1[i])
        i += 1

    while j < len(list_2):
        result.append(list_2[j])
        j += 1

    return result


def main():
    list_1 = [1, 3, 10]   # m
    list_2 = [0, 4, 7, 9]  # n
    result = merge(list_1, list_2)
    print(list_1)
    print(list_2)
    print(result)  # O (m + n)
    # O (nlogn)
    # O (n^2)

if __name__ == "__main__":
    main()
