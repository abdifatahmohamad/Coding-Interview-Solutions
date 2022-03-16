# Incomplete solution

class MaxStack:
    def __init__(self):
        self.stack = []
        self.maxStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.maxStack or val > self.maxStack[- 1][0]:
            self.maxStack.append([val, 1])
        elif val == self.maxStack[- 1][0]:
            self.maxStack[- 1][1] += 1
        else:
            self.maxStack.append(self.maxStack[- 1])

    def pop(self) -> int:
        # if not self.maxStack or self.stack:
        #     return
        if self.maxStack[- 1][0] == self.stack[- 1]:
            self.maxStack[- 1][1] -= 1
        if self.maxStack[- 1][1] == 0:
            del self.maxStack[- 1]
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        if self.maxStack:
            return self.maxStack[- 1][0]

    def popMax(self) -> int:
        if self.maxStack:
            return self.maxStack.pop()[0]


# Your MaxStack object will be instantiated and called as such:
obj = MaxStack()
obj.push(7)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.peekMax()
param_5 = obj.popMax()
