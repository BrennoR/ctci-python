# Intersection

import importlib
structures = importlib.import_module('linked-list')

intersection_node = structures.Node(100)
intersection_node.next = structures.Node(30)
intersection_node.next.next = structures.Node(40)
intersection_node.next.next.next = structures.Node(50)

ll = structures.LinkedList(header=structures.Node(1))
ll.add_node(8)
ll.add_node(7)
ll.add_node(5)
ll.add_node(node=intersection_node)

ll.traverse()

ll2 = structures.LinkedList(header=structures.Node(3))
ll2.add_node(5)
ll2.add_node(8)
ll2.add_node(5)
ll2.add_node(10)
ll2.add_node(2)
ll2.add_node(1)
ll2.add_node(node=intersection_node)

ll2.traverse()


# Time - ~O(|ll_1| + |ll_2|), Space - O(1)
def intersection(ll_1, ll_2):
    if ll_1 is None or ll_2 is None:
        return None

    cur_1 = ll_1.header
    cur_2 = ll_2.header
    while cur_1 != cur_2:
        if cur_1 is None:
            cur_1 = ll_2.header

        if cur_2 is None:
            cur_2 = ll_1.header

        cur_1 = cur_1.next
        cur_2 = cur_2.next

    return cur_1


# Time - ~O(|ll_1| + |ll_2|), Space - O(1)
def intersection_2(ll_1, ll_2):
    if ll_1 is None or ll_2 is None:
        return None

    cur_1 = ll_1.header
    cur_2 = ll_2.header
    len_1 = 1
    len_2 = 1
    while cur_1.next is not None:
        len_1 += 1
        cur_1 = cur_1.next

    while cur_2.next is not None:
        len_2 += 1
        cur_2 = cur_2.next

    if cur_1 != cur_2:
        return None

    if len_1 > len_2:
        runner_1 = ll_1.header
        runner_2 = ll_2.header
    else:
        runner_1 = ll_2.header
        runner_2 = ll_1.header

    for _ in range(abs(len_2 - len_1)):
        runner_1 = runner_1.next

    while runner_1 != runner_2:
        runner_1 = runner_1.next
        runner_2 = runner_2.next

    return runner_1


# Time - O(|ll_1| + |ll_2|), Space - O(|ll_1| + |ll_2|)
# behaves quite strangely
def intersection_3(ll_1, ll_2):
    set_1 = set()
    set_2 = set()
    cur_1 = ll_1.header
    cur_2 = ll_2.header
    while cur_1 is not None and cur_2 is not None:
        if cur_1 == cur_2 or cur_1 in set_2:
            return cur_1
        elif cur_2 in set_1:
            return cur_2

        set_1.add(cur_1)
        set_2.add(cur_2)
        cur_1 = cur_1.next
        cur_2 = cur_2.next

    while cur_1 is not None:
        if cur_1 in set_2:
            return cur_1

        cur_1 = cur_1.next

    while cur_2 is not None:
        if cur_2 in set_1:
            return cur_2

        cur_2 = cur_2.next


inter = intersection_3(ll, ll2)
print(inter.val)

