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

ll2 = structures.LinkedList(header=structures.Node(3))
ll2.add_node(5)
ll2.add_node(8)
ll2.add_node(5)
ll2.add_node(10)
ll2.add_node(2)
ll2.add_node(1)

ll2.traverse()


# Time - O(N), Space - O(N)
def partition(linklist, p):
    cur = linklist.header
    l1 = structures.Node(0)
    l2 = structures.Node(0)
    cur_l1 = l1
    cur_l2 = l2

    while cur is not None:
        if cur.val < p:
            cur_l1.next = cur
            cur_l1 = cur_l1.next
        else:
            cur_l2.next = cur
            cur_l2 = cur_l2.next
        cur = cur.next

    cur_l1.next = l2.next

    return l1.next


# Time - O(N), Space - O(N)
def partition_2(linked_list, x):
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


# Time - O(N), Space - O(1)
def partition_3(linklist, p):
    dummy = structures.Node(0)
    dummy.next = linklist.header
    cur = dummy.next
    while cur.next is not None:
        if cur.next.val < p:
            tmp = cur.next
            cur.next = cur.next.next
            tmp_2 = dummy.next
            dummy.next = tmp
            dummy.next.next = tmp_2
        else:
            cur = cur.next

    linklist.header = dummy.next
    return linklist


# Time - O(N), Space - O(1)
def partition_4(linklist, p):
    head = linklist.header
    cur = head
    while cur.next is not None:
        if cur.next.val < p:
            tmp = cur.next.next
            cur.next.next = head
            head = cur.next
            cur.next = tmp
        else:
            cur = cur.next

    linklist.header = head
    return linklist


partition_4(ll2, 5)
ll2.traverse()
