"""
This function will average the Snake bot scores

Author: (Ryley Turner)
"""

FILE_NAME = "HighScores.txt"

my_file = open(FILE_NAME, "r")

accumulation = 0
line_count = 0

for line in my_file:
	accumulation += int(line.strip())
	line_count += 1

print(accumulation / line_count)