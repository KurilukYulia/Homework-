import math


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def __sub__(self, other):
        if isinstance(other, Circle) and self.radius == other.radius:
            return Point(self.x-other.x)
        else:
            return f'{math.fabs(self.x- other.x),math.fabs( self.y - other.y),math.fabs( self.radius - other.radius)}'


circle_1 = Circle(-1, 1, 5)
circle_2 = Circle(2, 2, 3)
circle_3 = circle_1 - circle_2
print(circle_3)
circle_4 = Circle(-1, 1, 3)
circle_5 = Circle(2, 2, 3)
circle_6 = circle_4 - circle_5
print(circle_6)
