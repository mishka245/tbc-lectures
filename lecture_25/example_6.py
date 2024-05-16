# ფუნქცია
# მეთოდი
import random


class MyTuple:
    def __init__(self):
        self.data = tuple()
        print(self.data)
        self.filled = False

    def fill(self):
        for _ in range(20):
            self.data += (random.randint(10, 1000),)

        self.filled = True

    def average(self):
        # if not self.filled:
        #     raise ValueError("Data structure is not filled")
        if not self.filled:
            self.fill()
        return sum(self.data) / len(self.data)

    def odd(self) -> tuple:
        if not self.filled:
            self.fill()
        result = []
        for element in self.data:
            if element % 2 == 1:
                result.append(element)
        return tuple(result)

    def even(self) -> tuple:
        if not self.filled:
            self.fill()
        result = []
        for element in self.data:
            if element % 2 == 0:
                result.append(element)
        return tuple(result)


def main():
    my_tuple = MyTuple()
    # my_tuple.fill()
    print("data", my_tuple.data)
    print("average", my_tuple.average())
    print("odd", my_tuple.odd())
    print("even", my_tuple.even())


if __name__ == "__main__":
    main()
