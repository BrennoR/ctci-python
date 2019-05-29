# Three in One
# TODO: Implement dynamic stack sizes solution


# Fixed sizes implementation
class ThreeInOne:

    def __init__(self, stack_size):
        self.arr = [None] * stack_size * 3  # O(N)
        self.sizes = [0, 0, 0]
        self.stack_size = stack_size

    # O(1)
    def push(self, stack, element):
        if self.isFull(stack):
            raise Exception("The stack is full")
        self.arr[self.getTopIndex(stack) + 1] = element
        self.sizes[stack] += 1

    # O(1)
    def pop(self, stack):
        if self.isEmpty(stack):
            raise Exception("The stack is empty")
        self.sizes[stack] -= 1
        val = self.arr[self.getTopIndex(stack) + 1]
        self.arr[self.getTopIndex(stack) + 1] = None
        return val

    # O(1)
    def peek(self, stack):
        if self.isEmpty(stack):
            raise Exception("The stack is empty")
        return self.arr[self.getTopIndex(stack)]

    def getTopIndex(self, stack):
        return self.sizes[stack] + stack * self.stack_size - 1

    # O(1)
    def isEmpty(self, stack):
        return self.sizes[stack] == 0

    # O(1)
    def isFull(self, stack):
        return self.sizes[stack] == self.stack_size


if __name__ == "__main__":
    stack = ThreeInOne(3)
    print(stack.arr)
    stack.push(0, 10)
    print(stack.arr)
    stack.push(0, 20)
    print(stack.arr)
    print(stack.pop(0))
    print(stack.arr)
    print(stack.pop(0))
    print(stack.arr)
    stack.push(1, 11)
    stack.push(1, 22)
    print(stack.arr)
    stack.push(2, 33)
    stack.push(2, 44)
    print(stack.arr)
