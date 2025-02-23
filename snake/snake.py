from .constants import *
from ..utils.list_manipulation import add_arrays

class Snake:
    def __init__(self, init_body=[[0,0],[0,1],[0,2],[0,3]],init_direction=RIGHT):
        # First element in the array is the tail of the snake
        # Last element in the array is the head of the snake
        # By default, set this to be right
        self.body = init_body
        self.direction = init_direction
    
    # "Deletes" the current tail and updates with the updated position
    def update_pos(self, position):
        self.body = self.body[1:] + [position]
    
    def move(self, upper_width, upper_height):
        # Get the current direction, and move in that way
        dir = self.direction
        cur_head = self.head()
        new_head = add_arrays(cur_head, dir)
        if ((new_head[0] >= upper_height or new_head[0] < 0) or 
            (new_head[1] >= upper_width or new_head[1] < 0)):
            return -1
        self.update_pos(new_head)
        return 1
            
    def update_direction(self, direction):
        new_dir = None
        cur_dir = self.direction
        if direction == "w":
            new_dir = UP
        elif direction == "a":
            new_dir = LEFT
        elif direction == "s":
            new_dir = DOWN
        else:
            new_dir = RIGHT
            
        if new_dir == UP and cur_dir == DOWN:
            # Invalid move - leave the direction unchanged
            return
        elif new_dir == DOWN and cur_dir == UP:
            # Invalid move - leave the direction unchanged
            return
        elif new_dir == RIGHT and cur_dir == LEFT:
            # Invalid move - leave the direction unchanged
            return
        elif new_dir == LEFT and cur_dir == RIGHT:
            # Invalid move - leave the direction unchanged
            return
        self.direction = new_dir
    
    def head(self):
        return self.body[-1]
    def tail(self):
        return self.body[0]