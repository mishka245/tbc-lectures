def is_palindrome(text) -> bool:
    if text == text[::-1]:
        return True
    return False


def is_palindrome_shorter(text) -> bool:
    return text == text[::-1]


def main():
    print("is palindrome `radar`", is_palindrome("radar"))
    print("is palindrome `test`", is_palindrome("test"))
    print("is palindrome `level`", is_palindrome("level"))

    print("is palindrome shorter `level`", is_palindrome_shorter("level"))


if __name__ == "__main__":
    main()
