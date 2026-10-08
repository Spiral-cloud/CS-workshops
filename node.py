""" node.py
#  A node within the search tree
#
# Written by: Helen Harman
"""

import utils
        
class Node():
    def __init__(self, location, parent, action):
        # the state
        self.location = location
        # the parent node
        self.parent = parent
        # what actions we took to get from parent.location to this.location
        self.action = action         
        
    def is_goal(self, goal):
        return utils.same_location(self.location, goal)
    
    
    def __repr__(self):
        return f"<Node location:{self.location} action:{self.action}>"
            
    def __str__(self):
        return f"[location:{self.location} action:{self.action}]"
        
        
    
    def __eq__(self, other):
        """Checks if two Nodes are the same just using the location attribute. 
            When checking if the location has been visited/explored or added to frontiers, we can make use of "in".
                Overrides the default implementation
        """
        if isinstance(other, Node):
            return (self.location == other.location)
        return False    
        
