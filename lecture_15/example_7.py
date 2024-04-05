def is_palindrome(text) -> bool:
    n = len(text)
    for i in range(0, n // 2):
        if text[i] != text[n - i - 1]:
            return False
    return True


def is_palindrome_reversed_indices(text) -> bool:
    n = len(text)
    for i in range(0, n // 2):
        if text[i] != text[-i - 1]:
            return False
    return True


def main():
    print("is palindrome `radar`", is_palindrome("radar"), is_palindrome_reversed_indices("radar"))
    print("is palindrome `test`", is_palindrome("test"), is_palindrome_reversed_indices("test"))
    print("is palindrome `level`", is_palindrome("level"), is_palindrome_reversed_indices("level"))


if __name__ == "__main__":
    main()
