import unittest
from collections import Counter


# O(N log(N))
def check_permutation_sort(str1, str2):

    if len(str1) != len(str2):
        return False

    str1 = sorted(str1)
    str2 = sorted(str2)

    if str1 == str2:
        return True
    else:
        return False


# O(N)
def check_permutation_list(str1, str2):

    if len(str1) != len(str2):
        return False

    # assuming ASCII
    str1_chars = [0 for _ in range(128)]
    str2_chars = [0 for _ in range(128)]

    for char in str1:
        val = ord(char)
        str1_chars[val] += 1

    for char in str2:
        val = ord(char)
        str2_chars[val] += 1

    for i in range(128):
        if str1_chars[i] != str2_chars[i]:
            return False

    return True


# counter method from CtCl-6th-Edition-Python repository by careercup
# O(N)
def check_permutation_counter(str1, str2):
    if len(str1) != len(str2):
        return False
    counter = Counter()
    for c in str1:
        counter[c] += 1
    for c in str2:
        if counter[c] == 0:
            return False
        counter[c] -= 1
    return True


class TestPermutation(unittest.TestCase):
    false_strs = ['abcijklop', 'lacpobkid ']
    true_strs = ['kerlfuit', 'tilrekuf']

    def test_strs(self):
        # false strs check
        self.assertFalse(check_permutation_sort(self.false_strs[0], self.false_strs[1]))
        self.assertFalse(check_permutation_list(self.false_strs[0], self.false_strs[1]))

        # true strs check
        self.assertTrue(check_permutation_sort(self.true_strs[0], self.true_strs[1]))
        self.assertTrue(check_permutation_list(self.true_strs[0], self.true_strs[1]))


if __name__ == "__main__":
    unittest.main()
