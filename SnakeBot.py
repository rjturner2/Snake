"""
This is a basic framework for the fellas that will help them setup snake AI's.
There are some constants and functions I want you guys to be able to use to control the Snake itself, You'll see
them imported below. Feel free to rename anything you want, this is your file and can do whatever you want it to.

All of that being said, I will only take this file back from you, if you make changes to Snake.py itself, I will not be using those.

The goal is to - on average - have your bot achieve the longest snake possible.

We will run your bot through its paces an arbitrary number of times - ideally in the hundreds.

There is a prize for winning this competition, but I'm not sure what it is quite yet. I'll anounce it at some point

Please name your bot and uniquely name this file after your chosen bot name.

Author: (Your name here)
"""

# We will use left(), down(), right(), and up() to change the direction of the snake while in game
from Snake import heading_left as left, heading_down as down, heading_right as right, heading_up as up

# These will be useful to get both the current food location and the list of locations that the snake is currently taking up
from Snake import get_food_location, get_snake_position, get_grid_density, get_current_heading

# These are just some backend things for me to let you control the game while it's running.
from Snake import setup, animate

FPS = 1
canvas = setup(FPS)  # We send the FPS target to our setup function and it returns the Screen object, probably a little dumb but oh well.

def snake_ai():
	# This is where the logic for your snake bot will go!
	# Feel free to make helper functions and use them as you see fit, this is essentially your main().
	# Also the variables I define below can be renamed however you choose.
	
	snake = get_snake_position()  # This sets you up with the snake, which is stored as a list of tuples. e.g.: [(1, 2), (2, 2), (3, 2)] Index 0 is the head, and it works back from there
	food_location = get_food_location()  # This is the current food location which returns as a tuple
	max_x_location, max_y_location = get_grid_density()  # This will give you the maximum index allowable by the game, your snake will run into a wall if it goes further than either of these values or below zero.
	current_heading = get_current_heading()  # This returns the current heading as a string that looks like "up", "down", "left", or "right"

	######## YOUR CODE HERE ########

	# finally we need to recall snake_ai so our control keeps up with the animation of the game, probably don't remove this unless you want to lose or you've got something really clever going on.
	canvas.ontimer(snake_ai, int(round(1000 / FPS)))


def main():
	# This is all to set up the game and get your code running along side the game code.
	# Like Mertz always said, look at but do not modify the code below.
	animate()
	canvas.ontimer(snake_ai, int(round(1000 / FPS)))
	canvas.mainloop()

if __name__ == "__main__":
	main()
