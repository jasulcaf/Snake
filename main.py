import os

from snake.game import Game
from snake.snake import Snake
from snake.constants import *
game = Game(3,3,Snake([[0,0],[0,1]],RIGHT))
game.render()
game.run()

def print_directory_structure(root_dir, indent=0):
    for item in os.listdir(root_dir):
        path = os.path.join(root_dir, item)
        print("  " * indent + "+-- " + item)
        if os.path.isdir(path):
            print_directory_structure(path, indent + 1)

# Example usage:
# root_directory = "."  # Current directory
# print_directory_structure(root_directory)