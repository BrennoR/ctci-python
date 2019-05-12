# Stack of Plates
from stack import Stack


class StackOfPlates:
    def __init__(self, threshold):
        self.stacks = []
        self.stacks.append(Stack())
        self.sizes = [0]
        self.threshold = threshold

    def push(self, item):
        if self.sizes[self.current_stack()] == self.threshold:
            self.stacks.append(Stack())
            self.sizes.append(0)

        self.stacks[self.current_stack()].push(item)
        self.sizes[self.current_stack()] += 1

    def pop(self):
        if self.sizes[self.current_stack()] == 0:
            self.stacks.pop()
            self.sizes.pop()

        self.sizes[self.current_stack()] -= 1
        return self.stacks[self.current_stack()].pop()

    def popAt(self, index):
        if self.stacks[index].isEmpty():
            if index == self.current_stack():
                self.pop()
            else:
                raise Exception("The stack is empty")
        else:
            self.sizes[index] -= 1
            return self.stacks[index].pop()

    def current_stack(self):
        return len(self.stacks) - 1


if __name__ == "__main__":
    plates = StackOfPlates(3)
    plates.push(1)
    plates.push(2)
    plates.push(3)
    plates.push(4)
    plates.push(5)
    plates.push(6)
    plates.push(7)
    plates.push(8)
    plates.push(9)
    plates.pop()
    plates.pop()
    plates.push(9)
    plates.pop()
    plates.popAt(1)
    plates.push(2)
    plates.popAt(0)
    plates.popAt(1)

    for i in range(3):
        print(plates.stacks[i].items)
