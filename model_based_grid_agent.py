"""
model_based_grid_agent.py

A wrapper for a model-based reflex agent adapted to a grid environment.
This agent maintains a very simple internal model (a dictionary of cell statuses)
and uses it to decide actions. When the current cell is dirty, it cleans; otherwise,
it selects a movement action from the four possible directions.
While simple, this adaptation supports four-direction movement and can be extended further.
"""

import random
from agents import Agent, Dirt

def ModelBasedGridAgent():
    model = {}  # Internal model: maps location to status (e.g., 'Dirty' or 'Clean')
    def program(percept):
        location, status = percept
        # Update the model with the current percept.
        model[location] = status
        if status == 'Dirty':
            return 'Suck'
        # Here, a more sophisticated agent might use the model to plan a path.
        # For now, we randomly choose one of the four directions.
        return random.choice(['Left', 'Right', 'Up', 'Down'])
    return Agent(program)
