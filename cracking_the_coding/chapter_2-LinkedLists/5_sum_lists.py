import unittest

from .LinkedList import SinglyLinkedList


def sum_lists(lis1, lis2):
    """
    Problem: Each node in a list represents a digit in a number, reversed, so 1 -> 2 -> 3 = 321.
    Add these final numbers together and return the sum as a reversed linked list as well,
    so 1 -> 2 -> 3 + 2 -> 3 -> 4 = 3 -> 5 -> 7.

    Answer: Create a new list. Loop over both given lists and add result to new list, while carrying over remainder for
    next nodes. If there are additional nodes in one list stop looping over other list and just add new digits plus
    remainder.

    Time complexity: O(n)

    :param LinkedList lis1:
    :param LinkedList lis2:

    :return int sum:
    """

    carry = 0
    sum_lis = SinglyLinkedList()

    lis1_node = lis1.head
    lis2_node = lis2.head

    while lis1_node or lis2_node:
        if not lis1_node:
            sum_lis.add(lis2_node.data + carry)
            lis2_node = lis2_node.next
            carry = 0
        if not lis2_node:
            sum_lis.add(lis1_node.data + carry)
            lis1_node = lis1_node.next
            carry = 0
        else:
            sum_data = lis1_node.data + lis2_node.data + carry
            if len(str(sum_data)) > 1:
                carry = int(str(sum_data)[0])
                sum_data = int(str(sum_data)[1])
            else:
                carry = 0

            sum_lis.add(sum_data)

            lis1_node = lis1_node.next
            lis2_node = lis2_node.next

    return sum_lis

# TODO: Implement to store forwards?


class Test(unittest.TestCase):
    def sum_linked_list_rev(self):
        """
        7 -> 1 -> 6 + 5 -> 9 -> 2 = 2 -> 1 -> 9
        """

        first_lis = SinglyLinkedList()
        first_lis.add(7)
        first_lis.add(1)
        first_lis.add(6)

        second_lis = SinglyLinkedList()
        second_lis.add(5)
        second_lis.add(9)
        second_lis.add(2)

        result_list = sum_lists(first_lis, second_lis)

        self.assertEqual(result_list.as_list(), [2, 1, 9])
