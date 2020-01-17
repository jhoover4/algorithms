from collections import Counter
import unittest


def is_permutation(string_1: str, string_2: str) -> bool:
    """
    Problem: Determine if a string is a permutation of another string.

    Answer: Store string as bags, which takes linear time to create. Loop through second string and check bag for
    char amounts and decrement if char is found. If char value not found return false.

    Time complexity: O(n)

    :return Bool:
    """

    if len(string_1) != len(string_2):
        return False

    counter = Counter(string_1)

    for char in string_2:
        if counter[char] == 0:
            return False
        else:
            counter[char] -= 1

    return True


class Test(unittest.TestCase):
    def test_is_permutation_true(self):
        self.assertTrue(is_permutation('racecars', 'scarrace'))

    def test_is_permutation_false_len(self):
        self.assertFalse(is_permutation('racecars', 'raacecars'))
