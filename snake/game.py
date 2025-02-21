from utils.list_manipulation import print_list

class Game:
    def __init__(self, height=5, width=10):
        self.height = height
        self.width = width
        self.board = [[" " for _ in range(width)] for _ in range(height)]
    
    def render(self):
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