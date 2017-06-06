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


def h(node1, node2, l1, l2, *, g):
    """If node has 8 neighbors"""
    g_n = g(node1)
    path = node1.path
    parent = next(path)
    try:
        parent = next(path)
    except StopIteration:
        pass
    g_p = g(parent)
    if g_p <= g_n:
        w = l1
    else:
        w = l2
    h_n = euclid(node1, node2)
    return h_n + w * (g_n + h_n)


def alpha():
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
    filename = 'illustrations/alpha.gif'
    fa_h = partial(h, l1=1, l2=2, g=g)
    a_star(start, stop, graph, g, fa_h, filename=filename)
