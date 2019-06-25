# Check Subtree


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Time - O(n + km), Space = O(log n + log m)
def check_subtree_helper(root, root2):
    if root and root2 and root.value == root2.value:
        return check_subtree_helper(root.left, root2.left) and check_subtree_helper(root.right, root2.right)
    elif not root and not root2:
        return True
    else:
        return False


def check_subtree(root, root2):
    if not root or not root2:
        return -1

    cur = root
    stack = []

    while True:
        if cur is not None:
            stack.append(cur)
            cur = cur.left
        elif stack:
            cur = stack.pop()

            if cur.value == root2.value and check_subtree_helper(cur, root2):
                return True

            cur = cur.right
        else:
            break

    return False


# Simple approach, Time - O(n * m), Space - O(n + m):
def preorder(root, node_list):
    if root:
        node_list.append(root.value)
        preorder(root.left, node_list)
        preorder(root.right, node_list)
    else:
        node_list.append('X')


def check_subtree_2(root, root2):
    preorder_1 = []
    preorder_2 = []
    preorder(root, preorder_1)
    preorder(root2, preorder_2)

    for idx, node in enumerate(preorder_1):
        if node == preorder_2[0] and preorder_1[idx:] == preorder_2:
            return True

    return False


if __name__ == '__main__':
    tree_1 = TreeNode(2)
    tree_1.left = TreeNode(1)
    tree_1.left.left = TreeNode(4)
    tree_1.left.right = TreeNode(5)
    tree_1.right = TreeNode(6)
    tree_1.right.left = TreeNode(7)
    tree_1.right.right = TreeNode(8)
    tree_1.right.right.left = TreeNode(9)
    tree_1.right.right.right = TreeNode(10)

    tree_2 = TreeNode(6)
    tree_2.left = TreeNode(7)
    tree_2.right = TreeNode(8)
    tree_2.right.left = TreeNode(9)
    tree_2.right.right = TreeNode(10)

    print(check_subtree(tree_1, tree_2))
    print(check_subtree(tree_1, None))

    print(check_subtree_2(tree_1, tree_2))
