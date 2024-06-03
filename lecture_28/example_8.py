# *args and **kwargs

def my_func(a, b, *args, test_var="local", **kwargs):
    print(a, b, args)
    print("test_var=", test_var, kwargs)
    print(kwargs.items())
    print(kwargs.keys())
    print(kwargs.values())


my_func(1, 2, 3, 4, 5, name='John', city='New York')
my_func(1, 3, 2, 4, 5, age=25, name='John', city='New York', test_var=123)
my_func(1, 3, 2, 4, 5, 6, 7, 8, age=25, name='John', city='New York', test_var=123)

# my_func(name='John', age=25, city='New York', 1, 2, 3, 4, 5)  # SyntaxError: positional argument follows keyword argument
