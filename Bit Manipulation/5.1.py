# Insertion


def insertion(N, M, i, j):
    mask = ((1 << i) - 1) | (-1 << (j + 1))
    return bin((N & mask) | (M << i))


if __name__ == '__main__':
    print(insertion(0b10000000000, 0b10011, 2, 6))
    print(insertion(0b10101011111, 0b10000001, 1, 8))
