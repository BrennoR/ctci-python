# Binary to String


def bin_to_string(num: float, tolerance: float = 0.0001) -> str:
    if num == 0:
        return "0"
    elif num == 1:
        return "1"

    num_ret = num
    bin_str = "."

    while num != 0 and len(bin_str) < 33:
        num *= 2
        if num >= 1:
            bin_str += "1"
            num -= 1
        else:
            bin_str += "0"

    # check if num has been accurately represented w/ 32 bits using a tolerance val
    check_num = 0
    pow = -1
    for ch in bin_str[1:]:
        check_num += int(ch) * (2 ** pow)
        pow -= 1

    if abs(num_ret - check_num) > tolerance:
        return "Error"

    return bin_str


def bin_to_string_int(num: int) -> str:
    bin_str = ""

    if num < 0:
        raise ValueError("Number must be positive")
    elif num == 0:
        return "0"
    elif num > 2 ** 32 - 1:
        raise ValueError("Number cannot be represented in binary with 32 bits")

    pow = 31
    while 2 ** pow > 0:
        if num - 2 ** pow >= 0:
            bin_str += "1"
            num -= 2 ** pow
            pow -= 1
            break
        pow -= 1

    for p in range(pow, -1, -1):
        if num - 2 ** p >= 0:
            bin_str += "1"
            num -= 2 ** p
        else:
            bin_str += "0"

    return bin_str


if __name__ == '__main__':
    assert bin_to_string_int(128) == str(bin(128))[2:]
    assert bin_to_string_int(12383) == str(bin(12383))[2:]
    assert bin_to_string_int(0) == str(bin(0))[2:]
    assert bin_to_string_int(1) == str(bin(1))[2:]
    assert bin_to_string_int(984736189) == str(bin(984736189))[2:]

    assert bin_to_string(0.893)[:9] == '.11100100'
    assert bin_to_string(0.260)[:9] == '.01000010'
    assert bin_to_string(0.223)[:9] == '.00111001'
    assert bin_to_string(0.176)[:9] == '.00101101'
