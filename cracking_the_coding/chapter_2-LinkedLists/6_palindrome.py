import unittest
from collections import deque

from .LinkedList import SinglyLinkedList


def palindrome(lis):
    """
    Problem: Check if a linked list is a palindrome.

    Answer: Check for palindrome using a stack. Use two pointers, the second will skip ahead by two to find the length.
    Once length is found, we begin popping from the stack to check if there's a palindrome.

    Time complexity: O(n)

    :param LinkedList lis:

    :return bool:
    """

    pointer1 = lis.head
    pointer2 = lis.head

    if not pointer1 or not pointer1.next:
        return False

    stack = deque()
    length = 1
    length_found = False

    while pointer1:
        data = pointer1.data

        if length_found:
            last = stack.pop()
            # Stack doesn't match
            if last != data:
                return False

        else:
            stack.append(data)

            if pointer2.next and pointer2.next.next:
                length += 2
                pointer2 = pointer2.next.next
            else:
                if pointer2.next:
                    length += 1
                length_found = True

                # If its odd, don't need to repeat the middle entry
                if length % 2 != 0:
                    stack.pop()

        pointer1 = pointer1.next

    return True


class Test(unittest.TestCase):
    def test_is_palindrome(self):
        linked_lis = SinglyLinkedList()
        linked_lis.add(1)
        linked_lis.add(2)
        linked_lis.add(3)
        linked_lis.add(2)
        linked_lis.add(1)

        self.assertTrue(palindrome(linked_lis))

    def test_is_not_palindrome(self):
        linked_lis = SinglyLinkedList()
        linked_lis.add(1)
        linked_lis.add(7)
        linked_lis.add(3)
        linked_lis.add(5)
        linked_lis.add(1)

        self.assertFalse(palindrome(linked_lis))
