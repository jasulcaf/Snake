from utils.list_manipulation import print_list
from snake.snake import Snake
from snake.constants import *


class Game:
    def __init__(self, height=5, width=10):
        self.height = height
        self.width = width
        self.board = [[" " for _ in range(width)] for _ in range(height)]
        self.snake = Snake()
    
    def render(self):
        # Update the board with the current snake positioning
        snake_pos = self.snake.body
        for pos in snake_pos:
            x = pos[0]
            y = pos[1]
            self.board[x][y] = "0"
        snake_head = self.snake.head()
        self.board[snake_head[0]][snake_head[1]] = "X"
        
        # Create a padding so that user can tell what's a wall
        corner = "+"
        wall = "-"
        horizontal = [corner] + [wall for _ in range(self.width)] + [corner]
        print_list(horizontal)
        for row in range(0, self.height):
            curr = [wall] + self.board[row] + [wall]
            print_list(curr)
        print_list(horizontal)
game = Game()
print(game.board)
game.render()