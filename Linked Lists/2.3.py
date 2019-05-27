# Delete Middle Node

import importlib
structures = importlib.import_module('linked-list')

ll = structures.LinkedList(header=structures.Node(1))
ll.add_node(2)
ll.add_node(3)
ll.add_node(4)
ll.add_node(5)

ll.traverse()


# O(1)
def del_middle(node):
    if node is None or node.next is None:
        return False

    node.val = node.next.val
    node.next = node.next.next
    return True


three_node = ll.header.next.next
del_middle(three_node)
ll.traverse()
