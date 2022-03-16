# Complete answer

from logging import raiseExceptions


class MinStack:
    min = float("inf")

    def __init__(self):
        self.stack = []
        self.min = float("inf")

    def push(self, val):
        if val <= self.min:
            self.stack.append(self.min)
            self.min = val
        else:
            self.stack.append(val)

    def pop(self):
        stack_top = self.stack[len(self.stack) - 1]
        self.stack.pop()
        if self.min == stack_top:
            self.min = self.stack[len(self.stack) - 1]
            self.stack.pop()

    def top(self):
        return self.stack[len(self.stack) - 1]

    def getMin(self):
        return self.min


obj = MinStack()

obj.push(-2)
obj.push(-1)
obj.push(9)
obj.push(-34)
obj.push(-3)

print(obj.getMin())


###############################################################

# Incomplete answer


class MinStack:
    min = float('inf')

    def __init__(self, length):
        def __init__(self, length):
            # Creating an empty stack
            self.__length = length
            self.__S = [0] * length

            self.__min = float('inf')

        self.__top = -1

    def is_empty(self) -> bool:
        return self.__top == -1

    def push(self, val: int) -> None:
        self.__top += 1
        if self.__top == self.__length:
            raiseExceptions("Stack Overflow!")
        else:
            self.__S[self.__top] = val

    def pop(self) -> None:
        if self.is_empty():
            raiseExceptions("Stack is empty.")
        else:
            stack_top = self.__S[self.__top]
            self.__S[self.__top] = 0
            self.__top -= 1
            return stack_top

    def top(self) -> int:
        if self.is_empty():
            raiseExceptions("Stack is empty.")
        else:
            return self.__S[self.__top]

    def getMin(self) -> int:
        return self.__min


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
