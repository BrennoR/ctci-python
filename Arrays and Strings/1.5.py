# One Away


# O(n)
def one_away(str_1: str, str_2: str) -> bool:
    i, j = 0, 0
    while i < len(str_1) and j < len(str_2):
        if str_1[i] != str_2[j]:
            if len(str_1[i + 1:]) == len(str_2[j + 1:]):
                return str_1[i + 1:] == str_2[j + 1:]
            else:
                return str_1[i + 1:] == str_2[j:] or str_1[i:] == str_2[j + 1:]
        i += 1
        j += 1

    return i == len(str_1) - 1 or j == len(str_2) - 1


strings = [["pale", "ple"], ["pale", "bale"], ["pales", "pale"], ["pale", "bake"]]

for string in strings:
    print(one_away(string[0], string[1]))
