class PriorityQueue:
    """
    Implemented with a min binary heap.

    Time complexity: O(n) - Time needed to create heap.
    """

    def __init__(self, lis=None):
        """
        :param None|List lis: If provided uses list to create PriorityQueue.
        """

        if lis is None:
            self.tree = [0]
            self.size = 0
        else:
            self.size = len(lis)
            self.tree = [0] + lis[:]

            i = self.size // 2
            while i > 0:
                self._sink(i)
                i = i - 1

    def __repr__(self):
        return ', '.join(str(a) for a in self.tree)

    def is_empty(self):
        return self.size > 0

    def insert_with_priority(self, item):
        self.tree.append(item)
        self.size += 1

        self._swim(self.size)

    def pull_highest_priority_element(self):
        """
        Pops last element in queue and restores order.

        :return:
        """

        popped_value = self.tree.pop(1)

        # Move last value to top.
        self.tree[1] = self.tree[self.size - 1]
        self.size -= 1

        # Restore tree order from new root downwards.
        self._sink(1)

        return popped_value

    def peek(self):
        """
        Returns highest priority element without removing.
        :return:
        """

        return self.tree[1]

    def _swim(self, index):
        """
        Moves node up the heap.

        :param int index: Index of node.
        :return:
        """

        while index // 2 > 0:
            parent_index = index // 2

            if self.tree[index] < self.tree[parent_index]:
                node = self.tree[index]
                self.tree[index] = self.tree[parent_index]
                self.tree[parent_index] = node

            index = parent_index

    def _sink(self, index):
        """
        Moves node down the heap.

        :param int index: Index of node.
        :return:
        """

        while (index * 2) <= self.size:
            min_child_index = self._min_child_index(index)

            if self.tree[index] > self.tree[min_child_index]:
                tmp = self.tree[index]
                self.tree[index] = self.tree[min_child_index]
                self.tree[min_child_index] = tmp
            index = min_child_index

    def _min_child_index(self, index):
        """
        Finds smallest child of parent.

        :param int index:
        :return int:
        """

        left_child_index = index * 2
        right_child_index = index * 2 + 1

        # We've reached the end of the tree
        if right_child_index > self.size:
            return left_child_index
        else:
            if self.tree[left_child_index] < self.tree[right_child_index]:
                return left_child_index
            else:
                return right_child_index
