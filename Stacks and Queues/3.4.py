# Queue via Stacks


class myQueue:

    def __init__(self):
        self.enq_stack = []
        self.deq_stack = []

    def enqueue(self, element):
        self.enq_stack.append(element)

    def dequeue(self):
        if self.isEmpty():
            raise Exception("The queue is empty")
        self.fill_dequeue()
        return self.deq_stack.pop()

    def fill_dequeue(self):
        if len(self.deq_stack) == 0:
            while self.enq_stack:
                self.deq_stack.append(self.enq_stack.pop())

    def peek(self):
        if self.isEmpty():
            raise Exception("The queue is empty")
        self.fill_dequeue()
        return self.deq_stack[-1]

    def isEmpty(self):
        return len(self.enq_stack) == 0 and len(self.deq_stack) == 0


queue = myQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)

print(queue.isEmpty())
print(queue.dequeue())
print(queue.peek())
print(queue.dequeue())


