# Conversion


def xor_conversion(A: int, B: int) -> int:
    ones = str(bin(A ^ B))
    return ones.count("1")


def brute_conversion(A: int, B: int) -> int:
    A_bin = str(bin(A))[2:]
    B_bin = str(bin(B))[2:]
    A_idx = len(A_bin) - 1
    B_idx = len(B_bin) - 1

    count = 0
    while A_idx >= 0 and B_idx >= 0:
        if A_bin[A_idx] != B_bin[B_idx]:
            count += 1
        A_idx -= 1
        B_idx -= 1

    while A_idx >= 0:
        if A_bin[A_idx] == "1":
            count += 1
        A_idx -= 1

    while B_idx >= 0:
        if B_bin[B_idx] == "1":
            count += 1
        B_idx -= 1

    return count


if __name__ == '__main__':
    print(brute_conversion(29, 15))
    print(brute_conversion(0, 0))
    print(brute_conversion(0, 1))
    print(brute_conversion(123, 35223))

    print(xor_conversion(29, 15))
    print(xor_conversion(0, 0))
    print(xor_conversion(0, 1))
    print(xor_conversion(123, 35223))
