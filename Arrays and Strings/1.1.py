import unittest


def is_unique(string):
    chars = {}

    for char in string:
        if char in chars:
            return False
        else:
            chars[char] = True

    return True


# ascii solution code taken from CtCl-6th-Edition-Python repository by careercup
def ascii_solution(string):
    if len(string) > 128:
        return False

    char_set = [False for _ in range(128)]
    for char in string:
        val = ord(char)
        if char_set[val]:
            # Char already found in string
            return False
        char_set[val] = True

    return True


class TestUnique(unittest.TestCase):
    false_values = ['hello', '123  ', 'him4390f ~!3']
    true_values = ['abcjd9?', '12 8hib', 'padiogu01_']

    def test_values(self):
        # false values check
        for string in self.false_values:
            self.assertFalse(is_unique(string))

        # true values check
        for string in self.true_values:
            self.assertTrue(is_unique(string))


if __name__ == "__main__":
    unittest.main()
