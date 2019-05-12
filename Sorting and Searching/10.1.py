# Sorted Merge


# O(|A|+|B|)
def sorted_merge(A: [int], B: [int]) -> [int]:
    if A == [] or B == []:
        return A

    i = len(A) - len(B) - 1
    j = len(B) - 1
    k = len(A) - 1
    while j >= 0:
        if i >= 0 and A[i] >= B[j]:
            A[k] = A[i]
            i -= 1
        else:
            A[k] = B[j]
            j -= 1
        k -= 1

    return A


A = [1, 2, 4, 7, 9, 0, 0, 0, 0, 0]
B = [3, 5, 6, 8, 10]
print(sorted_merge(A, B))
