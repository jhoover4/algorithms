import unittest
from typing import List


def zero_matrix(matrix: List[List[int]]) -> List[List[int]]:
    """
    Problem: If an element in an M x N matrix is 0, return it with its whole row set to 0.

    Answer: While looping over every row, if we find a zero in the row, break out of the row loop and replace it
    with zeros that match the length of the row.

    Time complexity: O(MxN)
    """

    if not matrix or not matrix[0]:
        raise ValueError("Must supply valid M x N matrix.")

    new_matrix = []
    row_len = len(matrix[0])

    for row in range(len(matrix)):
        new_row = []
        for item in matrix[row]:
            if item == 0:
                new_row = [0 for _ in range(row_len)]
                break
            else:
                new_row.append(item)

        new_matrix.append(new_row)

    return new_matrix


class Test(unittest.TestCase):
    def test_has_zero(self):
        matrix = [
            [1, 2, 3],
            [1, 0, 3],
            [7, 8, 9]
        ]

        result_matrix = [
            [1, 2, 3],
            [0, 0, 0],
            [7, 8, 9]
        ]

        self.assertEqual(zero_matrix(matrix), result_matrix)

    def test_has_no_zero(self):
        matrix = [
            [1, 2, 3],
            [2, 2, 3],
            [7, 8, 9]
        ]

        result_matrix = [
            [1, 2, 3],
            [2, 2, 3],
            [7, 8, 9]
        ]

        self.assertEqual(zero_matrix(matrix), result_matrix)
