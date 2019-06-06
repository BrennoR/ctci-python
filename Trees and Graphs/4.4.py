# Check Balanced


class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Time - O(N), Space - O(H)
def check_height(node):
    if not node:
        return -1

    left_height = check_height(node.left)
    if left_height == float('-inf'):
        return float('-inf')

    right_height = check_height(node.right)
    if right_height == float('-inf'):
        return float('-inf')

    if abs(left_height - right_height) > 1:
        return float('-inf')
    else:
        return max(left_height, right_height) + 1


def check_balanced(root):
    return check_height(root) != float('-inf')


if __name__ == '__main__':

    # balanced tree
    tree_1 = TreeNode(0)
    tree_1.left = TreeNode(1)
    tree_1.right = TreeNode(2)
    tree_1.right.left = TreeNode(3)
    tree_1.right.right = TreeNode(4)

    # unbalanced tree
    tree_2 = TreeNode(0)
    tree_2.left = TreeNode(1)
    tree_2.right = TreeNode(2)
    tree_2.right.left = TreeNode(3)
    tree_2.right.left.right = TreeNode(4)

    # single node tree
    tree_3 = TreeNode(0)

    # null tree
    tree_4 = None

    print(check_balanced(tree_1))
    print(check_balanced(tree_2))
    print(check_balanced(tree_3))
    print(check_balanced(tree_4))
