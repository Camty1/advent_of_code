# Day 4 of Advent of Code 2023 - Part 1
#
# Cameron Wolfe 12/4/2023

TEST_INPUT = 'day4.txt'
SAMPLE_INPUT = 'test1.txt'

with open(TEST_INPUT, 'r') as file:
    sum = 0
    while line := file.readline():

        _, card = line.split(":")
        winning_numbers, your_numbers = card.strip().split("|")

        winning_number_list = winning_numbers.strip().split(" ")
        your_numbers_list = your_numbers.strip().split(" ")

        # print(winning_number_list, your_numbers_list)

        winning_numbers_set = set()

        for number in winning_number_list:
            if number:
                winning_numbers_set.add(number)

        num_matches = 0

        for number in your_numbers_list:
            if number and number in winning_numbers_set:
                num_matches += 1

        if num_matches > 0:
            sum += 2 ** (num_matches - 1)
        
    print(sum)


