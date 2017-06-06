# -*- coding: utf-8 -*-
from a_star import Node, a_star

from .utils import build_graph, g, euclid

from functools import partial


def successors(x, y):
    ss = [Node(x + 1, y), Node(x - 1, y),
          Node(x, y + 1), Node(x, y - 1)]

    ss += [Node(x + 1, y + 1), Node(x - 1, y - 1),
           Node(x - 1, y + 1), Node(x + 1, y - 1)]
    yield from ss


def h(node1, node2, N, e, *, d):
    """If node has 8 neighbors"""
    d_node1 = d(node1)
    if d_node1 < N:
        w = 1 - (d_node1 / N)
    else:
        w = 0
    return (1 + e * w) * euclid(node1, node2)


def dynamic_weighting():
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
    filename = 'illustrations/dynamic_weighting.gif'
    dm_h = partial(h, N=euclid(start, stop), e=5, d=g)
    a_star(start, stop, graph, g, dm_h, filename=filename)
