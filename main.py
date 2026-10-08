""" main.py
#
# The top level loop that runs the world until it is clean.
#
# run this using:
#
# python3 main.py
#
# Written by: Simon Parsons
# Modified by: Helen Harman
"""

from world import World
from vacuum  import Vacuum
from dirty_environment import DirtyEnvironment
import random
import config
import utils
import time

def start():
    # Create a world, then connect the agent.
    world = World()
    agent = Vacuum(world)

    # Show initial state    
    display = DirtyEnvironment(world)
    display.update()
    time.sleep(1)

    # Now run game...
    while not(world.is_finished()):
        world.update_vacuum(agent.make_move())
        display.update()
        time.sleep(0.5)

if __name__ == "__main__":
    start()
