# String Compression
import math


# O(n)
def string_compression(string: str) -> str:

    if not string:
        return string

    max_length = len(string)
    i = 0
    arr = []
    length = 0
    while i < len(string):
        j = i + 1
        count = 1
        while j < len(string) and string[j] == string[i]:
            j += 1
            count += 1
        arr.extend([string[i], str(count)])
        i = j
        length += math.floor(math.log(count, 10)) + 2

    if length <= max_length:
        return "".join(arr)
    else:
        return string


str_1 = "aabccccddc"
str_2 = "b"
str_3 = " "
str_4 = "ABCCDDDDD"
print(string_compression(str_1))
print(string_compression(str_2))
print(string_compression(str_3))
print(string_compression(str_4))
