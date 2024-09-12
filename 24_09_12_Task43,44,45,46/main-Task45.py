import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = float(x)
        self.__y = float(y)

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        # Calculate the distance from the current point to (x, y)
        return math.hypot(self.__x - x, self.__y - y)

    def distance_from_point(self, point):
        # Calculate the distance from the current point to another point
        return math.hypot(self.__x - point.getx(), self.__y - point.gety())


point1 = Point(0, 0)
point2 = Point(1, 1)

print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))
