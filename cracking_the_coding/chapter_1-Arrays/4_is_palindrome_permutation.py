import unittest
from collections import Counter


def is_palindrome_permutation(string_1: str, string_2: str) -> bool:
    """
    Problem: Determine if a string is a permutation and a palindrome of another string.

    Answer: Store string as bags, which takes linear time to create. Loop through second string and check bag for
    char amounts and decrement if char is found. If char value not found return false.

    Time complexity: O(n)

    :return Bool:
    """

    if len(string_1) != len(string_2):
        return False

    counter = Counter(string_1)

    # Check if palindrome
    has_odd = False
    for key, val in counter.items():
        if val % 2 != 0:
            if has_odd:
                return False
            else:
                has_odd = True

    # Check if permutation
    for char in string_2:
        if counter[char] == 0:
            return False
        else:
            if counter[char] == 0:
                return False
            else:
                counter[char] -= 1

    return True


class Test(unittest.TestCase):
    def test_is_permutation_true(self):
        self.assertTrue(is_palindrome_permutation('racecar', 'carrace'))

    def test_is_permutation_false(self):
        self.assertFalse(is_palindrome_permutation('racecars', 'raacecars'))

    def test_is_palindrome_false(self):
        self.assertFalse(is_palindrome_permutation('raciecars', 'scairrace'))
