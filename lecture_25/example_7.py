class Coordinate:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance(self, other: "Coordinate"):
        temp_x = (self.x - other.x) ** 2
        temp_y = (self.y - other.y) ** 2
        return (temp_x + temp_y) ** 0.5


c_1 = Coordinate(0, 0)
# c_2 = Coordinate(3, 4)
# print(c_2.x)
# print(c_1.x)
# print(c_1.distance(c_2))
print(c_1.distance(Coordinate(3, 4)))
