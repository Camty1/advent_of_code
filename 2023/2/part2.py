# Day 2 of Advent of Code 2023 - Part 2
#
# Cameron Wolfe 12/2/2023

TEST = 'test1.txt'
FILE_NAME = 'day2.txt'

num_blocks = {'red': 12, 'green': 13, 'blue': 14}
sum = 0

with open(FILE_NAME, 'r') as file:

    while line := file.readline().strip():
        blocks_present = {'red': 0, 'green': 0, 'blue': 0}        
        line_split = line.split(":")
        game_number = int(line_split[0].split(" ")[1].strip())
        game_pieces = line_split[1].strip()

        for grab in game_pieces.split(";"):
            grab = grab.strip()
            for subgrab in grab.split(","):
                subgrab = subgrab.strip()
                split_subgrab = subgrab.split(" ")
                amount = int(split_subgrab[0])
                color = split_subgrab[1]
                blocks_present[color] = max(blocks_present[color], amount)
        set_power = 1
        for _, amount in blocks_present.items():
            set_power *= amount
        sum += set_power


print(sum)
