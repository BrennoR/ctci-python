# Remove Duplicates
import importlib
structures = importlib.import_module('linked-list')


ll = structures.LinkedList(header=structures.Node(10))
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


# O(N) time, O(N) space
def remove_duplicates_1(ll):
    values = {}

    node = ll.header
    while node.next is not None:
        if node.next.val in values:
            temp = node.next.next
            node.next.next = None
            node.next = temp
        else:
            values[node.next.val] = 1
            node = node.next


# without temporary buffer
# O(N^2) time, O(1) space

def remove_duplicates_2(ll):
    current = ll.header
    while current is not None:
        runner = current
        while runner.next is not None:
            if runner.next.val == current.val:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next


remove_duplicates_2(ll)
ll.traverse()

