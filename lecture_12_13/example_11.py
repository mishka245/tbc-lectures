first_row = "qwertyuiop"
first_row_crypted = "wertyuiopq"

second_row = "asdfghjkl"
second_row_crypted = "sdfghjkla"

third_row = "zxcvbnm"
third_row_crypted = "xcvbnmz"


def crypt(c, encrypt):
    if encrypt == "d":
        if c in first_row:
            index = first_row_crypted.index(c)
            return first_row[index]
        elif c in second_row:
            index = second_row_crypted.index(c)
            return second_row[index]
        elif c in third_row:
            index = third_row_crypted.index(c)
            return third_row[index]
    else:
        if c in first_row:
            index = first_row.index(c)
            return first_row_crypted[index]
        elif c in second_row:
            index = second_row.index(c)
            return second_row_crypted[index]
        elif c in third_row:
            index = third_row.index(c)
            return third_row_crypted[index]


def main():
    word = input("Enter first word: ")
    encrypt = input("Enter e or d: ")

    result = ""
    for c in word:
        res = crypt(c, encrypt)
        print(f"{c} -> {res}")
        result += res

    print(f"{word} -> {result}")


if __name__ == "__main__":
    main()
