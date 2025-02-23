from .constants import *

class Snake:
    def __init__(self, init_body=[[0,0],[1,0],[2,0],[3,0]],init_direction=RIGHT):
        # First element in the array is the tail of the snake
        # Last element in the array is the head of the snake
        # By default, set this to be right
        self.body = init_body
        self.direction = init_direction
    
    def update_pos(self, position):
        self.body = self.body[1:] + [position]
    
    def update_direction(self, direction):
        self.direction = direction
    
    def head(self):
        return self.body[-1]