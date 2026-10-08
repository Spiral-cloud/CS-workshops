""" vacuum.py
#
# The code that defines the behaviour of the vacuum. 
#
# Written by: Simon Parsons
# Modified by: Helen Harman
"""

import world
import random
import utils
from utils import Actions
from utils import Location
from utils import LocState

from node import Node

class Vacuum():

    def __init__(self, world):
        # Make a copy of the world attribute, so that the agent can query the state of the world
        self.world = world 

        # The moves/actions that the agent can take.
        self.moves = [Actions.MOVE_LEFT, Actions.MOVE_RIGHT, Actions.MOVE_UP, Actions.MOVE_DOWN, Actions.CLEAN]
       
        # The output of the search method and the path the agent will move along
        self.path = []  
        # Used to move the agent along the path one step at a time    
        self.path_index = 0 
          
    
    
    def make_move(self):
        """ return the action that the agent should execute. """
        # if we haven't created a path yet, create one
        if not self.path:
            # getting the starting and end locations from the world
            initial_state = self.world.get_vacuum_location()
            goal_state = self.world.get_any_dirty_location()
            
            ####################
            # Edit this to call the search methods you write
            # Call the search method:
            self.path = self.iterative_deepening_search(initial_state, goal_state)
            #################
        
        # if we have traversed the path and cleaned the location, then stop
        if self.path_index == len(self.path) and not self.world.is_vacuum_at_dirty_location():
            return Actions.STOP
        # if we have reached the dirty location, then clean that location
        if self.path_index == len(self.path):
            return Actions.CLEAN
        
        # keep moving along the path:    
        self.path_index = self.path_index + 1  
        return self.path[self.path_index - 1]

    def breadth_first_search(self, initial_state, goal):
        node = Node(initial_state, None,  None)

        if node.is_goal(goal):
            print("Initial state and goal are the same")
            return[]
        frontiers = [node]
        explored = []
        while frontiers:
            node = frontiers.pop(0)
            explored.append(node)
            for action in self.world.get_actions(node.location):
                child = self.create_child_node(node,action)
                if child not in explored and child not in frontiers:
                    if child.is_goal(goal):
                        print("Found goal")
                        return self.recover_plan(child)
                    frontiers.append(child)
        print("Failed to find a path")
        return []

    def depth_limited_search(self,initial_state, goal):
        limit = 3
        node = Node(initial_state, None, None)
        if node.is_goal(goal):
            print("Initial state and goal are the same")
            return []
        frontiers = [node]
        explored = []
        while frontiers:
            depth = 0
            node = frontiers.pop()
            explored.append(node)
            if depth >= limit:
                print("cutoff")
            else:
                for action in self.world.get_actions(node.location):
                    child = self.create_child_node(node,action)
                    if child not in explored and child not in frontiers:
                        frontiers.append(child)
            if child.is_goal(goal):
                print("Found goal")
                return self.recover_plan(child)
                

    def iterative_deepening_search(self, initial_state,goal):
        limit = 3
        depth = 0
        while True:
            result = self.depth_limited_search(initial_state, goal, depth)
            if result != "cutoff":
                return result
            depth +=1

    
    def depth_first_search(self, initial_state, goal):    
        """Depth first search"""
        node = Node(initial_state, None, None)
        
        # goal test:
        if node.is_goal(goal):
            print("Initial state and goal are the same")
            return []
        
        frontiers = [node] 
        explored = []        
        
        while frontiers:
            node = frontiers[0] # get the first item
            frontiers = frontiers[1:] # remove the first item
            
            explored.append(node)
            
            # for each action the vacuum can take
            for action in self.world.get_actions(node.location):
                child = self.create_child_node(node, action) 
                # note, in the Node class we override the equals operator. Two nodes are equal if the location is the same (which means we can use "not in" here). 
                if child not in explored and child not in frontiers:   
                    if child.is_goal(goal):
                        print("Found goal")
                        return self.recover_plan(child)
                    frontiers.insert(0, child)  # add to front                        
        
        print("Failed to find a path")
        return []
    
    
    
    """ Creates a child node of the parent for the given action."""
    def create_child_node(self, parent, action):
        successor_state = self.world.get_successor_state(parent.location, action)
        return Node(successor_state, parent, action)
        
            
    """ methods for removing the plan once the goal has been found """
    def recover_plan(self, child):
        plan = []
        self.recover_plan_recursive(child, plan)
        return plan
        
    def recover_plan_recursive(self, node, plan):
        if node.parent:            
            self.recover_plan_recursive(node.parent, plan)
            plan.append(node.action)
       
       
