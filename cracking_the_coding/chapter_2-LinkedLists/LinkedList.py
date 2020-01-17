class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        return str(self.data)

    def add_tail(self, new_node):
        current_node = self

        while current_node:
            current_node = current_node.next

        current_node.next = new_node


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node_str = ""

        if self.is_empty():
            return node_str

        node = self.head

        while node:
            node_str += str(node.data)
            if node.next:
                node_str += " -> "

            node = node.next

        return node_str

    def is_empty(self):
        return self.head is None

    def add(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = new_node

        return new_node

    def remove(self, data):
        """
        Searches list to remove node that contains data provided.

        :param data:
        :return:
        """

        if self.is_empty():
            return 0

        node = self.head
        prev_node = None

        while node:
            if node.data == data:
                if prev_node:
                    prev_node.next = node
                else:
                    self.head = Node(data)
            prev_node = node
            node = node.next

        return data

    def size(self):
        node = self.head
        count = 0

        while node:
            node = node.next
            count += 1

        return count

    def as_list(self):
        """Mostly using this for testing purposes."""

        lis = []

        if self.is_empty():
            return None

        node = self.head
        while node:
            lis.append(node.data)
            node = node.next

        return lis
