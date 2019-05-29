# Stack min


class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, element):
        min = self.getMin(element)
        self.stack.append((element, min))

    def pop(self):
        if self.isEmpty():
            raise Exception("The stack is empty")
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            raise Exception("The stack is empty")
        return self.stack[-1][0]

    def getMin(self, element):
        if self.isEmpty() or element < self.stack[-1][1]:
            return element
        else:
            return self.stack[-1][1]

    def min(self):
        if self.isEmpty():
            raise Exception("The stack is empty")
        else:
            return self.stack[-1][1]

    def isEmpty(self):
        return len(self.stack) == 0


class MinStack2:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, element):
        if element <= self.min():
            self.min_stack.append(element)
        self.stack.append(element)

    def pop(self):
        if self.peek() <= self.min():
            self.min_stack.pop()
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            raise Exception("The stack is empty")
        return self.stack[-1]

    def min(self):
        if self.isEmpty():
            return float('inf')     # Also serves as an error value (stack is empty -> no min)
        else:
            return self.min_stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0


s = MinStack()
s.push(10)
s.push(8)
s.push(7)
s.push(6)
s.push(90)
s.push(2)
s.push(37)
s.push(20)
s.push(1)
s.pop()
s.pop()
s.pop()
print(s.stack)
print(s.min())

s.pop()
print(s.stack)
print(s.min())
