from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


# TODO Create a turtle player that starts at the bottom of the screen and listen for the 
#  "Up" keypress to move the turtle north

class Player(Turtle):
    # These two lines of code simple mean that the player class can do everything that the turtle class can do, but
    # we can now add more to it. You can get the super call using the lightbulb!
    def __init__(self):
        super().__init__()

