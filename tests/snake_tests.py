from snake.snake import Snake
from snake.constants import *

def test_update_direction1():
    snake = Snake()
    direction = "d"
    snake.update_direction(direction)
    assert(snake.direction == RIGHT)
    
def test_update_direction2():
    snake = Snake()
    assert(snake.direction == RIGHT)
    direction = "a"
    snake.update_direction(direction)
    assert(snake.direction == RIGHT) #Snake can't go left when going right

def test_update_direction3():
    snake = Snake()
    direction = "w"
    snake.update_direction(direction)
    assert(snake.direction == UP)
    
def test_update_direction4():
    snake = Snake()
    direction = "w"
    snake.update_direction(direction)
    assert(snake.direction == UP)
    direction = "s"
    snake.update_direction(direction)
    assert(snake.direction == UP)
    
def test_update_direction5():
    snake = Snake()
    direction = "s"
    snake.update_direction(direction)
    assert(snake.direction == DOWN)

# Just move 1 over right   
def test_move1():
    snake = Snake(init_body=[[0,0],[0,1],[0,2],[0,3]],init_direction=RIGHT)
    check = snake.move(5, 10)
    assert(check == 1)
    assert(snake.body == [[0,1],[0,2],[0,3],[0,4]])

# Just move 1 down    
def test_move2():
    snake = Snake(init_body=[[0,0],[0,1],[0,2],[0,3]], init_direction=DOWN)
    check = snake.move(5, 10)
    assert(check == 1)
    assert(snake.body == [[0,1],[0,2],[0,3],[1,3]])

# Just move 1 up    
def test_move3():
    snake = Snake(init_body=[[4,0],[4,1],[4,2],[4,3]], init_direction=UP)
    check = snake.move(5, 10)
    assert(check == 1)
    assert(snake.body == [[4,1],[4,2],[4,3],[3,3]])
    
# Just move 1 left    
def test_move4():
    snake = Snake(init_body=[[4,4],[4,3],[4,2]], init_direction=LEFT)
    check = snake.move(5, 10)
    assert(check == 1)
    assert(snake.body == [[4,3],[4,2],[4,1]])

# Exit bound by 1 too far left    
def test_move5():
    snake = Snake(init_body=[[4,2],[4,1],[4,0]], init_direction=LEFT)
    check = snake.move(5, 10)
    assert(check == -1)

# Exit bound by 1 too far right    
def test_move6():
    snake = Snake(init_body=[[0,3],[0,4]], init_direction=RIGHT)
    check = snake.move(5, 10)
    assert(check == -1)

# Exit bound by one too far up  
def test_move7():
    snake = Snake(init_body=[[0,1],[0,2]], init_direction=UP)
    check = snake.move(5, 10)
    assert(check == -1)

# Exit bound by one too far down    
def test_move8():
    snake = Snake(init_body=[[8,2],[9,2]], init_direction=DOWN)
    check = snake.move(5, 10)
    assert(check == -1)
    
# Ate an Apple    
def test_move9():
    snake = Snake(init_body=[[7,2],[7,3]], init_direction=RIGHT)
    check = snake.move(5, 10,tuple([7,4]))
    assert(check == 1)
    assert(snake.body == [[7,2],[7,3],[7,4]])

