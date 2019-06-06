# Successor


class TreeNode:

    def __init__(self, val, parent=None):
        self.val = val
        self.parent = parent
        self.left = None
        self.right = None


# Time - O(H), Space - O(1)
def successor(node):
    if node.right:
        node = node.right
        while node.left:
            node = node.left

        return node.val

    while node.parent and node == node.parent.right:
        node = node.parent

    return node.parent


if __name__ == '__main__':

    tree_1 = TreeNode(5)
    tree_1.left = TreeNode(3, parent=tree_1)
    tree_1.left.right = TreeNode(4, parent=tree_1.left)
    tree_1.left.left = TreeNode(2, parent=tree_1.left)
    tree_1.right = TreeNode(7, parent=tree_1)
    tree_1.right.left = TreeNode(6, parent=tree_1.right)
    tree_1.right.right = TreeNode(8, parent=tree_1.right)

    print(successor(tree_1))

