# Search in Rotated Array
# TODO: Account for duplicates, fix algorithm


# Time - O(log N)
def rotated_search(arr: [int], val: int):
    if arr is None or val is None:
        return -1

    start = 0
    end = len(arr) - 1
    while start < end:
        mid = (start + end) // 2
        if arr[mid] == val:
            return mid
        else:
            if arr[start] == val:
                return start
            elif arr[end] == val:
                return end
            if arr[mid] > val:
                if arr[start] > val:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                if arr[end] < val:
                    end = mid - 1
                else:
                    start = mid + 1

    return -1


if __name__ == '__main__':
    arr_1 = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
    print(rotated_search(arr_1, 5))
    print(rotated_search(arr_1, 0))
    print(rotated_search(None, 0))
    print(rotated_search(arr_1, None))
    arr_2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1]
    print(rotated_search(arr_2, 2))