# Stack of Plates


class StackOfPlates:

    def __init__(self, capacity):
        self.stacks = [[]]
        self.capacity = capacity

    def push(self, element):
        if len(self.stacks[-1]) == self.capacity:
            self.stacks.append([element])
        else:
            self.stacks[-1].append(element)

    def pop(self):
        if self.isEmpty():
            raise Exception("The stack of plates is empty")
        if len(self.stacks[-1]) == 1 and len(self.stacks) > 1:
            return self.stacks.pop()[0]
        else:
            return self.stacks[-1].pop()

    def popAt(self, index):
        if index + 1 > len(self.stacks) or len(self.stacks[index]) == 0:
            raise Exception("Invalid index or this stack of plates is empty")
        elif index == len(self.stacks):
            return self.pop()
        else:
            return self.stacks[index].pop()

    def peek(self):
        if self.isEmpty():
            raise Exception("The stack of plates is empty")
        return self.stacks[-1][-1]

    def isEmpty(self):
        return self.stacks[-1] == []


# Implements rollover for popAt procedure
class StackOfPlates2:

    def __init__(self, capacity):
        self.stacks = [[]]
        self.capacity = capacity

    def push(self, element):
        if len(self.stacks[-1]) == self.capacity:
            self.stacks.append([element])
        else:
            self.stacks[-1].append(element)

    def pop(self):
        if self.isEmpty():
            raise Exception("The stack of plates is empty")
        if len(self.stacks[-1]) == 1 and len(self.stacks) > 1:
            return self.stacks.pop()[0]
        else:
            return self.stacks[-1].pop()

    def popAt(self, index):
        if index + 1 > len(self.stacks) or index < 0 or len(self.stacks[index]) == 0:
            raise Exception("Invalid index or the stack of plates is empty")
        elif index == len(self.stacks):
            return self.pop()
        else:
            val = self.stacks[index].pop()
            self.leftShift(index)
            return val

    def leftShift(self, index):
        i = index
        while i + 1 < len(self.stacks):
            self.stacks[i].append(self.stacks[i + 1].pop(0))
            i += 1

        if len(self.stacks[i]) == 0:
            self.stacks.pop()

    def peek(self):
        if self.isEmpty():
            raise Exception("The stack of plates is empty")
        return self.stacks[-1][-1]

    def isEmpty(self):
        return self.stacks[-1] == []


if __name__ == "__main__":
    plates = StackOfPlates2(3)
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
    plates.push(10)
    print(plates.stacks)
    plates.pop()
    print(plates.stacks)
    plates.popAt(1)
    print(plates.stacks)
    plates.push(2)
    print(plates.stacks)
    plates.popAt(0)
    print(plates.stacks)
    plates.popAt(1)

    print(plates.stacks)
