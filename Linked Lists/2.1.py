# Remove Dups
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
def remove_dups(linklist):
    cur = linklist.header
    elements = set()
    elements.add(cur.val)
    while cur.next is not None:
        if cur.next.val in elements:
            cur.next = cur.next.next
        else:
            elements.add(cur.next.val)
            cur = cur.next

    return linklist.header


# without temporary buffer
# O(N^2) time, O(1) space

def remove_dups_2(linklist):
    cur = linklist.header
    while cur is not None:
        runner = cur
        while runner.next is not None:
            if cur.val == runner.next.val:
                runner.next = runner.next.next
            else:
                runner = runner.next
        cur = cur.next

    return linklist.header


remove_dups_2(ll)
ll.traverse()

