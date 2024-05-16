class Coordinate:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance(self, other: "Coordinate"):
        temp_x = (self.x - other.x) ** 2
        temp_y = (self.y - other.y) ** 2
        return (temp_x + temp_y) ** 0.5

    def __str__(self):
        return f"Coordinates [ {self.x}, {self.y} ]"


c_1 = Coordinate(3, 4)
t = str(c_1)
print("type(t)", type(t))
print("t = ", t)

print(c_1)

