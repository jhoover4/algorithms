import unittest
from collections import deque

from .LinkedList import SinglyLinkedList


# Problem 2.7
def intersection(lis):
    """
    Problem: Find where two nodes intersect in a malformed linked list.

    Answer:

    Time complexity:

    :param LinkedList lis:

    :return bool:
    """

    # TODO


class Test(unittest.TestCase):
    def test_is_intersection(self):
        test = SinglyLinkedList()
        test2 = SinglyLinkedList()

        test.add(1)
        test.add(2)
        test.add(3)
        intersection_node = test.add(7)
        test.add(8)

        test2.add(4)
        test2.add(5)
        test2_tail = test2.add(6)

        test2_tail.next = intersection_node

        self.assertTrue(intersection(test))

    def test_is_not_loop(self):
        pass
