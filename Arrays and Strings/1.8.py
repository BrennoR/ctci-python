# Zero Matrix


# O(n) - O(n^2)
def zero_matrix(matrix: [int]) -> [int]:
    rows = len(matrix)
    cols = len(matrix[0])

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0:
                matrix[r] = ['#'] * rows
                for i in range(rows):
                    matrix[i][c] = '#'

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == '#':
                matrix[r][c] = 0

    return matrix


matrix_1 = [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 0, 1, 3],
            [2, 4, 5, 2]]


print(zero_matrix(matrix_1))
