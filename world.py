""" world.py
#
# A file that represents the Vacuum World, keeping track of the
# position of all the objects and the agent, and
# moving them when necessary.
#
# Written by: Simon Parsons
# Modified by: Helen Harman
"""

import random
import config
import utils
from utils import Pose
from utils import Actions
from utils import State

class World():

    def __init__(self):

        # Import boundaries of the world. because we index from 0,
        # these are one less than the number of rows and columns.
        self.maxx = config.WORLD_LENGTH - 1
        self.maxy = config.WORLD_BREADTH - 1

        # Keep a list of locations that have been used.
        self.location_list = []

        
        # Vacuum
        self.vacuum_location = utils.pick_random_pose(self.maxx, self.maxy) 
        # To pick a specific start location:
        # self.vacuum_location = utils.Pose(14, 9)
        self.location_list.append(self.vacuum_location)

        
        # Dirt
        self.dirt_locations = []
        for i in range(config.NUMBER_OF_DIRTY_LOCATIONS):
            loc = utils.pick_unique_pose(self.maxx, self.maxy, self.location_list)
            self.dirt_locations.append(loc)
            self.location_list.append(loc)
        
        # To pick a specific dirty/goal location:
        # self.dirt_locations[0] = utils.Pose(1, 1)

        # Walls
        self.wall_locations = []
        for i in range(config.NUMBER_OF_WALL_LOCATIONS):
            loc = utils.pick_unique_pose(self.maxx, self.maxy, self.location_list)
            self.wall_locations.append(loc)
            self.location_list.append(loc)
        # To pick specific wall locations
        #self.wall_locations = [utils.Pose(2, 2), utils.Pose(5, 5)]    

        # Game state
        self.status = State.PLAY

        
    #--------------------------------------------------
 

    def get_vacuum_location(self):
        """ Where is the vacuum? """
        return self.vacuum_location

    def get_dirt_locations(self):
        """ Where are the dirty locations? """
        return self.dirt_locations
        
    def get_any_dirty_location(self):
        """ Get a randomly selected dirty location """
        return random.choice(self.dirt_locations)

    def is_vacuum_at_dirty_location(self):
        for i in range(len(self.dirt_locations)):
            if utils.same_location(self.vacuum_location, self.dirt_locations[i]):
                return True
        return False
 
    def is_traversable(self, loc):
        """ can the vacuum enter the provided location? """
        return ( (loc not in self.wall_locations) 
                   and (loc.x >= 0) and (loc.y >= 0) 
                    and (loc.x <= self.maxx) and (loc.y <= self.maxy) )
                    
    def is_xy_traversable(self, x, y):
        """ can the vacuum enter the provided x,y position? """
        return self.is_traversable(utils.Pose(x, y))
 
    def get_actions(self, location):
        """ returns the actions that can be taken from the provided location"""
        possible_moves = []
        
        if self.is_xy_traversable(location.x + 1, location.y):
            possible_moves.append(  Actions.MOVE_RIGHT )
             
        if self.is_xy_traversable(location.x - 1, location.y):
            possible_moves.append( Actions.MOVE_LEFT )
        
        if self.is_xy_traversable(location.x, location.y + 1):
            possible_moves.append( Actions.MOVE_DOWN )
        
        if self.is_xy_traversable(location.x, location.y - 1):
            possible_moves.append( Actions.MOVE_UP )
            
        return possible_moves
 
    def get_successor_state(self, location, action):
        """ returns the state/location we end up in if will apply action to location """
        if action == Actions.MOVE_RIGHT:
            return utils.Pose(location.x + 1, location.y)
        if action == Actions.MOVE_LEFT:
            return utils.Pose(location.x - 1, location.y)
        if action == Actions.MOVE_DOWN:
            return utils.Pose(location.x, location.y + 1)
        if action == Actions.MOVE_UP:
            return utils.Pose(location.x, location.y - 1)   

    def is_finished(self):
        """ Has the game come to an end? """
        if self.status == State.FINISHED:  
            print("Done!")
            return True
        return False
            
    #------------        
            
    def update_vacuum(self, action):
        """ execute the move """
        print("Executing action: ", action.name)
        
        if action == Actions.MOVE_LEFT:
            if self.vacuum_location.x > 0:
                self.vacuum_location.x = self.vacuum_location.x - 1
                
        elif action == Actions.MOVE_RIGHT:
            if self.vacuum_location.x < self.maxx:
                self.vacuum_location.x = self.vacuum_location.x + 1
                
        if action == Actions.MOVE_UP:
            if self.vacuum_location.y > 0:
                self.vacuum_location.y = self.vacuum_location.y - 1
                
        elif action == Actions.MOVE_DOWN:
            if self.vacuum_location.y < self.maxy:
                self.vacuum_location.y = self.vacuum_location.y + 1
                
        elif action == Actions.CLEAN: 
            index = -1
            for i in range(len(self.dirt_locations)):
                if utils.same_location(self.vacuum_location, self.dirt_locations[i]):
                    self.dirt_locations.pop(i)
                    break

        elif action == Actions.STOP:            
            self.status = State.FINISHED
        else: # noops
            pass
            
            
        

        
            
