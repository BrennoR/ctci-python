# Return Kth to Last
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


# O(N) time, O(1) space
def kth_to_last(ll, k):
    cur = ll.header
    runner = cur

    for _ in range(k):
        if runner is None:
            return None
        runner = runner.next

    while runner is not None:
        cur = cur.next
        runner = runner.next

    return cur.val


ll.traverse()
print(kth_to_last(ll, 2))
