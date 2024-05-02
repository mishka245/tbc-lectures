
def divide(a, b):
    return a - b


def test_divide():
    a_1 = 10
    b_1 = 5

    result = divide(a_1, b_1)
    correct_result = 2.0

    assert result == correct_result, "result isn't equal to expected value"


test_divide()