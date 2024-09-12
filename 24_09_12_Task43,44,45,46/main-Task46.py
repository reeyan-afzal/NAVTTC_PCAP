import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__vertices = [vertice1, vertice2, vertice3]

    def __distance(self, point1, point2):
        return math.sqrt((point2.get_x() - point1.get_x()) ** 2 + (point2.get_y() - point1.get_y()) ** 2)

    def perimeter(self):
        d1 = self.__distance(self.__vertices[0], self.__vertices[1])
        d2 = self.__distance(self.__vertices[1], self.__vertices[2])
        d3 = self.__distance(self.__vertices[2], self.__vertices[0])
        return d1 + d2 + d3


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
