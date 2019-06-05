# Tree Traversals


def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end='\t')
        inorder(root.right)


def preorder(root):
    if root:
        print(root.value, end='\t')
        inorder(root.left)
        inorder(root.right)


def postorder(root):
    if root:
        inorder(root.left)
        inorder(root.right)
        print(root.value, end='\t')

