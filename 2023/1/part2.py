# Day 1 of Advent of Code 2023 - Part 2
#
# Cameron Wolfe 12/1/2023

FILE_NAME = "day1.txt"
TEST = "test2.txt"

number_words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

sum = 0
with open(FILE_NAME, 'r') as file:
    
    while line := file.readline():
        
        first, last = -1, -1
        last_number_index = 0

        for i in range(len(line)):
        
            try:
                num = int(line[i])
            except:
                num = -1
                for j in range(len(number_words)):
                    if number_words[j] in line[last_number_index:i+1]:
                        num = j+1
                        break
                if num == -1:
                    continue

            if first == -1:
                first = num
            
            last = num
            last_number_index = i
        print(first,last)
        sum += 10*first + last

    print(sum)
