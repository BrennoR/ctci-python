# Minimal Tree
import importlib
traversals = importlib.import_module('tree-traversals')


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Time - O(N), Space - O(N)
def minimal_tree(arr):
    if arr:
        mid = len(arr) // 2
        root = TreeNode(arr[mid])
        left = arr[:mid]
        right = arr[mid + 1:]
        root.left = minimal_tree(left)
        root.right = minimal_tree(right)
        return root


if __name__ == '__main__':
    arr_1 = [1, 2, 3]
    arr_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    arr_3 = [1, 2, 3, 4]
    arr_4 = []
    arr_5 = None
    bst_1 = minimal_tree(arr_1)
    bst_2 = minimal_tree(arr_2)
    bst_3 = minimal_tree(arr_3)
    bst_4 = minimal_tree(arr_4)
    bst_5 = minimal_tree(arr_5)

    print("=" * 20, "Array 1: even num", "=" * 20, end='\n')
    traversals.inorder(bst_1)
    print('\n\n')

    print("=" * 20, "Array 2: even num large", "=" * 20, end='\n')
    traversals.inorder(bst_2)
    print('\n\n')

    print("=" * 20, "Array 3: odd num", "=" * 20, end='\n')
    traversals.inorder(bst_3)
    print('\n\n')

    print("=" * 20, "Array 4: []", "=" * 20, end='\n')
    traversals.inorder(bst_4)
    print('\n\n')

    print("=" * 20, "Array 5: None", "=" * 20, end='\n')
    traversals.inorder(bst_5)
    print('\n\n')
