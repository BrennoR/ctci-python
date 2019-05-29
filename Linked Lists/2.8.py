# Loop Detection

import importlib
structures = importlib.import_module('linked-list')

loop_node_f = structures.Node(100)
loop_node_r = structures.Node(200)
loop_node_f.next = loop_node_r

ll = structures.LinkedList(header=structures.Node(1))
ll.add_node(8)
ll.add_node(node=loop_node_r)
ll.add_node(5)
ll.add_node(node=loop_node_f)

ll2 = structures.LinkedList(header=structures.Node(3))
ll2.add_node(5)
ll2.add_node(8)
ll2.add_node(5)
ll2.add_node(10)
ll2.add_node(2)
ll2.add_node(1)


# Hare and Turtle Method
# Time - O(N), Space - O(1)
def loop_detection(linklist):
    if linklist is None:
        return None

    slow = linklist.header
    fast = linklist.header
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    if fast is None or fast.next is None:
        return None

    slow = linklist.header
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow


# Time - O(N), Space - O(N)
def loop_detection_2(linklist):
    cur = linklist.header
    nodes = set()
    while cur is not None:
        if cur in nodes:
            return cur
        nodes.add(cur)
        cur = cur.next

    return None


print(loop_detection(ll).val)

