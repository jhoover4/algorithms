import unittest

from .LinkedList import SinglyLinkedList


def kth_to_last(lis, index_from_end):
    """
    Problem: Return kth to last (as in k from the end, or the reverse index, such as list[-1] returning the last element).
    Do this in only ONE full loop (IE we can't just check the size first).

    Answer: Use 2 pointers A and B. Pointer A will be set to k into the list. Then move both at the same time, which means
    A will reach the end of the list when B hits the needed node.

    Time complexity: O(n)

    :param LinkedList lis:
    :param int index_from_end:

    :return:
    """

    if index_from_end <= 0:
        return lis.head

    pointer1 = lis.head
    pointer2 = lis.head

    i = 0
    while i < index_from_end:
        if pointer1.next:
            pointer1 = pointer1.next
        else:
            raise ValueError("Index out of bounds.")
        i += 1

    while pointer1:
        pointer1 = pointer1.next
        pointer2 = pointer2.next

    return pointer2


class Test(unittest.TestCase):
    def test_is_getting_reverse_index(self):
        linked_lis = SinglyLinkedList()
        linked_lis.add(1)
        linked_lis.add(2)
        linked_lis.add(3)
        linked_lis.add(4)

        self.assertEqual(kth_to_last(linked_lis, 1).data, 4)
        self.assertEqual(kth_to_last(linked_lis, 3).data, 2)
