import unittest


def is_substring(string: str, substring: str) -> bool:
    """
    Wrapper over Python's default functionality for sake of expressiveness in problem.
    """

    return substring in string


def string_rotation(string_1: str, string_2: str) -> bool:
    """
    Problem: Check if a string is a rotation of another string with only one call to is_substring.

    Answer: If you repeat the original word twice, the substring will always be present as the rotation will be complete.

    Time complexity: O(n)
    """

    if len(string_1) != len(string_2):
        return False

    return is_substring(string_1 + string_1, string_2)


class Test(unittest.TestCase):
    def test_is_rotation_unique_letters(self):
        self.assertTrue(string_rotation('waterbottle', 'erbottlewat'))

    def test_is_rotation_dup_letters(self):
        self.assertTrue(string_rotation('title', 'itlet'))
        self.assertTrue(string_rotation('mississippi', 'issippimiss'))

    def test_is_not_rotation(self):
        self.assertFalse(string_rotation('waterbottle', 'erbottlewar'))

    def test_is_not_equal_len(self):
        self.assertFalse(string_rotation('waterbotle', 'erbottlewat'))
