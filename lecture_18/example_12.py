def main():
    numbers = [("Mikheil", 27), ("Nona", 33), ("Giga", 19)]

    s = 0
    for name, age in numbers:
        print(age)
        s += age

    print(s)

if __name__ == "__main__":
    main()
