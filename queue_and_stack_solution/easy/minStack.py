# Complete answer

from logging import raiseExceptions


class MinStack:
    min_stack = float("inf")

    def __init__(self):
        # Keep the truck the current minimum stack
        self.min_stack = float("inf")
        # Regular stack
        self.stack = []

    def push(self, val: int) -> None:
        if val <= self.min_stack:
            self.stack.append(self.min_stack)
            self.min_stack = val

        # Always bush the regular stack
        self.stack.append(val)

    def pop(self) -> None:
        top_stack = self.stack[len(self.stack) - 1]

        # Always pop off the regular stack
        self.stack.pop()
        if self.min_stack == top_stack:
            self.min_stack = self.stack[len(self.stack) - 1]
            self.stack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> float:
        return self.min_stack

    # Print stack using string representation
    def __str__(self) -> str:
        # print("Printing stack.")
        return " ".join(str(x) for x in self.stack)


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(2)
obj.push(3)
obj.pop()
obj.push(4)
obj.push(-1)
print("Top of the stack: ", obj.top())
obj.push(6)
obj.getMin()
obj.push(-2)
obj.pop()
print("The minimum of the stack: ", obj.getMin())

print("Printing the entire stack: ", obj)


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
