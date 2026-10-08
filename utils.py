""" utils.py
#
# Some useful methods that are used in different places in the code.
#
# Written by: Simon Parsons
# Modified by: Helen Harman
"""

import random
import math
from enum import Enum

class Actions(Enum):
    """Representation of directions"""
    MOVE_LEFT = 0
    MOVE_RIGHT = 1
    MOVE_UP = 2
    MOVE_DOWN = 3
    CLEAN  = 4
    STOP = 5
    NOOPS = 6 # no operations

class State(Enum):
    """ representation of game state """
    PLAY = 0
    FINISHED  = 1
    
    
class Location(Enum):
    LEFT = 0
    RIGHT = 1
    
class LocState(Enum):
    CLEAR = 0
    DIRTY = 1

class Pose():
    """ Class to represent the position of elements within the game """
    x = 0
    y = 0
    
    def __init__(self, *args): 
        if len(args) > 1:
            self.x = args[0]
            self.y = args[1]
              
    def print(self):
        print('[', self.x, ',', self.y, ']')
        
    
    def __repr__(self):
        return f"<Pose x:{self.x} y:{self.y}>"
            
    def __str__(self):
        return f"[{self.x},{self.y}]"
        
    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Pose):
            return (self.x == other.x and self.y == other.y)
        return False


def same_location(pose1, pose2):
    """ Check if two game elements are in the same location """
    return pose1 == pose2

def separation(pose1, pose2):
    """ Return distance between two game elements. """
    return math.sqrt((pose1.x - pose2.x) ** 2 + (pose1.y - pose2.y) ** 2)# could just use math.dist

def checkBounds(max, dimension):
    """ Make sure that a location doesn't step outside the bounds on the world. """
    if (dimension > max):
        dimension = max
    if (dimension < 0):
        dimension = 0

    return dimension

def pick_random_pose(x, y):
    """  Pick a location in the range [0, x] and [0, y]
         Used to randomize the initial conditions. """
    p = Pose()
    p.x = random.randint(0, x)
    p.y = random.randint(0, y)

    return p

def pick_unique_pose(x, y, taken):
    """ Pick a unique location, in the range [0, x] and [0, y], given a list
         of locations that have already been chosen. """
    unique_choice = False
    while(not unique_choice):
        candidate_pose = pick_random_pose(x, y)
        if not contained_in(candidate_pose, taken):
            unique_choice = True
    return candidate_pose

def contained_in(pose, poses):
    """ Check if a pose with the same x and y is already in poses. """
    return pose in poses
