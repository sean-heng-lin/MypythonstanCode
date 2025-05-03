"""
File: PotholeFilling.py
Name: TODO:
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *
from StepUp import*

def main():
    """
    sean:
    """
    #algorithm
    for i in range(3):
        move_in()
        put_99()
        move_out()

def move_in():
    """
    pre-condition:Karel is at the upper left of the pothole facing East
    post-condition:Karel is in the pothole facing South
    """
    move()
    turn_right()
    move()

def move_out():
    """
    pre-condition:Karel is in the pothole facing South
    post-condition:Karel is at the upper left of the pothole facing East
    """
    turn_around()
    move()
    turn_right()
    move()

def turn_around():
    """
    pre-condition:Karel is in the pothole facing South
    post-condition:Karel is in the pothole facing North
    """
    for i in range(2):
        turn_left()
# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
