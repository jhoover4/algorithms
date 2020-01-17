import unittest

from .LinkedList import SinglyLinkedList


def delete_middle(node_to_remove):
    """
    Problem: Delete a node in the middle of a list without access to whole list (only single node).

    Answer: Use node next references to reference next node.

    Time complexity: O(n)

    :param Node node_to_remove:

    :return:
    """

    if node_to_remove is None:
        return ValueError("Node does not exist")

    next_node = node_to_remove.next
    node_to_remove = next_node

    return node_to_remove


class Test(unittest.TestCase):
    def test_delete_middle_node(self):
        linked_lis = SinglyLinkedList()
        linked_lis.add(1)
        linked_lis.add(2)
        middle_node = linked_lis.add(3)
        linked_lis.add(4)
        linked_lis.add(5)

        delete_middle(middle_node)

        self.assertEqual(linked_lis.as_list(), [1, 2, 4, 5])
