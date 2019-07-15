# Sparse Search
# TODO: Modify algorithm to find nearest string instead of walking both ways


# Time - O(N), Space - O(1)
def sparse_search(item, arr):
    if arr is None or item is None:
        return "Enter valid array and string"

    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        inner_left = mid - 1
        inner_right = mid + 1
        if arr[mid] == "":
            while inner_left > left and arr[inner_left] == "":
                inner_left -= 1
            while inner_right < right and arr[inner_right] == "":
                inner_right += 1

            if 0 <= inner_left < len(arr) and arr[inner_left] == item:
                return inner_left
            if 0 <= inner_right < len(arr) and arr[inner_right] == item:
                return inner_right

        if arr[mid] == item:
            return mid
        elif (arr[mid] != "" and arr[mid] > item) or (0 <= inner_left < len(arr) and arr[inner_left] > item):
            right = inner_left
        elif (arr[mid] != "" and arr[mid] < item) or (0 <= inner_right < len(arr) and arr[inner_right] < item):
            left = inner_right
        else:
            break

    return "String not found"


if __name__ == '__main__':
    arr_1 = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
    print(sparse_search("dad", arr_1))
