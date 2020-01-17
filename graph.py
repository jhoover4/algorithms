import collections


class Graph:
    """
    """

    def __init__(self, arr):
        # if arr:
        #     for item in arr:


        self.nodes = []

    def breadth_first_search(self, start):
        """
        :param start: The beginning node.
        :return []:
        """

        # TODO: Ability to have end?

        if not self.nodes:
            return 0

        node_names = []

        current_node = self.nodes[start]
        current_node.marked = True
        queue = collections.deque(current_node)

        while len(queue) > 0:
            current_node = queue.popleft()
            node_names.append(current_node.name)

            for node in current_node.adjacent:
                if not node.marked:
                    node.marked = True
                    queue.append(node)

        return node_names


class Node:
    def __init__(self):
        self.name = ''
        self.adjacent = []
        self.marked = False  # for bfs
