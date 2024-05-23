class Point(object):
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance(self, other: "Point"):
        temp_x = (self.x - other.x) ** 2
        temp_y = (self.y - other.y) ** 2
        return (temp_x + temp_y) ** 0.5

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        if not isinstance(other, Point):
            raise ValueError("Can only ad Point type")
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Point(new_x, new_y)

    def __eq__(self, other):  # ==
        return self.x == other.x and self.y == other.y


p1 = Point(0, 0)
p2 = Point(1, 1)

p1.x = 120
print(p1.x)

print(str(p1))
print(str(p2))

new_point = p1 + p2

print(new_point)

print(p1 == p2)
