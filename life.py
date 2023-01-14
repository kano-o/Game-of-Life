import random

"""
def dead_state(width, height):
    dead_life = [[0 for x in range(width)] for y in range(height)]
    return dead_life
"""

def random_state(width, height):
    random_life = [[random.randint(0,1) for x in range(width)] for y in range(height)]
    return random_life

width = 30
height = 10

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

render(random_state(width, height))