"""
გვაქვს რიცხვების სია, უნდა ვიპოვოთ უდიდე რიცხვი ამ სიაში და მისი ინდექსი
"""
import random

NUMBERS_COUNT = 100


def generate_numbers_list() -> list:
    result = []
    for i in range(NUMBERS_COUNT):
        result.append(random.randint(0, 1000))
    return result


def find_max_number_and_index(numbers: list) -> tuple[int, int]:
    max_number_index = 0
    max_number = numbers[max_number_index]
    for i in range(len(numbers)):
        if numbers[i] > max_number:
            max_number = numbers[i]
            max_number_index = i

    return max_number, max_number_index


def find_max_number_and_index_using_enumerator(numbers: list) -> tuple[int, int]:
    max_number_index = 0
    max_number = numbers[max_number_index]
    for index, number in enumerate(numbers):  # index, element from iterable
        if number > max_number:
            max_number = number
            max_number_index = index

    return max_number, max_number_index


def main():
    numbers = generate_numbers_list()
    max_number, max_number_index = find_max_number_and_index(numbers)
    print(numbers)
    # print(result)
    # print(type(result))
    print("Max number index", max_number_index)
    print("Max number is", max_number)

    max_number, max_number_index = find_max_number_and_index_using_enumerator(numbers)
    print("Max number index", max_number_index)
    print("Max number is", max_number)


if __name__ == "__main__":
    main()
