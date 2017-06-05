# -*- coding: utf-8 -*-
import heapq
import itertools

from .graph import Path
from .drawing import draw_graph, write_gif


class PriorityQueue:
    def __init__(self):
        self.items = []
        self.counter = itertools.count()

    def add(self, item, priority):
        count = next(self.counter)
        entry = (priority, count, item)
        heapq.heappush(self.items, entry)

    def pop(self):
        priority, count, item = heapq.heappop(self.items)
        return item

    def __bool__(self):
        return bool(self.items)


def a_star(start, stop, graph, g, h, *, filename=None):
    """Implementation of a start algorithm"""
    gifed = bool(filename)
    images = []
    start = Path.from_node(start, None)
    closed = set()
    opened = PriorityQueue()
    opened.add(start, g(start) + h(start, stop))
    count = 0
    while opened:
        current = opened.pop()
        if current in closed:
            continue
        if gifed:
            im = draw_graph(graph, current.path, closed, 100)
            # im.save('ims/im{}.JPG'.format(count))  # for debug
            count += 1
            images.append(im)
        if current == stop:
            if gifed:
                write_gif(filename, images)
            return current.path, closed
        closed.add(current)
        for successor in graph.successors(current):
            successor = Path.from_node(successor, current)
            opened.add(successor, g(successor) + h(successor, stop))
    return None, closed
