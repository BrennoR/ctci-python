# Sorted Matrix Search
# TODO: Implement better approach


# Naive approach, Time - O(M log N), Space - O(1)
def sorted_matrix_search(M, x):
    if M is None or x is None:
        return None

    rows = len(M)
    cols = len(M[0])

    for r in range(rows):
        if M[r][0] <= x <= M[r][-1]:
            left = 0
            right = cols - 1
            while left <= right:
                mid = (left + right) // 2
                if M[r][mid] == x:
                    return [r, mid]
                elif M[r][mid] > x:
                    right = mid - 1
                else:
                    left = mid + 1

    return "Element not in matrix"


if __name__ == '__main__':
    matrix_1 = [[1, 2, 5, 7, 9],
                [2, 4, 7, 9, 10],
                [4, 8, 9, 14, 19],
                [8, 11, 12, 15, 20],
                [15, 18, 22, 30, 31]]

    print(sorted_matrix_search(matrix_1, 15))
    print(sorted_matrix_search(matrix_1, 20))
    print(sorted_matrix_search(matrix_1, 22))
    print(sorted_matrix_search(None, 1))
