def foo() -> int:
    return "Python"


def bar() -> str:
    return "123"


def main():
    result = foo()
    print(result[1])

    bar_result = bar()
    print(bar_result[1])


if __name__ == "__main__":
    main()
