class MinStack:
    def __init__(self):
        self.stack = []
        self.minm = None

    def push(self, value):
        if not self.stack:
            self.stack.append(value)
            self.minm = value
        else:
            if value < self.minm:
                self.stack.append(2*value - self.minm)
                self.minm = value
            else:
                self.stack.append(value)
    
    def pop(self):
        if not self.stack:
            return None
        else:
            popped = self.stack.pop()
            if popped>self.minm:
                return popped
            else:
                self.minm = 2*self.minm - popped
                return popped
    
    def top(self):
        if not self.stack:
            return None
        else:
            return self.stack[-1]

    def getMin(self):
        if not self.stack:
            return None
        else:
            return self.minm

stack = MinStack()
stack.push(3)
stack.push(5)
print(stack.getMin())
stack.push(2)
stack.push(1)
print(stack.getMin())
stack.push(1)
stack.push(-1)
print(stack.getMin())
stack.pop()
stack.pop()
stack.pop()
print(stack.getMin())
