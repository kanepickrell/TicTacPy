### Random Scripts

class Point:
    defaultColor = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(5,2)
print(point.defaultColor)
print(Point.defaultColor)
point.draw()

another = Point(3,4)
another.draw()