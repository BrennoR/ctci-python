# Bit Operations

a = 0b100   # binary
b = 0x1E8   # hexadecimal

print("binary:", a)
print("hexadecimal:", b)

c = bin(198)    # integer to binary using bin function
print(c)

d = int('0b1011', 2)    # binary to integer using int function
print(d)

# Operators

# AND
print(bin(0b100 & 0b100))

# OR
print(bin(0b100 | 0b100))

# XOR
print(bin(0b100 ^ 0b100))

# ones complement
print(bin(~0b100), ~0b100)   # -> 100 -> 011 -> negative.. = -5 (for three bits)

# binary left shift
print(bin(0b100 << 2), 0b100 << 2)

# binary right shift
print(bin(0b100 >> 1), 0b100 >> 1)

# operations
print("=" * 30, "operations", "=" * 30)


# gets bit at i, returns True if 1, False otherwise
def get_bit(num, i):
    mask = 1 << i
    return (num & mask) != 0


print(get_bit(int('0b1100', 2), 0))
print(get_bit(int('0b1100', 2), 1))
print(get_bit(int('0b1100', 2), 2))
print(get_bit(int('0b1100', 2), 3))
print(get_bit(12, 0))
print(get_bit(12, 1))
print(get_bit(12, 2))
print(get_bit(12, 3))


# sets bit at i to 1
def set_bit(num, i):
    mask = 1 << i
    return num | mask


print(bin(set_bit(int('0b01101', 2), 0)), set_bit(int('0b01101', 2), 0))
print(bin(set_bit(int('0b01101', 2), 1)), set_bit(int('0b01101', 2), 1))
print(bin(set_bit(int('0b01101', 2), 2)), set_bit(int('0b01101', 2), 2))
print(bin(set_bit(int('0b01101', 2), 3)), set_bit(int('0b01101', 2), 3))
print(bin(set_bit(int('0b01101', 2), 10)), set_bit(int('0b01101', 2), 10))


# clears bit at i
def clear_bit(num, i):
    mask = ~(1 << i)
    return num & mask


print(bin(clear_bit(int('0b1111', 2), 0)), clear_bit(int('0b1111', 2), 0))
print(bin(clear_bit(int('0b1111', 2), 1)), clear_bit(int('0b1111', 2), 1))
print(bin(clear_bit(int('0b1111', 2), 2)), clear_bit(int('0b1111', 2), 2))
print(bin(clear_bit(int('0b1111', 2), 3)), clear_bit(int('0b1111', 2), 3))


# clear bits from the most significant bit through i (inclusive)
def clear_bits_ms_through_i(num, i):
    mask = (1 << i) - 1
    return num & mask


print(bin(clear_bits_ms_through_i(int('0b1111', 2), 0)), clear_bits_ms_through_i(int('0b1111', 2), 0))
print(bin(clear_bits_ms_through_i(int('0b1111', 2), 1)), clear_bits_ms_through_i(int('0b1111', 2), 1))
print(bin(clear_bits_ms_through_i(int('0b1111', 2), 2)), clear_bits_ms_through_i(int('0b1111', 2), 2))
print(bin(clear_bits_ms_through_i(int('0b1111', 2), 3)), clear_bits_ms_through_i(int('0b1111', 2), 3))


# clear bits from i through 0 (inclusive)
def clear_bits_i_through_0(num, i):
    mask = (-1 << (i + 1))
    return num & mask


print(bin(clear_bits_i_through_0(int('0b1111', 2), 0)), clear_bits_i_through_0(int('0b1111', 2), 0))
print(bin(clear_bits_i_through_0(int('0b1111', 2), 1)), clear_bits_i_through_0(int('0b1111', 2), 1))
print(bin(clear_bits_i_through_0(int('0b1111', 2), 2)), clear_bits_i_through_0(int('0b1111', 2), 2))
print(bin(clear_bits_i_through_0(int('0b1111', 2), 3)), clear_bits_i_through_0(int('0b1111', 2), 3))


# updates the ith bit to a value v
def update_bit(num, i, bitIs1):
    value = int(bitIs1)
    mask = ~(1 << i)
    return (num & mask) | (value << i)


print(bin(update_bit(int('0b1111', 2), 0, False)), update_bit(int('0b1111', 2), 0, False))
print(bin(update_bit(int('0b1111', 2), 1, False)), update_bit(int('0b1111', 2), 1, False))
print(bin(update_bit(int('0b1111', 2), 2, False)), update_bit(int('0b1111', 2), 2, False))
print(bin(update_bit(int('0b1111', 2), 3, False)), update_bit(int('0b1111', 2), 3, False))
