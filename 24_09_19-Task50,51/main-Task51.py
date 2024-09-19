# Task 51 - Set and Get Attributes

class MyClass:
    pass


obj = MyClass()
obj.a = 1
obj.b = 2
obj.i = 3
obj.i_real = 3.5
obj.i_integer = 4
obj.z = 5
print(obj.__dict__)


def incIntI(_obj):
    for name in obj.__dict__.keys():
        if name.startswith('i'):
            val = getattr(_obj, name)
            if isinstance(val, int):
                setattr(obj, name, val + 1)


incIntI(obj)
print(obj.__dict__)
