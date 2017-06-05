# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw


def get_xy(x, y, size, margin=2):
    x0 = x * size + margin
    y0 = y * size + margin
    x1 = (x + 1) * size - margin - 1
    y1 = (y + 1) * size - margin - 1
    return x0, y0, x1, y1


def draw_graph(graph, path, closed, size, path_color='green',
               closed_color='blue'):
    side = graph.side
    image = Image.new('RGB', (side * size, side * size), 'black')
    draw = ImageDraw.Draw(image)

    path = set(path)
    closed = set(closed)
    for node in graph.get_nodes():
        if node in path:
            color = path_color
        elif node in closed:
            color = closed_color
        else:
            color = 'white'
        draw.rectangle(get_xy(node.x, node.y, size), fill=color)
    return image


def write_gif(filename, images, duration=500):
    image = images.pop(0)
    image.save(filename, append_images=images, duration=duration, save_all=True)
