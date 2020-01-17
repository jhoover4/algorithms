import unittest

from .LinkedList import SinglyLinkedList


# Problem 2.1
def remove_duplicates(dup_lis):
    """
    Problem: Remove duplicates from an unsorted linked list. No buffer allowed.

    Answer: Create a new list. Iterate through original list and check prev child for duplicates.

    Time complexity: O(n)

    :return:
    """

    print("Original List: ", dup_lis)

    new_lis = SinglyLinkedList()

    current_node = dup_lis.head
    prev_node = None
    while current_node:
        if prev_node is None or current_node.data != prev_node.data:
            new_lis.add(current_node.data)
        prev_node = current_node
        current_node = current_node.next

    print("Deduped List: ", new_lis)
    return new_lis


class Test(unittest.TestCase):
    def test_is_unique_true(self):
        linked_lis = SinglyLinkedList()
        linked_lis.add(1)
        linked_lis.add(1)
        linked_lis.add(1)
        linked_lis.add(2)
        linked_lis.add(2)
        linked_lis.add(3)

        deduped_lis = remove_duplicates(linked_lis)

        self.assertEqual(deduped_lis.as_list(), [1, 2, 3])
