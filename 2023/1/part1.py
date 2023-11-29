# Day 1 of Advent of Code 2023 - Part 1
#
# Cameron Wolfe 12/1/2023

FILE_NAME = "day1.txt"
TEST = "test.txt"

sum = 0

with open(FILE_NAME, 'r') as file:
    
    while line := file.readline():
        
        first, last = -1, -1

        for i in range(len(line)):
        
            try:
                num = int(line[i])
            except:
                continue

            if first == -1:
                first = num
            
            last = num

        sum += 10*first + last

    print(sum)
