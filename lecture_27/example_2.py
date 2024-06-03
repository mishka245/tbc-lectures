class Test:
    bar = 1

    def __init__(self, x):
        self.foo = x

    def __str__(self):
        return f"Test({self.foo}), class var 'bar' = {self.bar}"


def main():
    a = Test("Kutaisi")
    b = Test("Zestafoni")
    print("a", a)
    print("b", b)
    Test.bar = 100
    c = Test("Samtredia")
    print("c", c)

    print("--------------")
    print("a", a)
    print("b", b)

    a.bar = 300
    print("--------------")
    print("c", c)

    print("a", a)
    print("b", b)

    Test.bar = 500
    print("--------------")
    print("a", a)


if __name__ == "__main__":
    main()
