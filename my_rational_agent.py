# my_rational_agent.py
"""
This module implements a BFS-based rational vacuum agent.
This agent is designed for Exercise 2.14, where the environment is unknown 
and the agent must use state (an internal model) and planning to perform effectively.
It extends the base Agent class (from agents.py) without modifying the base code.
"""

import random
from collections import deque
from agents import Agent  # Import the base Agent from agents.py

def RationalVacuumAgent():
    """A rational agent for the partially observable vacuum environment.
    This agent uses a model-based approach with systematic exploration and BFS for planning.
    """
    # Initialize the model of the environment
    model = {
        'locations': set(),   # Set of known locations
        'dirt_status': {},    # Map of location to status
        'known_map': {},      # Map of known locations and their status ('explorable', 'obstacle', 'unknown')
        'current_location': None,
        'last_action': None,
        'backtrack_path': []  # Stack for backtracking (if needed)
    }

    def update_model(model, action, percept):
        """Update the agent's model based on action and percept."""
        location, status = percept

        if model['current_location'] is not None and action in ['Right', 'Left', 'Up', 'Down']:
            x, y = model['current_location']
            expected_location = None
            if action == 'Right':
                expected_location = (x+1, y)
            elif action == 'Left':
                expected_location = (x-1, y)
            elif action == 'Up':
                expected_location = (x, y-1)
            elif action == 'Down':
                expected_location = (x, y+1)
            if expected_location and expected_location != location:
                model['known_map'][expected_location] = 'obstacle'
        model['current_location'] = location
        model['locations'].add(location)
        model['known_map'][location] = 'explorable'
        model['dirt_status'][location] = status
        x, y = location
        for adjacent in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if adjacent not in model['known_map']:
                model['known_map'][adjacent] = 'unknown'
        model['last_action'] = action
        return model

    def get_unexplored_adjacent(model):
        """Find an unexplored adjacent location."""
        x, y = model['current_location']
        for action, adjacent in [('Right', (x+1, y)), ('Left', (x-1, y)),
                                 ('Down', (x, y+1)), ('Up', (x, y-1))]:
            if adjacent in model['known_map'] and model['known_map'][adjacent] == 'unknown':
                return action, adjacent
        return None, None

    def get_next_action_bfs(model):
        """Use BFS to find the shortest path to an unexplored area."""
        start = model['current_location']
        queue = deque([(start, [])])  # (location, path)
        visited = {start}
        while queue:
            current, path = queue.popleft()
            x, y = current
            for direction, adjacent in [('Right', (x+1, y)), ('Left', (x-1, y)),
                                          ('Down', (x, y+1)), ('Up', (x, y-1))]:
                if adjacent in model['known_map'] and model['known_map'][adjacent] == 'unknown':
                    return path[0] if path else direction
                if (adjacent not in visited and adjacent in model['known_map'] and 
                    model['known_map'][adjacent] == 'explorable'):
                    new_path = path + [get_direction(current, adjacent)]
                    queue.append((adjacent, new_path))
                    visited.add(adjacent)
        return random.choice(['Right', 'Left', 'Up', 'Down'])

    def get_direction(from_loc, to_loc):
        """Determine the direction from from_loc to to_loc."""
        fx, fy = from_loc
        tx, ty = to_loc
        if tx > fx:
            return 'Right'
        elif tx < fx:
            return 'Left'
        elif ty > fy:
            return 'Down'
        elif ty < fy:
            return 'Up'
        return 'NoOp'

    def program(percept):
        nonlocal model
        if model['current_location'] is None:
            model['current_location'] = percept[0]
        model = update_model(model, model['last_action'], percept)
        location, status = percept
        if status == 'Dirty':
            return 'Suck'
        action, _ = get_unexplored_adjacent(model)
        if action:
            model['last_action'] = action
            return action
        action = get_next_action_bfs(model)
        model['last_action'] = action
        return action

    return Agent(program)  # Use the base Agent class from agents.py
