# Task 42 - Stack

class Stack:
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
    def __init__(self):
        super().__init__()
        self.__sum = 0

    def push(self, val):
        Stack.push(self, val)
        self.__sum += val

    def pop(self):
        return Stack.pop(self)

    def return_sum(self):
        return self.__sum

    def display_stack(self):
        elements = ''
        for _ in range(len(Stack.return_stack_list(self))):
            elements += str(self.pop()) + ', '
        return elements


stack = ChildStack()

while True:
    try:
        user_val = int(input("Enter the value to add in stack(only numbers): "))
        stack.push(user_val)
    except (ValueError, KeyboardInterrupt):
        break

print("\nThe Stack consists: ", stack.display_stack())
print("The sum of the Stack is:", stack.return_sum())

