# ფუნქცია
# მეთოდი
import random


class MyTuple:
    def __init__(self):
        self.data = tuple()
        print(self.data)

    def fill(self):
        for _ in range(20):
            self.data += (random.randint(10, 1000),)

    def average(self):
        return sum(self.data) / len(self.data)

    def odd(self) -> tuple:
        result = []
        for element in self.data:
            if element % 2 == 1:
                result.append(element)
        return tuple(result)

    def even(self) -> tuple:
        result = []
        for element in self.data:
            if element % 2 == 0:
                result.append(element)
        return tuple(result)


def main():
    my_tuple = MyTuple()
    my_tuple.fill()
    print("data", my_tuple.data)
    print("average", my_tuple.average())
    print("odd", my_tuple.odd())
    print("even", my_tuple.even())


if __name__ == "__main__":
    main()
