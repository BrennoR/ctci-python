# Palindrome
# TODO: IMPLEMENT RECURSIVE APPROACH

import importlib
structures = importlib.import_module('linked-list')

ll1 = structures.LinkedList(header=structures.Node('a'))
ll1.add_node('b')
ll1.add_node('a')
ll1.add_node('b')
ll1.add_node('a')

ll1.traverse()

ll2 = structures.LinkedList(header=structures.Node('b'))
ll2.add_node('c')
ll2.add_node('c')
ll2.add_node('b')

ll2.traverse()

ll3 = structures.LinkedList(header=structures.Node('b'))
ll3.add_node('a')
ll3.add_node('c')
ll3.add_node('b')


# Time - O(N), Space - O(N)
def palindrome(ll):
    cur = ll.header
    arr = []
    while cur is not None:
        arr.append(cur.val)
        cur = cur.next

    start = 0
    end = len(arr) - 1

    while start < end:
        if arr[start] != arr[end]:
            return False
        start += 1
        end -= 1

    return True


# Time - O(N), Space - O(N) [N/2 specifically]
def palindrome_2(ll):
    length = 0
    head = ll.header

    if head is None:
        return True

    runner = head
    while runner is not None:
        length += 1
        runner = runner.next

    stack = []
    cur = head
    for _ in range(length // 2):
        stack.append(cur.val)
        cur = cur.next

    if length % 2 != 0:
        cur = cur.next

    while stack:
        if cur.val != stack.pop():
            return False
        cur = cur.next

    return True


print(palindrome_2(ll1))
print(palindrome_2(ll2))
print(palindrome_2(ll3))
