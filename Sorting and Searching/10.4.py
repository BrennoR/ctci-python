# Sorted Search, No Size


# Time - O(log N), Space - O(1)
def find_element(x, arr):
    i, left = 0, 0

    if x is None:
        raise Exception("Enter a valid value for x")

    if arr is None or arr[i] == -1:
        raise Exception("Empty array")

    while arr[i] < x and arr[i] != -1:
        left = i
        i = (i + 1) * 2 - 1

    right = i
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x or arr[mid] == -1:
            right = mid - 1
        else:
            left = mid + 1

    return "Element not found"


if __name__ == '__main__':
    listy_1 = [1, 2, 3, 5, 6, 8, 9, 10, 14, 15, 17, 18, 19, 21,
               -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    listy_2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, -1, -1, -1, -1, -1, -1,
               -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    listy_3 = None
    listy_4 = [-1]
    listy_5 = [4, -1, -1, -1]

    print(find_element(15, listy_1))        # 9
    print(find_element(3, listy_2))         # 10
    print(find_element(9, listy_2))         # Element not found
    # print(find_element(1, listy_3))         # Empty/None array
    # print(find_element(None, listy_3))      # No x
    # print(find_element(5, listy_4))         # Empty/None array
    print(find_element(4, listy_5))         # 0
    print(find_element(1, listy_5))         # Element not found
