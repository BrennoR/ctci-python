# List of Depths
from collections import deque


class LinkedListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Time - O(N), Space - O(N)
def list_of_depths(root):
    if not root:
        return []

    queue = deque()
    queue.append(root)
    lof = []

    while queue:
        depth_len = len(queue)
        dummy = LinkedListNode(0)
        cur = dummy
        for _ in range(depth_len):
            node = queue.popleft()
            cur.next = LinkedListNode(node.value)
            cur = cur.next
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        lof.append(dummy.next)

    return lof


if __name__ == '__main__':

    # perfect binary tree
    tree_1 = TreeNode(0)
    tree_1.left = TreeNode(1)
    tree_1.right = TreeNode(2)
    tree_1.left.left = TreeNode(3)
    tree_1.left.right = TreeNode(4)
    tree_1.right.left = TreeNode(5)
    tree_1.right.right = TreeNode(6)

    # unbalanced binary tree
    tree_2 = TreeNode(0)
    tree_2.left = TreeNode(1)
    tree_2.right = TreeNode(2)
    tree_2.left.left = TreeNode(3)
    tree_2.left.right = TreeNode(4)
    tree_2.left.left.left = TreeNode(5)
    tree_2.left.left.right = TreeNode(6)
    tree_2.left.right.right = TreeNode(7)

    # single node tree
    tree_3 = TreeNode(0)

    # empty/null tree
    tree_4 = None

    lof_1 = list_of_depths(tree_1)
    lof_2 = list_of_depths(tree_2)
    lof_3 = list_of_depths(tree_3)
    lof_4 = list_of_depths(tree_4)

    lofs = [lof_1, lof_2, lof_3, lof_4]
    for lof, num in zip(lofs, range(1, 5)):
        print('=' * 40, 'lof - {}'.format(num), '=' * 40)
        for ll, depth in zip(lof, range(0, len(lof))):
            print('Depth {}:'.format(depth), end='\t')
            cur = ll
            while cur:
                print(cur.value, end='\t')
                cur = cur.next
            print('')
