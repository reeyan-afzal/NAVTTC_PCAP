# Task 42 - Count Stack


class Stack:
    """Parent Class"""

    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

    def return_stack_list(self):
        return self.__stack_list


class ChildStack(Stack):
    """Child Class"""
    def __init__(self):
        super().__init__()
        self._sum = 0
        self._count = 0

    def push(self, val):
        super().push(val)
        self._sum += val
        self._count += 1

    def pop(self):
        return super().pop()

    def return_sum(self):
        return self._sum

    def return_count(self):
        return self._count

    def display_stack(self):
        elements = ", ".join([str(self.pop()) for _ in range(len(self.return_stack_list()))])
        return elements


stack = ChildStack()
try:
    for i in range(100):
        stack.push(i)
except KeyboardInterrupt:
    exit()
print("\nThe Stack consists: [" + stack.display_stack() + "]")
print("The sum of the Stack is:", stack.return_sum())
print("The elements count in the Stack is:", stack.return_count())
