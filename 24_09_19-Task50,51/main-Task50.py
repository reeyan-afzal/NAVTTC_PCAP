# Task 50 - Multiple Inheritance

class Animal:
    pass


class Mammal(Animal):
    pass


class Bird(Animal):
    pass


class Bat(Mammal, Bird):
    pass


def print_base(cls):
    print('(', end=' ')
    for x in cls.__bases__:
        print(x.__name__, end=' ')
    print(')')


bat = Bat()
print_base(Animal)
print_base(Mammal)
print_base(Bird)
print_base(Bat)
