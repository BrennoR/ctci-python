# First Common Ancestor


class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Time - O(N), could also add another function to check bool for cases w/ no ancestor
def first_common_ancestor(root, node1, node2):
    if root:
        if root == node1 or root == node2:
            return True

        left = first_common_ancestor(root.left, node1, node2)
        right = first_common_ancestor(root.right, node1, node2)

        if type(left) == TreeNode:
            return left

        if type(right) == TreeNode:
            return right

        if left and right:
            return root

        return left or right


if __name__ == '__main__':

    tree_1 = TreeNode(1)
    tree_1.left = TreeNode(2)
    tree_1.right = TreeNode(3)
    tree_1.right.left = TreeNode(4)
    tree_1.right.right = TreeNode(5)
    tree_1.right.left.right = TreeNode(6)
    tree_1.right.right.left = TreeNode(7)
    tree_1.right.right.right = TreeNode(8)

    print(first_common_ancestor(tree_1, tree_1.right.right.left, tree_1.right.right.right).val)
