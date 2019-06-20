# Recursive Multiply


# Time - O(log s), where s is the smaller
def minProductHelper(smaller, bigger):
    if smaller == 0:
        return 0
    elif smaller == 1:
        return bigger
    s = smaller >> 1
    halfProd = minProductHelper(s, bigger)

    if smaller % 2 == 0:
        return halfProd + halfProd
    else:
        return halfProd + halfProd + bigger


def minProduct(a, b):
    smaller = min(a, b)
    bigger = max(a, b)
    return minProductHelper(smaller, bigger)


if __name__ == '__main__':
    print(minProduct(5, 10))
