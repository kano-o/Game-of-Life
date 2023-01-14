import random

"""
def dead_state(width, height):
    dead_life = [[0 for x in range(width)] for y in range(height)]
    return dead_life
"""

def random_state(width, height):
    random_life = [[random.randint(0,1) for x in range(width)] for y in range(height)]
    return random_life

width = 70
height = 30

#print(random_state(width, height))

def render(board):
    
    out = ''
    lines = ''

    for x in range(width + 2):
        
        lines += '-'

    out += lines
    out += '\n'

    for x in range(height):
        out += '|'
        for y in range(width):
            if (board[x][y] == 1):
                out += '\033[92m■\033[0m'
            else:
                out += '\033[91m■\033[0m'
            
        out += '|'
        out += '\n'
    
    out += lines

    print(out)

board = random_state(width, height)

render(board)

def clamp(index, max):
    return(index % max)

def count_neighbors(board, x, y):
  neighbors = 0
  for i in range(x-1, x+2):
    for j in range(y-1, y+2):
      if i == x and j == y:
        continue
      # Clamp the values so they don't go out of bounds
      if board[i % height][j % width] == 1:
        neighbors += 1
  return neighbors

def is_alive(board, x, y):
    return board[x][y] == 1

def next_board_state(board):

    new_board = [[0 for x in range(width)] for y in range(height)]

    for x in range(height):
        for y in range(width):    
            if (is_alive(board, x, y)):
                if (count_neighbors(board, x, y) < 2):
                    new_board[x][y] = 0
                elif (count_neighbors(board, x, y) < 4):
                    new_board[x][y] = 1
                elif (count_neighbors(board, x, y) > 3):
                    new_board[x][y] = 0
            else:
                if (count_neighbors(board, x, y) == 3):
                    new_board[x][y] = 1
            
    
    return new_board

render(next_board_state(board))



"""
1. Any live cell with 0 or 1 live neighbors becomes dead, because of underpopulation
2. Any live cell with 2 or 3 live neighbors stays alive, because its neighborhood is just right
3. Any live cell with more than 3 live neighbors becomes dead, because of overpopulation
4. Any dead cell with exactly 3 live neighbors becomes alive, by reproduction
"""