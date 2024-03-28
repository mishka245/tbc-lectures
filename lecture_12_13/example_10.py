def check_anagram(first, second):
    is_anagram = True
    for c in first:
        if first.count(c) != second.count(c):
            is_anagram = False
            break
    return is_anagram

def main():
    first = input("Enter first word: ")
    second = input("Enter second word: ")

    print(check_anagram(first, second) and check_anagram(second, first))

if __name__ == "__main__":
    main()
