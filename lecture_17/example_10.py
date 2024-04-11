
def avg(x, y):
    return (x + y) / 2

def main():
    l1 = [1, 2, 5, 12]
    l2 = [0, 4, 10, 10]

    for x in map(lambda a, b: (a + b) / 2, l1, l2):
        print(x)

    print("Using function")
    for x in map(avg, l1, l2):
        print(x)


if __name__ == "__main__":
    main()
