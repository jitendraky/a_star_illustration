# -*- coding: utf-8 -*-
from a_star import Node, a_star
from .utils import build_graph, g


def successors(x, y):
    ss = [Node(x + 1, y), Node(x - 1, y),
          Node(x, y + 1), Node(x, y - 1)]
    yield from ss


def h(node1, node2, e=1):
    """If node has 4 neighbors"""
    return e * (abs(node1.x - node2.x) + abs(node1.y - node2.y))


def classic_4_neighbors():
    side = 10
    walls = (
        Node(2, 3), Node(3, 3), Node(4, 3), Node(5, 3), Node(6, 3), Node(7, 3),
        Node(2, 4), Node(3, 4), Node(4, 4), Node(5, 4), Node(6, 4), Node(7, 4),
                                                        Node(6, 5), Node(7, 5),
                                                        Node(6, 6), Node(7, 6)
    )
    start = Node(0, 9)
    stop = Node(9, 0)
    graph = build_graph(side, successors, *walls)
    filename = 'illustrations/classic_4_neighbors.gif'
    a_star(start, stop, graph, g, h, filename=filename)
