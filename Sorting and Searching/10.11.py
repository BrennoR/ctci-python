# Peaks and Valleys
# TODO: Implement better approach


# Naive approach, Time - O(N log N), Space - O(N), [IF PLATEAUS ARE ALLOWED]
def pk_vl_convert(arr: [int]) -> [int]:
    if arr is None:
        return arr

    arr.sort()
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    i, j, k = 0, len(right) - 1, 0
    while i < len(left) and j >= 0:
        arr[k] = right[j]
        k += 1
        j -= 1
        arr[k] = left[i]
        k += 1
        i += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j >= 0:
        arr[k] = right[j]
        j -= 1
        k += 1

    return arr


# Naive approach 2 [not good with duplicates], Time - O(N log N), Space - O(1)
def pk_vl_convert_2(arr: [int]) -> [int]:
    if arr is None:
        return arr

    arr.sort()
    for i in range(0, len(arr) - 1, 2):
        tmp = arr[i]
        arr[i] = arr[i + 1]
        arr[i + 1] = tmp

    return arr


if __name__ == '__main__':
    arr_1 = [5, 3, 1, 2, 3]
    arr_2 = [1]
    arr_3 = []
    arr_4 = None
    arr_5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    arr_6 = [5, 3, 1, 2, 3, 3]
    print(pk_vl_convert(arr_1))
    print(pk_vl_convert(arr_2))
    print(pk_vl_convert(arr_3))
    print(pk_vl_convert(arr_4))
    print(pk_vl_convert(arr_5))
    print(pk_vl_convert(arr_6))
    print('-' * 80)
    print(pk_vl_convert_2(arr_1))
    print(pk_vl_convert_2(arr_2))
    print(pk_vl_convert_2(arr_3))
    print(pk_vl_convert_2(arr_4))
    print(pk_vl_convert_2(arr_5))
    print(pk_vl_convert_2(arr_6))

