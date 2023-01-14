import random

"""
def dead_state(width, height):
    dead_life = [[0 for x in range(width)] for y in range(height)]
    return dead_life
"""

def random_state(width, height):
    random_life = [[random.randint(0,1) for x in range(width)] for y in range(height)]
    return random_life

print(random_state(5, 5))