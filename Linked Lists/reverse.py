# Reverse a linked list
import importlib
structures = importlib.import_module('linked-list')

ll = structures.LinkedList(structures.Node(10))
ll.add_node(20)
ll.add_node(30)
ll.add_node(40)
ll.add_node(20)
ll.add_node(30)
ll.add_node(50)
ll.add_node(80)
ll.add_node(100)
ll.add_node(50)

ll.traverse()


# O(N), O(1)
def reverse(linked_list):
    prev = None
    current = linked_list.header
    while current is not None:
        temp = current.next
        current.next = prev
        prev = current
        current = temp

    linked_list.header = prev
    linked_list.traverse()

    return linked_list


# Stack implementation
def reverse_2(linked_list):
    stack = []
    current = linked_list.header
    while current is not None:
        stack.append(current)
        current = current.next

    linked_list.header = stack.pop()
    node = linked_list.header
    while stack:
        node.next = stack.pop()
        node.next.next = None
        node = node.next

    linked_list.traverse()

    return linked_list


reverse(ll)
reverse_2(ll)
