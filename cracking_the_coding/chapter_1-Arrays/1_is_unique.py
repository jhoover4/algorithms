import unittest


def is_unique(string: str) -> bool:
    """
    Problem: Determine if a string has all unique characters.

    Answer: Use a hash table (a set uses this for lookups) to check if char gets repeated.
    This is trivial to implement in Python.

    Time complexity: O(n)
    """

    existing_chars = set()

    for char in string:
        if char in existing_chars:
            return False
        else:
            existing_chars.add(char)

    return True


def is_unique_no_data_structures(string: str) -> bool:
    """
    Problem: Determine if a string has all unique characters without using any data structures.

    Answer: Sort the string as an array. Loop through array. If neighboring characters are equal, it is not unique.

    Time complexity: O(n log n) - For sorting
    """

    sorted_string = sorted(string)

    for i in range(len(sorted_string)):
        if i != len(sorted_string) - 1:
            if sorted_string[i] == sorted_string[i + 1]:
                return False

    return True


class Test(unittest.TestCase):
    def test_is_unique_true(self):
        self.assertTrue(is_unique('abcde'))

    def test_is_unique_false(self):
        self.assertFalse(is_unique('Aun-uniquestring'))

    def test_is_unique_no_data_structures_true(self):
        self.assertTrue(is_unique_no_data_structures('abcde'))

    def test_is_unique_no_data_structures_false(self):
        self.assertFalse(is_unique_no_data_structures('Aun-uniquestring'))
