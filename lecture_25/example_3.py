class Rectangle:
    def __init__(self, a: int, b: int):
        self.side_a = a
        self.side_b = b

    def info(self):
        return f"Rectangle({self.side_a}, {self.side_b})"

    def area(self) -> float:
        return self.side_a * self.side_b

    def perimeter(self):
        return 2 * (self.side_a + self.side_b)


r1 = Rectangle(3, 4)
r2 = Rectangle(10, 30)
print(r2.info(), "area ->", r2.area())

my_rectangles = [
    r1,
    r2,
    Rectangle(11, 12),
    Rectangle(1, 2)
]
print("*" * 100)
for r in my_rectangles:
    print(r.info(), r.area())
print("*" * 100)

test_type = Rectangle("10", [])
print(test_type)
print(type(test_type))
print(test_type.info())
print(test_type.area())




