# Day 4 of Advent of Code 2023 - Part 2
#
# Cameron Wolfe 12/4/2023

TEST_INPUT = 'day4.txt'
SAMPLE_INPUT = 'test1.txt'

with open(TEST_INPUT, 'r') as file:
    total = 0
    current_card = 0
    num_cards = [1 for line in file]
    file.seek(0)
    
    while line := file.readline():
        _, card = line.split(":")
        winning_numbers, your_numbers = card.strip().split("|")

        winning_number_list = winning_numbers.strip().split(" ")
        your_numbers_list = your_numbers.strip().split(" ")

        winning_numbers_set = set()

        for number in winning_number_list:
            if number:
                winning_numbers_set.add(number)

        num_matches = 0

        for number in your_numbers_list:
            if number and number in winning_numbers_set:
                num_matches += 1

        if num_matches > 0:
            for i in range(0, num_matches):
                num_cards[current_card + 1 + i] += num_cards[current_card]

        current_card += 1
        
    print(num_cards)
    print(sum(num_cards))
