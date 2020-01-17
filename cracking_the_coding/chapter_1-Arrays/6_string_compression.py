import unittest


def string_compression(string):
    """
    Problem: Implement a method that represents repeating characters with a number.
    Return the new string only if its shorter than the original.

    Answer: Loop over string and use a two variables to keep track of current char and the count.
    Add these to an array when character changes.

    Time complexity: O(n)

    :param string:

    :rtype: str
    """

    new_string = []

    current = string[0]
    count = 0
    for i, char in enumerate(string):
        if char != current:
            new_string.append(current + str(count))
            current = char
            count = 1
        else:
            count += 1
            if i == len(string) - 1:
                new_string.append(current + str(count))

    result = ''.join(new_string)

    if len(result) > len(string):
        return string

    return result


class Test(unittest.TestCase):
    def test_is_shorter(self):
        self.assertEquals(string_compression('pale'), 'pale')

    def test_has_repeats(self):
        self.assertEquals(string_compression('aabcccccaaa'), 'a2b1c5a3')
