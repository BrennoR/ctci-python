# Magic Index


def magic_index(arr):
    if not arr:
        return False

    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == mid:
            return mid
        elif arr[mid] > mid:
            end = mid - 1
        else:
            start = mid + 1

    return False


# FOLLOW-UP, non-distinct integers
def magic_index_2(arr):
    if not arr:
        return False

    start = 0
    end = len(arr) - 1
    while start < end:
        mid = (start + end) // 2
        if arr[mid] == mid:
            return mid
        else:
            left = mid - 1
            while left > start and arr[left] == arr[mid]:
                left -= 1
            if arr[left] == left:
                return left

            right = mid + 1
            while right < end and arr[right] == arr[mid]:
                right += 1
            if arr[right] == right:
                return right

            if arr[left] > left:
                start = right
            else:
                end = left

    return False


if __name__ == '__main__':
    # m_index = 5
    arr_1 = [-1, 0, 1, 2, 3, 5]

    # no m_index
    arr_2 = [-8, -7, -6, -5, -4, -3, -2]

    # m_index = 4
    arr_3 = [-3, -2, -1, 0, 4, 9, 10, 15]

    # empty array
    arr_4 = []

    # null
    arr_5 = None

    print(magic_index(arr_1))
    print(magic_index(arr_2))
    print(magic_index(arr_3))
    print(magic_index(arr_4))
    print(magic_index(arr_5))

    # Non-distinct values
    # m_index = 5
    arr_6 = [1, 2, 4, 4, 5, 5]
    print(magic_index_2(arr_6))

    arr_7 = [2, 2, 3, 2, 2, 5]
    print(magic_index_2(arr_7))

    arr_8 = [1, 8, 8, 8, 8, 8, 9, 9, 9, 10, 10, 11]
    print(magic_index_2(arr_8))
