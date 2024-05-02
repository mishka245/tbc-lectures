def my_func(lst, number):
    assert type(lst) == list, "argument is not list"

    new_lst = []
    for elem in lst:
        try:
            new_lst.append(elem/number)
        except ZeroDivisionError:
            print("Zero division")
            new_lst.append("Err")

    return new_lst

try:
    result = my_func([2, 4, 6, 8], 0)
    print(result)
except AssertationError:
    print("Can't call my_func")