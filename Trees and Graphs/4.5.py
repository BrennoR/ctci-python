# Validate BST


class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Time - O(N), Space - O(H)
def validate_bst(root, min=float('-inf'), max=float('inf')):
    if not root:
        return True
    if root.val <= min or root.val > max:
        return False

    return validate_bst(root.left, min, root.val) and validate_bst(root.right, root.val, max)


if __name__ == '__main__':

    # BST
    tree_1 = TreeNode(5)
    tree_1.left = TreeNode(3)
    tree_1.left.right = TreeNode(4)
    tree_1.left.left = TreeNode(2)
    tree_1.right = TreeNode(7)
    tree_1.right.left = TreeNode(6)
    tree_1.right.right = TreeNode(8)
    # tree_1.left.right.right = TreeNode(1000)      # False Check

    # Not BST
    tree_2 = TreeNode(5)
    tree_2.left = TreeNode(3)
    tree_2.left.right = TreeNode(1)
    tree_2.left.left = TreeNode(2)
    tree_2.right = TreeNode(6)
    tree_2.right.right = TreeNode(8)

    # single node tree
    tree_3 = TreeNode(0)

    # null tree
    tree_4 = None

    print(validate_bst(tree_1))
    print(validate_bst(tree_2))
    print(validate_bst(tree_3))
    print(validate_bst(tree_4))
