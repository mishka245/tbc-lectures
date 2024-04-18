def main():
    my_list = [0, 9, 8, 7]
    my_tuple = (("Mikheil", 27), 123, "Python", my_list)
    print(my_tuple)
    my_list[0] = 26
    print(my_tuple)
    my_list.append(90)
    my_list.append(123)
    print(my_tuple)


if __name__ == "__main__":
    main()
