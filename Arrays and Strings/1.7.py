# Rotate Matrix
import numpy as np


# Time - O(N * N), Space - O(4N)
def rotate_matrix(matrix):
    i = 0
    j = len(matrix) - 1
    while i < j:
        one = np.copy(matrix[i, i:j+1])
        two = np.copy(matrix[i+1:j+1, j])
        three = np.copy(matrix[j, i:j])
        four = np.copy(matrix[i+1:j, i])
        matrix[i:j+1, j] = one
        matrix[j, i:j] = two[::-1]
        matrix[i:j, i] = three
        matrix[i, i+1:j] = four[::-1]
        i += 1
        j -= 1

    return matrix


# Time - O(N * N), Space - O(1)
def rotate_matrix_2(matrix):
    if len(matrix) == 0 or len(matrix) != len(matrix[0]):
        return False

    layer = 0
    while layer < len(matrix) // 2:
        first = layer
        last = len(matrix) - 1 - layer
        for i in range(first, last):
            offset = i - first
            top = matrix[first, i]

            # left -> top
            matrix[first, i] = matrix[last - offset, first]

            # bottom -> left
            matrix[last - offset, first] = matrix[last, last - offset]

            # right -> bottom
            matrix[last, last - offset] = matrix[i, last]

            # top -> right
            matrix[i, last] = top

        layer += 1

    return matrix


mat_1 = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

mat_2 = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]])

# print(rotate_matrix(mat_1))
print(rotate_matrix_2(mat_1))
# print(rotate_matrix(mat_2))
print(rotate_matrix_2(mat_2))
