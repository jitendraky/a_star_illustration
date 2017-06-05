# -*- coding: utf-8 -*-
class Graph:
    def __init__(self):
        self._edges = {}
        self.side = 0

    def add_edge(self, src_node, dest_node, length):
        self._edges[(src_node, dest_node)] = length

    def get_edge(self, src_node, dest_node):
        return self._edges[(src_node, dest_node)]

    def successors(self, node):
        """Find all linked nodes"""
        for src_node, dest_node in self._edges.keys():
            if node == src_node:
                yield dest_node

    def get_nodes(self):
        nodes = set()
        for edge in self._edges.keys():
            nodes.update(edge)
        return list(nodes)


class Node:
    """Graph node class"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        """Return a nicely formatted representation string"""
        return '{self.__class__.__name__}(x={self.x}, y={self.y})'.format(
            self=self
        )


class Path(Node):
    """Node that keeps path"""

    def __init__(self, x, y, prev=None):
        super().__init__(x, y)
        self.prev = prev

    @classmethod
    def from_node(cls, node, prev):
        return cls(node.x, node.y, prev)

    @property
    def path(self):
        current = self
        while current:
            yield current
            current = current.prev
