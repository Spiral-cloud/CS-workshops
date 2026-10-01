""" vacuum.py
#
# The code that defines the behaviour of the vacuum. You should be able to
# do all you need in here, using access methods from world.py, and
# using makeMove() to generate the next move.
#
# Written by: Simon Parsons
# Modified by: Helen Harman
# Last Modified: 01/02/24
"""

import world
import random
import utils
from utils import Actions
#
from utils import Location
from utils import LocState

class Vacuum():

    def __init__(self, world):

        # Make a copy of the world an attribute, so that Link can
        # query the state of the world
        self.world = world

        # What moves are possible.
        self.moves = [Actions.MOVE_LEFT, Actions.MOVE_RIGHT, Actions.CLEAN]
       
        # table for table-driven agent:
        self.action_table = [ #  percept sequence,                                                                         Action
            [ [{Location.LEFT : LocState.CLEAR}],                                                                     Actions.MOVE_RIGHT ],
            [ [{Location.LEFT : LocState.DIRTY}],                                                                     Actions.CLEAN      ],
            [ [{Location.RIGHT: LocState.CLEAR}],                                                                     Actions.MOVE_LEFT  ],
            [ [{Location.RIGHT: LocState.DIRTY}],                                                                     Actions.CLEAN      ],
            [ [{Location.LEFT : LocState.DIRTY}, {Location.LEFT : LocState.CLEAR}],                                   Actions.MOVE_RIGHT ],
            [ [{Location.LEFT : LocState.CLEAR}, {Location.RIGHT: LocState.DIRTY}],                                   Actions.CLEAN      ],
            [ [{Location.RIGHT: LocState.CLEAR}, {Location.LEFT : LocState.DIRTY}],                                   Actions.CLEAN      ],
            [ [{Location.RIGHT: LocState.DIRTY}, {Location.RIGHT: LocState.CLEAR}],                                   Actions.MOVE_LEFT  ], 
            [ [{Location.LEFT : LocState.DIRTY}, {Location.LEFT : LocState.CLEAR}, {Location.RIGHT: LocState.DIRTY}], Actions.CLEAN      ],
            [ [{Location.RIGHT: LocState.DIRTY}, {Location.RIGHT: LocState.CLEAR}, {Location.LEFT : LocState.DIRTY}], Actions.CLEAN      ],         
            # Finish:
            [ [{Location.LEFT : LocState.DIRTY}, {Location.LEFT : LocState.CLEAR}, {Location.RIGHT: LocState.DIRTY}, {Location.RIGHT: LocState.CLEAR}], Actions.STOP ],
            [ [{Location.RIGHT: LocState.DIRTY}, {Location.RIGHT: LocState.CLEAR}, {Location.LEFT : LocState.DIRTY}, {Location.LEFT : LocState.CLEAR}], Actions.STOP ],
            [ [{Location.LEFT : LocState.DIRTY}, {Location.LEFT : LocState.CLEAR}, {Location.RIGHT: LocState.CLEAR}], Actions.STOP ],
            [ [{Location.LEFT : LocState.CLEAR}, {Location.RIGHT: LocState.DIRTY}, {Location.RIGHT: LocState.CLEAR}], Actions.STOP ],
            [ [{Location.RIGHT: LocState.CLEAR}, {Location.LEFT : LocState.DIRTY}, {Location.LEFT : LocState.CLEAR}], Actions.STOP ],
            [ [{Location.RIGHT: LocState.DIRTY}, {Location.RIGHT: LocState.CLEAR}, {Location.LEFT : LocState.CLEAR}], Actions.STOP ],                                  
            [ [{Location.RIGHT: LocState.CLEAR}, {Location.LEFT : LocState.CLEAR}], Actions.STOP ],
            [ [{Location.RIGHT: LocState.CLEAR}, {Location.LEFT : LocState.CLEAR}], Actions.STOP ]                             
           ] # End of table
        
        self.percepts = [] # populate this list with what the agent perceives (the agent can only perceive the state of its current location).
        
        
        # state for model-based agent
        self.state = { Location.LEFT : -1,  Location.RIGHT : -1 }
        self.vacuum_location = Location(self.world.get_vacuum_location().x)
        
        
       
    #
    # Methods   
    def random_move(self):
        return random.choice(self.moves)
    def table_agent(self):
        self.vacuum_location = Location(self.world.get_vacuum_location().x)
        if self.world.is_vacuum_at_dirty_location():
            dictionary = {self.vacuum_location: LocState.DIRTY}
        else:
            dictionary = {self.vacuum_location: LocState.CLEAR}
        self.percepts.append(dictionary)
        for entry in self.action_table:
            if entry[0] == self.percepts:
                return entry[1]
    def reflex_vacuum_agent(self):
        if self.world.is_vacuum_at_dirty_location():
            return Actions.CLEAN
        elif self.vacuum_location == Location.LEFT:
            return Actions.MOVE_RIGHT
        elif self.vacuum_location == Location.RIGHT:
            return Actions.MOVE_LEFT
    # return the action that the agent should execute.
    def make_move(self):
        
       x = self.random_move()
       y = self.table_agent()
       return self.reflex_vacuum_agent() # no operations
        
        
        
        
        
        
