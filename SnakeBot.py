"""
This is a basic framework for the fellas that will help them setup snake AI's.
There are some constants and functions I want you guys to be able to use to control the Snake itself, You'll see
them imported below. Feel free to rename anything you want, this is your file and can do whatever you want it to.

All of that being said, I will only take this file back from you, if you make changes to Snake.py itself, I will not be using those.

The goal is to - on average - have your bot achieve the longest snake possible.

We will run your bot through its paces an arbitrary number of times, but all bots will get the same number of chances to achieve high scores.

There is a prize for winning this competition

Please name your bot and uniquely name this file after your chosen bot name.

Author: (Your name here)
"""

# We will use left(), down(), right(), and up() to change the direction of the snake while in game
from Snake import heading_left as left, heading_down as down, heading_right as right, heading_up as up

# These will be useful to get both the current food location and the list of locations that the snake is currently taking up
from Snake import get_food_location, get_snake_position

# These are just some backend things for me to let you control the game while it's running.
from Snake import setup
from Snake import animate

FPS = 1

def snake_ai():
	# This is where the logic for your snake bot will go!
	# Feel free to make helper functions and use them as you see fit, this is essentially your main().
	
	snake = get_snake_position()  # This sets you up with the snake, which is stored as a list of tuples. e.g.: [(1, 2), (2, 2), (3, 2)]
	food_location = get_food_location()  # This is the current food location which returns as a tuple


def main():
	# This is all to set up the game and get your code running along side the game code.
	# Like Mertz always said, look at but do not modify the code below.

	canvas = setup(FPS)
	canvas.ontimer(snake_ai, int(round(1000 / FPS)))
	animate()
	canvas.mainloop()

if __name__ == "__main__":
	main()
