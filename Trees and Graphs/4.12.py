# Paths with Sum
# TODO: Implement more efficient solution using hashtable sums


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Brute Force Solution
# Time - O(N log N) to O(N ^ 2), Space - O(N)
class PathsWithSum:

    def __init__(self, target_sum, root):
        self.pathsSum = 0
        self.target_sum = target_sum
        self.root = root
        self.seen = set()
        self.count = 0

    def findPaths(self):
        self.findPathsHelper(self.root, 0)
        return self.pathsSum

    def findPathsHelper(self, root, sum):
        if root:
            sum += root.value
            if sum == self.target_sum:
                self.pathsSum += 1
            self.findPathsHelper(root.left, sum)
            self.findPathsHelper(root.right, sum)
            if root.left and root.left not in self.seen:
                self.seen.add(root.left)
                self.findPathsHelper(root.left, 0)
            if root.right and root.right not in self.seen:
                self.seen.add(root.right)
                self.findPathsHelper(root.right, 0)


if __name__ == '__main__':
    tree_1 = TreeNode(1)
    tree_1.left = TreeNode(6)
    tree_1.left.left = TreeNode(1)
    tree_1.left.right = TreeNode(2)
    tree_1.left.left.left = TreeNode(5)
    tree_1.left.left.right = TreeNode(4)
    tree_1.left.left.left.right = TreeNode(2)
    tree_1.right = TreeNode(7)
    tree_1.right.left = TreeNode(-1)
    tree_1.right.right = TreeNode(4)
    tree_1.right.left.left = TreeNode(1)
    tree_1.right.right.left = TreeNode(3)
    tree_1.right.right.right = TreeNode(5)
    tree_1.right.right.right.left = TreeNode(2)

    solution = PathsWithSum(target_sum=7, root=tree_1)
    print(solution.findPaths())
    print(solution.count)
