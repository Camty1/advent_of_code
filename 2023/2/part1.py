# Day 2 of Advent of Code 2023 - Part 1
#
# Cameron Wolfe 12/2/2023

TEST = 'test1.txt'
FILE_NAME = 'day2.txt'

num_blocks = {'red': 12, 'green': 13, 'blue': 14}
sum = 0

with open(FILE_NAME, 'r') as file:

    while line := file.readline().strip():
        
        line_split = line.split(":")
        game_number = int(line_split[0].split(" ")[1].strip())
        game_pieces = line_split[1].strip()

        valid = True
        for grab in game_pieces.split(";"):
            grab = grab.strip()
            for subgrab in grab.split(","):
                subgrab = subgrab.strip()
                split_subgrab = subgrab.split(" ")
                amount = int(split_subgrab[0])
                color = split_subgrab[1]
                if amount > num_blocks[color]:
                    valid = False

        if valid:
            sum += game_number


print(sum)
