# environment.py
"""
This module implements a ModifiedVacuumEnvironment.
It is designed to meet the requirements of Exercise 2.11 (the standard vacuum-cleaner world)
and Exercise 2.14 (the modified vacuum environment with unknown boundaries, obstacles, and dirt configuration).
Users can modify the environment by explicitly adding dirt and obstacles.
"""

from src.berkeley_ai.agents import XYEnvironment, Dirt, Wall
import random

class ModifiedVacuumEnvironment(XYEnvironment):
    """
    A modified vacuum environment with configurable grid size.
    Provides methods to add dirt and obstacles explicitly.
    Supports four-directional movement and checks if the environment is clean.
    """
    def __init__(self, width=5, height=5):
        super().__init__(width, height)
        self.dirt_locations = set()
        self.add_walls()

    def add_dirt(self, location):
        """
        Add dirt at a specified location if there is no obstacle.
        :param location: A tuple (x, y)
        """
        if not self.some_things_at(location, Wall):
            self.add_thing(Dirt(), location)
            self.dirt_locations.add(location)

    def add_obstacle(self, location):
        """
        Add an obstacle (wall) at a specified location if no dirt is present.
        :param location: A tuple (x, y)
        """
        if location not in self.dirt_locations:
            self.add_thing(Wall(), location)

    def percept(self, agent):
        """
        Return the percept for an agent.
        Percept is a tuple: (agent's current location, status)
        where status is 'Dirty' if there is any Dirt at that location.
        """
        location = agent.location
        status = 'Dirty' if self.some_things_at(location, Dirt) else 'Clean'
        return (location, status)

    def execute_action(self, agent, action):
        """
        Execute an action by the agent.
        Movement actions update the agent's location (if valid) and incur a penalty.
        'Suck' cleans any dirt at the agent's current location and awards a reward.
        """
        agent.bump = False
        x, y = agent.location
        new_location = agent.location

        if action == 'Right':
            new_location = (x+1, y)
        elif action == 'Left':
            new_location = (x-1, y)
        elif action == 'Up':
            new_location = (x, y-1)
        elif action == 'Down':
            new_location = (x, y+1)
        elif action == 'Suck':
            dirt_list = self.list_things_at(agent.location, Dirt)
            if dirt_list:
                for dirt in dirt_list:
                    self.delete_thing(dirt)
                self.dirt_locations.discard(agent.location)
                agent.performance += 100  # Reward for cleaning
            return
        elif action == 'NoOp':
            return

        # Check if new_location is valid and not blocked by a wall
        if self.is_valid_location(new_location) and not self.some_things_at(new_location, Wall):
            agent.location = new_location
        else:
            agent.bump = True
        agent.performance -= 1  # Penalty for each action

    def is_valid_location(self, location):
        """
        Check if a location is within bounds.
        """
        x, y = location
        return 0 <= x < self.width and 0 <= y < self.height

    def is_clean(self):
        """
        The environment is clean if there is no dirt left.
        """
        return len(self.dirt_locations) == 0

    def run(self, steps=1000):
        """
        Run the simulation for a number of steps or until the environment is clean.
        """
        for _ in range(steps):
            if self.is_clean():
                break
            self.step()
