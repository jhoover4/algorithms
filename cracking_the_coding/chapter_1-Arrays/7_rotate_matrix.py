import unittest
from typing import List


def rotate_matrix(matrix: List[List[int]]) -> List[List[int]]:
    """
    Problem: Rotate an M x N matrix 90 degrees.

    Answer:

    Time complexity: O(MxN)
    """

    if not matrix or not matrix[0]:
        raise ValueError("Must supply valid M x N matrix.")

    col_len = len(matrix)
    row_len = len(matrix[0])
    new_matrix = [[] for _ in range(row_len)]

    for row in range(col_len):
        for i, item in enumerate(matrix[row]):
            new_matrix[i].insert(0, item)

    return new_matrix


def rotate_matrix_in_place(matrix: List[List[int]]) -> List[List[int]]:
    """
    Problem: Rotate an M x N matrix 90 degrees in place (no new data structure)

    Answer:

    Time complexity: O(MxN)
    """

    # TODO: Finish this

    if not matrix or not matrix[0]:
        raise ValueError("Must supply valid M x N matrix.")

    col_len = len(matrix)
    row_len = len(matrix[0])
    new_matrix = [[] for _ in range(row_len)]

    for row in range(col_len):
        for i, item in enumerate(matrix[row]):
            new_matrix[i].insert(0, item)

    return new_matrix


class Test(unittest.TestCase):
    def test_has_rotated_square(self):
        test_matrix = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ]

        rotated_matrix = [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5]
        ]

        self.assertEqual(rotate_matrix(test_matrix), rotated_matrix)

    def test_has_rotated_rectangle(self):
        test_matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16],
            [17, 18, 19, 20]
        ]

        rotated_matrix = [
            [17, 13, 9, 5, 1],
            [18, 14, 10, 6, 2],
            [19, 15, 11, 7, 3],
            [20, 16, 12, 8, 4],
        ]

        self.assertEqual(rotated_matrix, rotate_matrix(test_matrix))
