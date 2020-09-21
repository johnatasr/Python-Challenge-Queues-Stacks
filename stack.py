
class StackPopException(Exception):
    def __init__(self):
        self.message = "The stack is empty"

    def __str__(self):
        if self.message:
            return 'StackPopException, {0} '.format(self.message)
        else:
            return 'StackPopException has been raised'


class StackPushException(Exception):
    def __init__(self):
        self.message = "The stack is full"

    def __str__(self):
        if self.message:
            return 'StackPushException, {0} '.format(self.message)
        else:
            return 'StackPushException has been raised'


class StackPeekException(Exception):
    def __init__(self):
        self.message = "The stack is empty"

    def __str__(self):
        if self.message:
            return 'StackPushException, {0} '.format(self.message)
        else:
            return 'StackPushException has been raised'


class Stack:
    def __init__(self):
        self.__size = 1000                      # Length of stack
        self.items = [None] * self.__size       # A list with None values to be used in stack
        self.top = -1                           # Top of stack

    # Checks if is empty
    def is_empty(self) -> bool:
        return True if self.top < 0 else False

    # Add elements in stack without validation
    def add(self, i) -> None:
        self.top = self.top + 1
        self.items[self.top] = i
        print(f'Added: {i}')

    # Add elements in the top of stack
    def push(self, i) -> None:
        if self.top >= (self.__size - 1):
            raise StackPushException()
        else:
            self.top += 1
            self.items[self.top] = i
            print(f'Pushed into stack: {i}')

    # Remove the last element added in stack
    def pop(self):
        if self.top < 0:
            raise StackPopException()
        else:
            poped = self.items[self.top]
            del self.items[self.top]
            self.items = self.items + [None]
            self.top -= 1
            print(f'Removed: {poped}')
            return poped

    # Returns a element in top of stack
    def peek(self):
        if self.top < 0:
            raise StackPeekException()
        else:
            return self.items[self.top]

    # Length of stack
    def __len__(self) -> int:
        return self.top + 1

    # A string representation of class
    def __str__(self) -> str:
        if self.top < 0:
            return str("")
        else:
            stack_str = ''
            for index in enumerate(range(self.top, -1, -1)):
                if index[0] > 0:
                    stack_str = stack_str + f' -> {self.items[index[1]]}'
                else:
                    stack_str = stack_str + f'{self.items[index[1]]}'
            return f"{stack_str}"




if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(1.5)
    stack.push('Teste')
    stack.push(Stack)
    stack.push(lambda x: x)
    stack.push({})
    stack.push([])
    stack.push(None)

    print(stack)
    print(f'Is empty ?  {stack.is_empty()}')
    print(len(stack))

    poped = stack.pop()
    print(len(stack))

    peek = stack.peek()
    print(peek)




