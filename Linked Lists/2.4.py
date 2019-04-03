# Partition

import importlib
structures = importlib.import_module('linked-list')

ll = structures.LinkedList(header=structures.Node(1))
ll.add_node(8)
ll.add_node(7)
ll.add_node(5)
ll.add_node(3)
ll.add_node(4)
ll.add_node(10)

ll.traverse()


# O(N) time, O(N) space
def partition(linked_list, x):
    node = linked_list.header
    previous = []
    post = []

    while node is not None:
        if node.val < x:
            previous.append(node)
        else:
            post.append(node)
        node = node.next

    all = previous + post
    linked_list.header = all[0]
    node = linked_list.header

    for n in all[1:]:
        node.next = n
        node = node.next

    return ll


partition(ll, 5)
ll.traverse()
