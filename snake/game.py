from collections import defaultdict
from random import randint

from utils.list_manipulation import print_list
from snake.snake import Snake
from snake.constants import *


class Game:
    def __init__(self, width=10, height=5,snake=Snake()):
        self.height = height
        self.width = width
        self.board = [[" " for _ in range(width)] for _ in range(height)]
        self.snake = snake
        self.apple = self.spawn_apple()
        self.score = 0
    
    def snake_positions(self):
        snake_pos = self.snake.body
        pos_dir = defaultdict(int)
        for pos in snake_pos:
            tmp = tuple(pos)
            pos_dir[tmp] += 1
        return pos_dir
    
    def spawn_apple(self, prev_apple=None):
        #print("inside spawn apple")
        pos_dir = self.snake_positions()
        rnd_spawn = randint(0, (self.width * self.height)-1)
        tmp = -1
        while True:
            row = rnd_spawn // self.width
            col = rnd_spawn % self.width
            tmp = tuple([row, col])
            if tmp in pos_dir or tmp == prev_apple:
                # Means that apple would spawn on snake body - need to redraw
                rnd_spawn = randint(0, (self.width * self.height)-1)
                continue
            else:
                # Means the random draw is fine
                break
        #print("The random number is: ",rnd_spawn)
        return tmp
    
    def render(self):
        #print("At start of render apple is at: ", self.apple)
        # Check if snake has ate itself
        pos_dir = self.snake_positions()
        for freq in pos_dir.values():
            if freq > 1:
                # Means that the snake has ate itself
                return None
        
        snake_head = tuple(self.snake.head())
        
        # Check if snake has ate the apple, if so update the game
        if snake_head == self.apple:
            # Snake has ate the apple
            self.score += 1 # Update score count
            self.apple = self.spawn_apple(snake_head) # Spawn a new apple
        
        # Create a padding so that user can tell what's a wall
        corner = "+"
        wall = "-"
        horizontal = [corner] + [wall for _ in range(self.width)] + [corner]
        print_list(horizontal)
        for row in range(0, self.height):
            curr_row = []
            for col in range(0, self.width):
                tmp = tuple([row,col])
                if tmp in pos_dir:
                    # Means that this is a spot where snake is
                    # Check if head or rest of body
                    if tmp == snake_head:
                        curr_row.append("X")
                    else:
                        curr_row.append("0")
                elif tmp == self.apple:
                    curr_row.append("*")
                else:
                    curr_row.append(" ")
            curr = [wall] + curr_row + [wall]
            print_list(curr)
        print_list(horizontal)
        
        return 1
    
    def run(self):
        while True:
            user_input = input("What is your next move?: ").lower()
            if user_input == "exit":
                break
            elif len(user_input) > 1:
                self.render()
                print("Please only type wasd (for up, left, down, right) respectively")
                continue
            self.snake.update_direction(user_input)
            notWallHit = self.snake.move(self.width,self.height,self.apple)
            if notWallHit == -1:
                print("You have hit a wall, Game Over!")
                print("Your score was: ", self.score)
                break
            check_ate = self.render()
            if check_ate == None:
                print("You have ate yourself, Game Over!")
                print("Your score was: ", self.score)
                break