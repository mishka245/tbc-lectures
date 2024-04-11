

def main():
    l1 = [1, 2, 5, 12]
    l2 = [0, 4, 10, 10]

    for x in map(lambda a, b: a / b, l2, l1):
        print(x)



if __name__ == "__main__":
    main()
