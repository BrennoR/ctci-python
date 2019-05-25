# Zero Matrix
import numpy as np


# Time - O(N * N), Space - O(2N)
def zero_matrix(matrix):
    rows = set()
    cols = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)

    for r in rows:
        matrix[r, :] = np.zeros(shape=(1, len(matrix[0])))

    for c in cols:
        matrix[:, c] = np.zeros(shape=(len(matrix), ))

    return matrix


# Time - O(N * N), Space - O(1)
def zero_matrix_2(matrix):
    matrix = np.array(matrix, dtype=np.dtype(object))
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[i, :] = '#'
                matrix[:, j] = '#'

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '#':
                matrix[i][j] = 0

    return matrix


# Time - O(N * N), Space - O(1)
def zero_matrix_3(matrix):
    matrix = np.array(matrix, dtype=np.dtype(object))

    row_has_zero = False
    col_has_zero = False

    # check if first row has a zero
    for j in range(len(matrix[0])):
        if matrix[0, j] == 0:
            row_has_zero = True

    # check if first column has a zero
    for i in range(len(matrix)):
        if matrix[i, 0] == 0:
            col_has_zero = True

    # iterate through the array and mark rows and cols that have zeros
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i, j] == 0:
                matrix[i, 0] = 0
                matrix[0, j] = 0

    # nullify rows based on first column values
    for i in range(1, len(matrix)):
        if matrix[i, 0] == 0:
            matrix[i, :] = 0

    # nullify columns based on first row values
    for j in range(1, len(matrix[0])):
        if matrix[0, j] == 0:
            matrix[:, j] = 0

    # nullify first row
    if row_has_zero:
        matrix[0, :] = 0

    # nullify first column
    if col_has_zero:
        matrix[:, 0] = 0

    return matrix


mat_1 = np.array([[1, 2, 3, 4],
                  [5, 0, 7, 8],
                  [9, 10, 0, 12],
                  [13, 14, 15, 16]])

mat_2 = np.array([[1, 2, 0],
                  [4, 5, 6],
                  [7, 8, 9]])

print(zero_matrix_3(mat_1), end='\n\n')
print(zero_matrix_3(mat_2))
