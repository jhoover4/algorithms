import unittest

from .LinkedList import Node, SinglyLinkedList


def partition(lis, partition_val):
    """
    Problem: Partition list where all values before partition value are to the left and all values greater than or
    equal to x are on the right.

    Answer: Create new list. Loop through original list. If node value in original list less than partition,
    add to head, else add to tail.

    Time complexity: O(n^2)?

    :param LinkedList lis:
    :param int partition_val:

    :return:
    """

    if not lis.head:
        return lis

    partitioned_lis = SinglyLinkedList()

    node = lis.head
    while node:
        if node.data < partition_val:
            partition_head = partitioned_lis.head
            new_node = Node(node.data)

            if not partition_head:
                partitioned_lis.head = new_node
            else:
                new_node.next = partition_head
                partitioned_lis.head = new_node
        else:
            partitioned_lis.add(node.data)

        node = node.next

    return partitioned_lis


class Test(unittest.TestCase):
    def test_partition_linked_list(self):
        linked_lis = SinglyLinkedList()
        linked_lis.add(3)
        linked_lis.add(5)
        linked_lis.add(8)
        linked_lis.add(5)
        linked_lis.add(10)
        linked_lis.add(2)
        linked_lis.add(1)

        partitioned_lis = partition(linked_lis, 5)

        self.assertEqual(partitioned_lis.as_list(), [1, 2, 3, 5, 8, 5, 10])
