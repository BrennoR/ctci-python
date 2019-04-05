class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self, header: Node):
        self.header = header

    def add_node(self, val):
        current_node = self.header
        if current_node is None:
            self.header = Node(val)
        else:
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = Node(val)

    def traverse(self):
        current_node = self.header
        while current_node is not None:
            print(current_node.val, end='\t')
            current_node = current_node.next
        print("")


if __name__ == "__main__":
    linked_list = LinkedList(header=Node(10))
    linked_list.add_node(20)
    linked_list.add_node(30)

    linked_list.traverse()

