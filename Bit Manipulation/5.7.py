# Pairwise Swap


def pairwise_swap(num: int) -> int:
    return ((num & 0xaaaaaaaa) >> 1) ^ ((num & 0x55555555) << 1)


def brute_pairwise_swap(num: int):
    bin_list = list(bin(num))[2:]
    for b in range(len(bin_list) - 1, 0, -2):
        bin_list[b], bin_list[b - 1] = bin_list[b - 1], bin_list[b]

    return int("".join(bin_list), 2)


if __name__ == '__main__':
    print(bin(1432), brute_pairwise_swap(1432))
    print(bin(0), brute_pairwise_swap(0))
    print(bin(8), brute_pairwise_swap(8))

    print(bin(1432), bin(pairwise_swap(1432)))
    print(bin(564), bin(pairwise_swap(564)))
