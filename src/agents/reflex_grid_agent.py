"""
reflex_grid_agent.py

A wrapper for the simple reflex agent adapted to a grid environment.
This agent uses four-directional movement (Left, Right, Up, Down) when the cell is clean,
and performs the "Suck" action when dirt is detected.
This extension addresses Exercise 2.14 by enabling exploration in all directions.
"""

import random
from src.berkeley_ai.agents import Agent

def ReflexGridAgent():
    def program(percept):
        # percept is assumed to be a tuple: (location, status)
        location, status = percept
        if status == 'Dirty':
            return 'Suck'
        # Randomly choose one of the four directions for exploration.
        return random.choice(['Left', 'Right', 'Up', 'Down'])
    return Agent(program)
