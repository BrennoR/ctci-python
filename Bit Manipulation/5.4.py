# Next Number


def next_number_brute(num: int) -> (int, int):

    # special cases
    if num == 1:
        return None, 2
    elif num == 0:
        return None, 1

    bin_str = str(bin(num))
    count_1 = 0
    for ch in bin_str[2:]:
        if ch == "1":
            count_1 += 1

    large_iter = num + 1
    while True:
        bin_large = str(bin(large_iter))
        c_large = 0
        for ch in bin_large[2:]:
            if ch == "1":
                c_large += 1

        if c_large == count_1:
            break
        else:
            c_large = 0
            large_iter += 1

    small_iter = num - 1
    while True:
        bin_small = str(bin(small_iter))
        c_small = 0
        for ch in bin_small[2:]:
            if ch == "1":
                c_small += 1

        if c_small == count_1:
            break
        else:
            c_small = 0
            small_iter += 1

    return small_iter, large_iter


if __name__ == '__main__':
    print(bin(10), bin(next_number_brute(10)[0]), bin(next_number_brute(10)[1]))
    print(bin(1230), bin(next_number_brute(1230)[0]), bin(next_number_brute(1230)[1]))
    print(bin(1), bin(next_number_brute(1)[1]))
    print(bin(0), bin(next_number_brute(0)[1]))
    print(bin(234238), bin(next_number_brute(234238)[0]), bin(next_number_brute(234238)[1]))

