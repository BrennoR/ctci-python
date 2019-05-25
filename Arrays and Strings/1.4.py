# Palindrome Permutation
from collections import Counter


# O(n)
def palindrome_permutation(string: str) -> bool:

    cnt = Counter(string)
    odd = False
    for value in cnt.values():
        mod = value % 2
        if mod != 0:
            if odd:
                return False
            odd = True

    return True


if __name__ == "__main__":
    strings = ["tactcoa", "raecrac", "koala", "lososl"]

    for string in strings:
        print(palindrome_permutation(string))
