import unittest
from collections import deque

from .LinkedList import SinglyLinkedList


def loop_detection(lis):
    """
    Problem: Given a circular linked list, find the node at the beginning of the loop.

    Answer: Use two pointers, one slow and one fast. The fast pointer and slow pointer will eventually meet k nodes
    from the list start, with k being the number of nodes before the loop began.

    This means we can now point a new pointer at the head and keep one at our meeting point. Move them both together and
    they will converge on the loop start point.

    Time complexity: O(n)

    :param LinkedList lis:

    :return bool:
    """

    slow = lis.head
    fast = lis.head.next

    if not slow:
        raise ValueError("List is empty.")

    if not fast:
        return None

    # Find meeting point, which is k away from loop start
    while fast and fast != slow:
        fast = fast.next.next
        slow = slow.next

    # Not a loop
    if not fast.next or not fast.next.next:
        return None

    slow = lis.head
    fast = fast.next

    while fast != slow:
        fast = fast.next
        slow = slow.next

    return fast


class Test(unittest.TestCase):
    def test_is_loop(self):
        pass

    def test_is_not_loop(self):
        pass
