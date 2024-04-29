def read_file(filename) -> str:
    file = open(filename, "r")
    file_content = file.read()
    file.close()
    return file_content


def count_lines(text):
    return text.count("\n")


def count_words(text):
    # return len(text.split(" "))
    counter = 0
    for word in text.split(" "):
        if word.strip():
            counter += 1
    return counter


def count_words_with_comprehension(text):
    return len([word for word in text.split(" ") if word.strip()])


def main():
    file_content = read_file("example_4.txt")
    print("Lines count - ", count_lines(file_content))
    print("Words count - ", count_words(file_content))
    print("Words count using comprehension- ", count_words_with_comprehension(file_content))
    print("Symbols count - ", len(file_content))


if __name__ == "__main__":
    main()
