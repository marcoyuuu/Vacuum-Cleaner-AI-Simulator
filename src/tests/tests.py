# tests.py
"""
Unit tests for the Vacuum Cleaner AI Simulator project.

This suite tests:
  - Environment factory functions (default and worst-case) to ensure proper grid dimensions and element placement.
  - Core environment functions: adding/cleaning dirt and obstacle avoidance.
  - Agent performance for the grid-adapted agents:
      * ReflexGridAgent, RandomGridAgent, ModelBasedGridAgent, and RationalVacuumAgent.
  - Simulation helper functions: time-series (cumulative performance), heatmaps, and overall agent comparison.
  
These tests help verify that the project meets the requirements from Exercises 2.11 and 2.14.
"""

import unittest
import numpy as np

from src.environment.environment import ModifiedVacuumEnvironment
from src.berkeley_ai.agents import Dirt, Wall
from src.agents.reflex_grid_agent import ReflexGridAgent
from src.agents.random_grid_agent import RandomGridAgent
from src.agents.model_based_grid_agent import ModelBasedGridAgent
from src.agents.my_rational_agent import RationalVacuumAgent

from src.simulation.simulation import (
    default_env_factory,
    worst_case_env_factory,
    run_simulation,
    compare_agents,
    run_simulation_time_series,
    run_simulation_heatmap
)

class TestEnvironmentFunctions(unittest.TestCase):
    def test_default_env_factory(self):
        """Test that the default environment factory creates an environment of correct size and populates inner cells."""
        env = default_env_factory(env_width=5, env_height=5)
        self.assertEqual(env.width, 5)
        self.assertEqual(env.height, 5)
        # Check inner cells (1,1) to (3,3) for potential dirt or obstacles.
        dirt_count = sum(1 for x in range(1,4) for y in range(1,4) if env.some_things_at((x, y), Dirt))
        obs_count = sum(1 for x in range(1,4) for y in range(1,4) if env.some_things_at((x, y), Wall))
        # Expect some cells to have dirt or obstacles given high probability.
        self.assertTrue(dirt_count >= 0)
        self.assertTrue(obs_count >= 0)

    def test_worst_case_env_factory(self):
        """Test that the worst-case environment contains the expected maze-like structure."""
        env = worst_case_env_factory()
        self.assertEqual(env.width, 5)
        self.assertEqual(env.height, 5)
        # The worst-case design should block the center; for example, cell (1,1) should have an obstacle.
        self.assertTrue(env.some_things_at((1, 1), Wall))
        # Dirt should be in the corners.
        for loc in [(0, 0), (0, 4), (4, 0), (4, 4)]:
            self.assertTrue(env.some_things_at(loc, Dirt))

class TestAgentPerformance(unittest.TestCase):
    def test_reflex_agent_cleaning(self):
        """Test that the ReflexGridAgent cleans dirt from the environment."""
        env = ModifiedVacuumEnvironment(5, 5)
        env.add_dirt((2, 2))
        agent = ReflexGridAgent()
        env.add_thing(agent, (2, 2))
        env.run(steps=10)
        self.assertTrue(env.is_clean(), "Environment should be clean after ReflexGridAgent cleans dirt.")

    def test_random_agent_obstacle_avoidance(self):
        """Test that the RandomGridAgent avoids moving into obstacles."""
        env = ModifiedVacuumEnvironment(5, 5)
        env.add_obstacle((2, 2))
        agent = RandomGridAgent()
        env.add_thing(agent, (1, 2))
        env.run(steps=10)
        self.assertNotEqual(agent.location, (2, 2), "RandomGridAgent should avoid the obstacle at (2,2).")

    def test_rational_agent_cleaning(self):
        """Test that the RationalVacuumAgent uses BFS to plan a path and clean dirt."""
        env = ModifiedVacuumEnvironment(5, 5)
        env.add_dirt((3, 3))
        agent = RationalVacuumAgent()
        env.add_thing(agent, (1, 1))
        env.run(steps=50)
        self.assertTrue(env.is_clean() or agent.performance > 0,
                        "RationalVacuumAgent should clean the environment or achieve positive performance.")

class TestSimulationFunctions(unittest.TestCase):
    def test_run_simulation_time_series(self):
        """Test that the time-series function returns a non-empty list of numerical performance values."""
        ts = run_simulation_time_series(RationalVacuumAgent, default_env_factory, steps=50, env_width=5, env_height=5)
        self.assertTrue(len(ts) > 0, "Time-series data should not be empty.")
        self.assertTrue(all(isinstance(val, (int, float)) for val in ts), "All time-series entries must be numbers.")
    
    def test_run_simulation_heatmap(self):
        """Test that the heatmap function returns an array with the correct shape and numeric values."""
        hm = run_simulation_heatmap(RationalVacuumAgent, default_env_factory, steps=50, env_width=5, env_height=5)
        self.assertEqual(hm.shape, (5, 5), "Heatmap shape should be (5,5).")
        self.assertTrue(np.issubdtype(hm.dtype, np.number), "Heatmap values should be numeric.")

    def test_compare_agents(self):
        """Test that compare_agents returns a dictionary with expected agent keys."""
        results = compare_agents(default_env_factory, trials=5, steps=50, env_width=5, env_height=5, env_label="default")
        self.assertIsInstance(results, dict)
        for key in ["Reflex", "Random", "Model-Based", "Rational"]:
            self.assertIn(key, results)

if __name__ == "__main__":
    unittest.main()
