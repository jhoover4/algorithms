import unittest


def urlify(string: str) -> str:
    """
    Problem: Replace all spaces between characters with '%20'.

    Answer:

    Time complexity:
    """

    new_string = ""
    was_space = False

    for char in string:
        if char.isspace() and not was_space:
            was_space = True
            new_string += "%20"
        else:
            was_space = False
            new_string += char

    return new_string.rstrip('%20 ')


class Test(unittest.TestCase):
    def test_urlify(self):
        original_str = 'Mr John Smith  '

        self.assertEquals(urlify(original_str), 'Mr%20John%20Smith')
