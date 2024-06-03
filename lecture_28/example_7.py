# Default values for function arguments

def my_function(a=1, b=2, c=3):
    print(a, b, c)


def foo(bar):  # bar is required positional argument
    print(bar)


# foo()  # TypeError: foo() missing 1 required positional argument: 'bar'

my_function()
my_function(10)
my_function(10, 20)
my_function(10, 20, 30)
my_function(c=30)
my_function(b=20)
my_function(c=30, b=20)
my_function(a=10, b=20, c=30)
