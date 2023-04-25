map =  [[0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000],
        [0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000],
        [0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000],
        [0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000],
        [0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000],
        [0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000],
        [0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000],
        [0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000]]


title = None

lut = [[4, 4],[3, 4],[4, 3],[3, 3],[0, 0],[1, 0],[1, 1],[2, 1],[3, 1],[4, 1],[5, 1],[6, 1],[7, 1],[1, 2],[2, 2],[3, 2],[4, 2],[5, 2],[6, 2],[7, 2],[1, 3],[2, 3],[5, 3],[6, 3],[7, 3],[1, 4],[2, 4],[5, 4],[6, 4],[7, 4],[1, 5],[2, 5],[3, 5],[4, 5],[5, 5],[6, 5],[7, 5],[1, 6],[2, 6],[3, 6],[4, 6],[5, 6],[6, 6],[7, 6],[1, 7],[2, 7],[3, 7],[4, 7],[5, 7],[6, 7],[7, 7],[2, 0],[3, 0],[4, 0],[5, 0],[6, 0],[7, 0],[0, 7],[0, 6],[0, 5],[0, 4],[0, 3],[0, 2],[0, 1]]

from xml.dom.minidom import parse
import re

from tkinter import Tk
from tkinter.filedialog import askopenfilename

import json

# Open file picker

Tk().withdraw()
filename = askopenfilename()


# Open JSON file

with open(filename) as f:
    data = json.load(f)
    title = filename.split('/')[-1].split('.')[0]
    color = data['color']

    for i in range(8):
        for j in range(8):
            # convert #000000 to 0x000000
            map[i][j] = int(data['color'][i][j][1:], 16)
    

# Open SVG file
svg = parse('Matrix.svg')

# Crate a dict of all unique color
color_list = {}
for y in map:
    for x in y:
        if x == 0:
            continue
        color_str = '{:0>6X}'.format(x)
        if color_str not in color_list:
            # SVG color class
            style = f"""
              .c{color_str} {{
                fill: #{color_str};
              }}
            """
            # print(style)
            svg.getElementsByTagName("style")[0].firstChild.nodeValue += style

buttons = svg.getElementsByTagName("g")[1].getElementsByTagName("g")[3].getElementsByTagName("path")

minX = 100000
maxX = 0
minY = 100000
maxY = 0

for button in buttons:
    d = button.getAttribute('d')
    # print(d)
    match = re.search(r"M(\d+\.?\d*),(\d+\.?\d*)", d)
    # print(match.group(1), match.group(2))
    position = [float(match.group(1)), float(match.group(2))]

    if position[0] < minX:
        minX = position[0]
    if position[0] > maxX:
        maxX = position[0]
    if position[1] < minY:
        minY = position[1]
    if position[1] > maxY:
        maxY = position[1]

# 8x8 matrix of none
button_map = [[None for x in range(8)] for y in range(8)]

filled = []
# get index and button from buttons
for idx, button in enumerate(buttons):
    # d = button.getAttribute('d')
    # # print(d)
    # match = re.search(r"M(\d+\.?\d*),(\d+\.?\d*)", d)
    # # print(match.group(1), match.group(2))
    # position = [float(match.group(1)), float(match.group(2))]

    # x = round((position[0] - minX) / (maxX - minX) * 7)
    # y = round((position[1] - minY) / (maxY - minY) * 7)

    x = lut[idx][0]
    y = lut[idx][1]

    if x*1000+y in filled:
        continue

    button_map[y][x] = button

    if map[y][x] == 0:
        continue

    # print(f'x: {x}, y: {y}, color: {hex(map[y][x])}, rawx: {(position[0] - minX) / (maxX - minX) * 7}, rawy: {(position[1] - minY) / (maxY - minY) * 7}')

    color_str = '{:0>6X}'.format(map[y][x])
    button.setAttribute('class', 'c'+color_str)

    filled.append(x * 1000 + y)


with open(f'{title}.svg', 'w') as f:
    f.write(svg.toxml())
