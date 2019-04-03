# Three in One


# Fixed sizes implementation
class MultiStack:
    def __init__(self, num_stacks, stack_size):
        self.num_stacks = num_stacks
        self.array = [0] * num_stacks * stack_size
        self.sizes = [0] * num_stacks
        self.stack_size = stack_size

    def push(self, value, stack_num):
        if self.isFull(stack_num):
            raise Exception("This stack is full")
        self.sizes[stack_num] += 1
        self.array[self.indexOfTop(stack_num)] = value

    def pop(self, stack_num):
        if self.isEmpty(stack_num):
            raise Exception("This stack is empty")
        item = self.array[self.indexOfTop(stack_num)]
        self.array[self.indexOfTop(stack_num)] = 0
        self.sizes[stack_num] -= 1
        return item

    def peek(self, stack_num):
        if self.isEmpty(stack_num):
            raise Exception("This stack is empty")
        return self.array[self.indexOfTop(stack_num)]

    def isEmpty(self, stack_num):
        return self.sizes[stack_num] < 1

    def isFull(self, stack_num):
        return self.sizes[stack_num] >= self.stack_size

    def indexOfTop(self, stack_num):
        offset = stack_num * self.stack_size
        return offset + self.sizes[stack_num] - 1


if __name__ == "__main__":
    stack = MultiStack(3, 2)
    print(stack.array)
    stack.push(10, 0)
    print(stack.array)
    stack.push(20, 0)
    print(stack.array)
    print(stack.pop(0))
    print(stack.array)
    print(stack.pop(0))
    print(stack.array)
    stack.push(11, 1)
    stack.push(22, 1)
    print(stack.array)
    stack.push(33, 2)
    stack.push(44, 2)
    print(stack.array)
