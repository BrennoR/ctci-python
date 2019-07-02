# BST Sequences
# TODO: Rework Solution


class Node:

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# Solution taken from w-hat ctci-solutions repository
def bst_sequences(bst):
    return bst_sequences_partial([], [bst])


def bst_sequences_partial(partial, subtrees):
    if not len(subtrees):
        return [partial]
    sequences = []
    for index, subtree in enumerate(subtrees):
        next_partial = partial + [subtree.data]
        next_subtrees = subtrees[:index] + subtrees[index + 1:]
        if subtree.left:
            next_subtrees.append(subtree.left)
        if subtree.right:
            next_subtrees.append(subtree.right)
        sequences += bst_sequences_partial(next_partial, next_subtrees)
    return sequences


if __name__ == '__main__':
    print(bst_sequences(Node(7, Node(4, Node(5)), Node(9))))
    print(bst_sequences(Node(7, Node(4, Node(5), Node(6)), Node(9))))
