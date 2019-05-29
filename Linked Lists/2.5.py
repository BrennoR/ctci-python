# Sum Lists
# TODO: IMPLEMENT FOLLOW UP

import importlib
structures = importlib.import_module('linked-list')

ll = structures.LinkedList(header=structures.Node(1))
ll.add_node(7)
ll.add_node(8)

ll.traverse()

ll2 = structures.LinkedList(header=structures.Node(6))
ll2.add_node(8)
ll2.add_node(5)

ll2.traverse()


# Time - O(max(|ll_1|, |ll_2|), Space - O(max(|ll_1|, |ll_2|) + 1)
def sum_lists(ll_1, ll_2):
    cur_1 = ll_1.header
    cur_2 = ll_2.header
    ll_3 = structures.Node(0)
    res = ll_3
    carry = 0
    while cur_1 is not None or cur_2 is not None or carry:
        value = carry
        if cur_1:
            value += cur_1.val
            cur_1 = cur_1.next
        if cur_2:
            value += cur_2.val
            cur_2 = cur_2.next
        val = value % 10
        carry = value // 10
        ll_3.next = structures.Node(val)
        ll_3 = ll_3.next

    return res.next


new_1 = sum_lists(ll, ll2)
while new_1 is not None:
    print(new_1.val, end='\t')
    new_1 = new_1.next


# FOLLOW UP
def sum_lists_2(ll_1, ll_2):
    pass
