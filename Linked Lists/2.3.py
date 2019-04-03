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
def delete_middle_node(middle_node):
    if middle_node is None or middle_node.next is None:
        return False

    middle_node.val = middle_node.next.val
    middle_node.next = middle_node.next.next
    return True


three_node = ll.header.next.next
delete_middle_node(three_node)
ll.traverse()
