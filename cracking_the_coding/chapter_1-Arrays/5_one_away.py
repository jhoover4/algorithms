import collections
import unittest


def one_away(string_1: str, string_2: str) -> bool:
    """
    Problem: Determine if a string is one "edit" (edit, replace, or delete) away from another string.

    Answer: Using a bag for string1, check if any of the numbers in the bag and string2 are off more than once.
    BETTER THAN THE BOOK'S SOLUTION GAYLE!

    Time complexity: O(n)

    :return Bool:
    """

    counter = collections.Counter(string_1)

    for char in string_2:
        if counter[char]:
            counter[char] -= 1

    counter += collections.Counter()

    return len(list(counter.elements())) < 2


class Test(unittest.TestCase):
    def test_is_permutation_insert(self):
        self.assertTrue(one_away('pale', 'ple'))

    def test_is_permutation_delete(self):
        self.assertTrue(one_away('pales', 'pale'))

    def test_is_permutation_replace(self):
        self.assertTrue(one_away('pale', 'bale'))

    def test_is_permutation_false(self):
        self.assertFalse(one_away('pale', 'bake'))
