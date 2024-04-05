def is_palindrome(text) -> bool:
    if len(text) <= 1:
        return True
    if text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])


def is_palindrome_shorter(text) -> bool:
    if len(text) <= 1:
        return True
    return text[0] == text[-1] and is_palindrome_shorter(text[1:-1])


def main():
    print("is palindrome `radar`", is_palindrome("radar"))
    print("is palindrome `test`", is_palindrome("test"))
    print("is palindrome `level`", is_palindrome("level"))

    print("is palindrome short `level`", is_palindrome_shorter("level"))
    print("is palindrome short `test`", is_palindrome_shorter("test"))


if __name__ == "__main__":
    main()
