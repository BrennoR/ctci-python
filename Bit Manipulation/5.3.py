# Flip Bit to Win


def flip_bit_to_win(num: int) -> int:
    bin_str = str(bin(num))[2:]

    idx = 0
    left_side = 0
    count = 0
    max_count = 0
    zero_flag = False

    while idx < len(bin_str):
        if bin_str[idx] == "1":
            count += 1
            idx += 1
        elif zero_flag:
            if count > max_count:
                max_count = count
            count -= left_side
            zero_flag = False
        else:
            count += 1
            left_side = count
            idx += 1
            zero_flag = True

    return max(count, max_count)


if __name__ == '__main__':
    assert flip_bit_to_win(1775) == 8
    assert flip_bit_to_win(1212) == 6
    assert flip_bit_to_win(0) == 1
    assert flip_bit_to_win(1) == 1
    assert flip_bit_to_win(1229348) == 4
