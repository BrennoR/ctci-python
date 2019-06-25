# Random Node
import numpy as np
# TODO: Implement probabilistic traversal method


# BST regular functions taken from data-structures-and-algorithms-python repository
# Time - O(N), Space - O(N)
class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0
        self.node_list = []

    def length(self):
        return self.size

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
            self.node_list.append(self.root)
        self.size += 1

    def _put(self, key, val, current_node):
        if key < current_node.key:
            if current_node.has_left_child():
                self._put(key, val, current_node.left_child)
            else:
                node = TreeNode(key, val, parent=current_node)
                current_node.left_child = node
                self.node_list.append(node)
        elif key > current_node.key:
            if current_node.has_right_child():
                self._put(key, val, current_node.right_child)
            else:
                node = TreeNode(key, val, parent=current_node)
                current_node.right_child = node
                self.node_list.append(node)
        else:
            current_node.payload = val

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, current_node):
        if not current_node:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.left_child)
        else:
            return self._get(key, current_node.right_child)

    def delete(self, key):
        if self.size > 1:
            node_to_remove = self._get(key, self.root)
            if node_to_remove:
                self.remove(node_to_remove)
                self.node_list.remove(node_to_remove)
                self.size -= 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.node_list.clear()
            self.size -= 1
        else:
            raise KeyError('Error, key not in tree')

    @staticmethod
    def remove(current_node):
        if current_node.is_leaf():  # leaf node
            if current_node == current_node.parent.leftChild:
                current_node.parent.left_child = None
            else:
                current_node.parent.right_child = None
        elif current_node.has_both_children():  # interior node
            succ = current_node.findSuccessor()
            succ.splice_out()
            current_node.key = succ.key
            current_node.payload = succ.payload

        else:  # this node has one child
            if current_node.has_left_child():
                if current_node.is_left_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.left_child
                elif current_node.is_right_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.left_child
                else:
                    current_node.replace_node_data(current_node.left_child.key,
                                                   current_node.left_child.payload,
                                                   current_node.left_child.left_child,
                                                   current_node.left_child.right_child)
            else:
                if current_node.is_left_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.right_child
                elif current_node.is_right_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.right_child
                else:
                    current_node.replace_node_data(current_node.right_child.key,
                                                current_node.right_child.payload,
                                                current_node.right_child.left_child,
                                                current_node.right_child.right_child)

    def getRandomNode(self):
        rnd_idx = np.random.randint(0, self.size)
        return self.node_list[rnd_idx]

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def __setitem__(self, key, value):
        self.put(key, value)

    def __delete__(self, key):
        self.delete(key)

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()


class TreeNode:

    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.left_child = left
        self.right_child = right
        self.parent = parent

    def has_left_child(self):
        return self.left_child

    def has_right_child(self):
        return self.right_child

    def is_left_child(self):
        return self.parent and self.parent.left_child == self

    def is_right_child(self):
        return self.parent and self.parent.right_child == self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.left_child or self.right_child)

    def has_any_children(self):
        return self.left_child or self.right_child

    def has_both_children(self):
        return self.left_child and self.right_child

    def replace_node_data(self, key, val, lc, rc):
        self.key = key
        self.payload = val
        self.left_child = lc
        self.right_child = rc
        if self.has_left_child():
            self.left_child.parent = self
        if self.has_right_child():
            self.right_child.parent = self

    def splice_out(self):
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        elif self.has_any_children():
            if self.has_left_child():
                if self.is_left_child():
                    self.parent.left_child = self.left_child
                else:
                    self.parent.right_child = self.left_child
                self.left_child.parent = self.parent
            else:
                if self.is_left_child():
                    self.parent.left_child = self.right_child
                else:
                    self.parent.right_child = self.right_child
                self.right_child.parent = self.parent

    def find_successor(self):
        succ = None
        if self.has_right_child():
            succ = self.right_child.find_min()
        else:
            if self.parent:
                if self.is_left_child():
                    succ = self.parent
                else:
                    self.parent.right_child = None
                    succ = self.parent.find_successor()
                    self.parent.right_child = self

        return succ

    def find_min(self):
        current = self
        while current.has_left_child():
            current = current.left_child

        return current


if __name__ == '__main__':
    tree_1 = BinarySearchTree()
    tree_1.put(1, 1)
    tree_1.put(2, 2)
    tree_1.put(3, 3)
    tree_1.put(4, 4)
    tree_1.put(5, 5)
    tree_1.put(6, 6)

    print(tree_1.getRandomNode().key)
