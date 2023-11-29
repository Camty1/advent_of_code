#!/bin/bash

YEAR=$(date +%Y)

if [ -d $YEAR ]; then
	echo "$YEAR is already initialized"
else
	echo "Initializing $YEAR"	
	mkdir "$YEAR"

	for DAY in {1..25}; do
		mkdir "$YEAR/$DAY"
		echo -e "# Day $DAY of Advent of Code $YEAR - Part 1\n#\n# Cameron Wolfe 12/$DAY/$YEAR" > "./$YEAR/$DAY/part1.py"
		echo -e "# Day $DAY of Advent of Code $YEAR - Part 2\n#\n# Cameron Wolfe 12/$DAY/$YEAR" > "./$YEAR/$DAY/part2.py"
	done
fi
