# Day 3 of Advent of Code 2023 - Part 2
#
# Cameron Wolfe 12/3/2023

import numpy as np

def get_neighbors(location, dim_1, dim_2):
    neighbors = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            a = location[0] + i
            b = location[1] + j
            if (a >= 0 and a < dim_1) and (b >= 0 and b < dim_2):
                neighbors.append((a,b))
    
    neighbors.remove(location)

    return neighbors


TEST = 'test1.txt'
SAMPLE_INPUT = 'day3.txt'

symbol_set = set()
number_set = [str(x) for x in range(10)]

with open(SAMPLE_INPUT, 'r') as file:
    
    c = file.read(1)
    line_width = -1
    file_height = -1
    width_counter = 0
    line_counter = 0
    while c:
        width_counter += 1
        try:
            int(c)
        except:
            if c != '\n' and c != '.':
                symbol_set.add(c)
            elif c == '\n':
                if line_width == -1:
                    line_width = width_counter - 1
                line_counter += 1

        c = file.read(1)
    file_height = line_counter

    gears = []
    numbers = -np.ones((file_height, line_width), dtype=int)
    number_values = []

    file.seek(0)

    c = file.read(1)
    reading_number = False
    width_counter = 0
    line_counter = 0
    number_counter = 0
    number_container = ""
    while c:
        if c in number_set:
            reading_number = True
            number_container += c
            numbers[line_counter, width_counter] = number_counter
        else:
            if reading_number:
                reading_number = False
                number_values.append(int(number_container))
                number_container = ""
                number_counter += 1

            if c == '*':
                gears.append((line_counter, width_counter))
            
            if c == '\n':
                width_counter = -1
                line_counter += 1

        width_counter += 1
        c = file.read(1)

    sum = 0
    for gear_location in gears:
        added = []
        neighbors = get_neighbors(gear_location, line_width, file_height)

        for neighbor in neighbors:
            neighbor_value = numbers[neighbor[0], neighbor[1]]

            if neighbor_value != -1 and not neighbor_value in added:
                added.append(neighbor_value)
                if len(added) == 2:
                    sum += number_values[added[0]] * number_values[added[1]]

    print(sum)

