# Stack of Boxes
# TODO: Optimize repeated work


class Solution:

    def __init__(self, stack):
        self.max_height = 0
        self.stack = stack
        self.stack.sort(key=lambda x: x[1], reverse=True)

    def stack_of_boxes(self):
        for idx in range(len(self.stack)):
            self.recurse_boxes([self.stack[idx][0] + 1, self.stack[idx][1] + 1, self.stack[idx][2] + 1], idx,
                               len(self.stack), 0)
        return self.max_height

    def recurse_boxes(self, current_dim, start, end, height):
        w, h, d = current_dim
        for idx in range(start, end):
            if self.stack[idx][0] < w and self.stack[idx][1] < h and self.stack[idx][2] < d:
                new_dim = self.stack[idx]
                new_height = height + new_dim[1]
                if new_height > self.max_height:
                    self.max_height = new_height
                self.recurse_boxes(new_dim, idx + 1, end, new_height)


if __name__ == '__main__':
    stack = [[10, 9, 8], [9, 8, 7], [8, 7, 6], [7, 7, 6], [7, 6, 5], [6, 6, 6], [5, 5, 5], [5, 4, 4], [4, 4, 4],
             [4, 3, 3], [3, 3, 3], [3, 2, 2], [1, 1, 1]]
    boxes = Solution(stack)
    max_height = boxes.stack_of_boxes()
    print(max_height)

    stack_2 = [[100, 100, 100]]
    new = Solution(stack_2)
    print(new.stack_of_boxes())
    stack_2.append([25, 25, 25])
    new = Solution(stack_2)
    print(new.stack_of_boxes())
    stack_2.append([5, 20, 30])
    stack_2.append([4, 17, 28])
    new = Solution(stack_2)
    print(new.stack_of_boxes())
