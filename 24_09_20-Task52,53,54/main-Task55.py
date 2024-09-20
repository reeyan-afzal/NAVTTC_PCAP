from math import pi


class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        raise NotImplementedError("Subclasses must implement the area method.")


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return pi * (self.radius ** 2)


def print_area(shape: Shape):
    print(f"The area of the {shape.name} is: {shape.area():.2f}")


rectangle = Rectangle(5, 10)
circle = Circle(7)

print_area(rectangle)
print_area(circle)
