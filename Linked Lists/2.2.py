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
    k_runner = ll.header
    end_runner = k_runner

    for i in range(k - 1):
        end_runner = end_runner.next

    while end_runner.next is not None:
        k_runner = k_runner.next
        end_runner = end_runner.next

    return k_runner.val


ll.traverse()
print(kth_to_last(ll, 7))
