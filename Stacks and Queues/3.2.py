# Stack min
from stack import Stack


# pop, push, min - O(1)
class MinStack(Stack):
    def __init__(self):
        super().__init__()
        self.min = float('inf')

    def push(self, item):
        if item < self.min:
            self.min = item
        Stack.push(self, [item, self.min])

    def pop(self):
        Stack.pop(self)
        self.min = Stack.peek(self)[1]

    def minimum(self):
        if not Stack.isEmpty(self):
            return self.min
        else:
            raise Exception("Empty stack")


# solution better suited to save space
class MinStack_2(Stack):
    def __init__(self):
        super().__init__()
        self.s2 = Stack()
        self.min = float('inf')

    def push(self, item):
        Stack.push(self, item)
        if item <= self.min:
            self.s2.push(item)
            self.min = item

    def pop(self):
        if Stack.peek(self) == self.s2.peek():
            self.s2.pop()
            self.min = self.s2.peek()
        Stack.pop(self)

    def minimum(self):
        if not Stack.isEmpty(self):
            return self.s2.peek()
        else:
            raise Exception("Empty stack")


s = MinStack_2()
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
print(s.items)
print(s.s2.items)

print(s.minimum())
