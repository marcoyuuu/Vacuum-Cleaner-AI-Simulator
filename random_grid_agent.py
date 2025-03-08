"""
random_grid_agent.py

A wrapper for a randomized reflex agent adapted for a grid environment.
If the cell is dirty, it cleans; otherwise, it randomly chooses from four directions
(with an additional "NoOp" option if needed).
This adaptation allows full exploration of a 2D grid.
"""

import random
from agents import Agent, Dirt

def RandomGridAgent():
    def program(percept):
        location, status = percept
        if status == 'Dirty':
            return 'Suck'
        # Random choice among four directions and an optional NoOp.
        return random.choice(['Left', 'Right', 'Up', 'Down', 'NoOp'])
    return Agent(program)
