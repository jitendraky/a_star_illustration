# -*- coding: utf-8 -*-
import math
from itertools import tee

from a_star import Node, Graph


def euclid(node1, node2):
    return math.sqrt((node1.x - node2.x) ** 2 + (node1.y - node2.y) ** 2)


def g(node):
    """Default distance between nodes is 1"""
    first, second = tee(node.path, 2)
    next(second, None)
    return sum(euclid(node1, node2) for node1, node2 in zip(first, second))


def rectangle_walk(width, height):
    for x in range(width):
        for y in range(height):
            yield Node(x, y)


def inside(node, side):
    """Returns True if node is inside rectangle else False"""
    return 0 <= node.x < side and 0 <= node.y < side


def build_graph(side, get_successors, *walls):
    """Create a graph with unreachable nodes in walls"""
    graph = Graph()
    for node in rectangle_walk(side, side):
        if node in walls or not inside(node, side):
            continue
        for suc in get_successors(node.x, node.y):
            if suc in walls or not inside(suc, side):
                continue
            graph.add_edge(node, suc, 1)
    graph.side = side
    return graph
