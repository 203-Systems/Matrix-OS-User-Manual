batch_mode = True

from xml.dom.minidom import parse
from svgpathtools import parse_path

from tkinter import Tk
from tkinter.filedialog import askopenfilename, askdirectory

import os
import json

# Helper function to calculate center point
def calculate_center(d):
    path_alt = parse_path(d)
    bbox = path_alt.bbox()
    center_x = (bbox[0] + bbox[1]) / 2
    center_y = (bbox[2] + bbox[3]) / 2
    return center_x, center_y


def generate(title, map):
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

    buttons = svg.getElementsByTagName("g")[1].getElementsByTagName("path")

    minX = 100000
    maxX = 0
    minY = 100000
    maxY = 0

    lut = {}
    for idx, button in enumerate(buttons):
        d = button.getAttribute('d')
        position = calculate_center(d)

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
    # print(len(buttons))
    for idx, button in enumerate(buttons):
        d = button.getAttribute('d')
        position = calculate_center(d)

        x = round((position[0] - minX) / (maxX - minX) * 7)
        y = round((position[1] - minY) / (maxY - minY) * 7)

        # print(idx)

        # x = lut[idx][0]
        # y = lut[idx][1]

        # Create LUT
        # print(f"[{x}.{y}], ", end="")
        # print("{} - Center point: ({}, {}) - Pos: ({}, {})".format(idx, position[0], position[1], x, y))

        if x * 1000 + y in filled:
            continue

        button_map[y][x] = button

        if map[y][x] == 0:
            continue

        # print(f'x: {x}, y: {y}, color: {hex(map[y][x])}, rawx: {(position[0] - minX) / (maxX - minX) * 7}, rawy: {(position[1] - minY) / (maxY - minY) * 7}')

        color_str = '{:0>6X}'.format(map[y][x])
        button.setAttribute('class', 'c' + color_str)

        filled.append(x * 1000 + y)

    # print(f"Title: {title}")
    with open(f'{title}.svg', 'w') as f:
        f.write(svg.toxml())


map =  [[0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000],
        [0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000],
        [0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000],
        [0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000],
        [0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000],
        [0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000],
        [0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000],
        [0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000]]

if __name__ == '__main__' and batch_mode:
    print("Select folder contains all Jsons")
    # Open file picker
    Tk().withdraw()
    path = askdirectory()

    filenames = []
    for root, dirs, files in os.walk(path):  # Walk through the current directory and its subdirectories
        for file in files:
            if file.endswith('.json'):
                filenames.append(os.path.join(root, file).replace('\\', '/'))

    # Open JSON file
    for filename in filenames:
        with open(filename) as f:
            title = file_name = os.path.splitext(os.path.basename(filename))[0]
            data = json.load(f)
            title = filename.split('/')[-1].split('.')[0]
            color = data['color']

            for i in range(8):
                for j in range(8):
                    # convert #000000 to 0x000000
                    map[i][j] = int(data['color'][i][j][1:], 16)

            print(f"Generating {filename} - {title}")
            generate(title, map)

if __name__ == '__main__' and not batch_mode:
    print("Select UI Json")
    # Open file picker
    Tk().withdraw()
    filename = askopenfilename()

    # Open JSON file
    with open(filename) as f:
        title = file_name = os.path.splitext(os.path.basename(filename))[0]
        data = json.load(f)
        title = filename.split('/')[-1].split('.')[0]
        color = data['color']

        for i in range(8):
            for j in range(8):
                # convert #000000 to 0x000000
                map[i][j] = int(data['color'][i][j][1:], 16)

        generate(title, map)
