# simulation.py
"""
This module runs performance experiments and generates professional visualizations 
for the vacuum environment simulator.

It addresses:
  - Exercise 2.11 (Vacuum-Cleaner World): A modular, performance-measuring simulator.
    The environment is configurable (size, shape, dirt placement, etc.)—for example, a 2x1 world or a larger grid.
    
  - Exercise 2.14 (Modified Vacuum Environment): An environment with unknown boundaries, obstacles, 
    and random dirt, where the agent can move Up, Down, Left, and Right.
    It compares multiple agents:
      - Simple Reflex Agent (from src.berkeley_ai.agents.py, adapted via reflex_grid_agent.py)
      - Randomized Reflex Agent (from src.berkeley_ai.agents.py, adapted via random_grid_agent.py)
      - Model-Based Reflex Agent (from src.berkeley_ai.agents.py, adapted via model_based_grid_agent.py)
      - BFS-based Rational Agent (from my_rational_agent.py)

Visualizations produced for each of two environments (default and worst-case) include:
  - Initial Environment State (cells showing clean, dirty, or obstacles)
  - Bar Charts (Average Performance with Error Bars)
  - Box Plots (Performance Distribution)
  - Line Charts (Time-Series of Cumulative Performance for each agent)
  - Heatmaps (Spatial Visit Frequencies for each agent)

All figures are saved with descriptive filenames.
"""

import os
import random
import statistics
import matplotlib.pyplot as plt
import numpy as np

from src.environment.environment import ModifiedVacuumEnvironment
from src.berkeley_ai.agents import Dirt, Wall
from src.agents.reflex_grid_agent import ReflexGridAgent as ReflexAgent
from src.agents.random_grid_agent import RandomGridAgent as RandomAgent
from src.agents.model_based_grid_agent import ModelBasedGridAgent as ModelAgent
from src.agents.my_rational_agent import RationalVacuumAgent as RationalAgent

# --------------------------------------------------
# Environment Factory Functions
# --------------------------------------------------

def default_env_factory(env_width=5, env_height=5, inner_dirt_prob=0.5, inner_obs_prob=0.3,
                        boundary_dirt_prob=0.1, boundary_obs_prob=0.1, **kwargs):
    """
    Factory for the default environment with random dirt and obstacles.
    
    Parameters:
      - env_width, env_height: Dimensions of the environment.
      - inner_dirt_prob, inner_obs_prob: Probabilities for dirt and obstacles in inner cells.
      - boundary_dirt_prob, boundary_obs_prob: Probabilities for dirt and obstacles in boundary cells.
      - Accepts extra keyword arguments (e.g., env_label) without error.
    """
    env = ModifiedVacuumEnvironment(env_width, env_height)
    
    for x in range(env_width):
        for y in range(env_height):
            # Check if cell is at boundary.
            if x == 0 or y == 0 or x == env_width - 1 or y == env_height - 1:
                # For boundary cells, use lower probabilities.
                if random.random() < boundary_dirt_prob:
                    env.add_dirt((x, y))
                if random.random() < boundary_obs_prob:
                    env.add_obstacle((x, y))
            else:
                # Inner grid probabilities.
                if random.random() < inner_dirt_prob:
                    env.add_dirt((x, y))
                if random.random() < inner_obs_prob:
                    env.add_obstacle((x, y))
    return env

def create_worst_case_environment():
    """
    Creates a 5x5 grid with:
      - obstacles in row=1 and row=3, columns=1..3
      - dirt in each corner
      - NO perimeter walls, so we have a corridor around the outer columns
    """
    width, height = 5, 5
    env = ModifiedVacuumEnvironment(width, height)
    
    # Place obstacles in columns 1 and 3 for rows 1..3 (the "middle" three rows).
    for row in [1, 2, 3]:
        env.add_obstacle((1, row))  # Column=1
        env.add_obstacle((3, row))  # Column=3
    
    # Place dirt in each of the four corners
    corner_dirt_locations = [(0, 0), (0, height - 1),
                             (width - 1, 0), (width - 1, height - 1)]
    for loc in corner_dirt_locations:
        # Directly add a Dirt object at the corner
        dirt = Dirt()
        dirt.location = loc
        env.things.append(dirt)
        env.dirt_locations.add(loc)
    
    return env
    

def worst_case_env_factory(**kwargs):
    """
    Factory for the worst-case environment.
    Accepts extra keyword arguments without error.
    """
    return create_worst_case_environment()

# --------------------------------------------------
# Environment Visualization Function
# --------------------------------------------------

def visualize_environment_state(env, title="Environment State", save_filename=None):
    """
    Visualizes the current state of the environment:
      - Obstacles (Wall) are colored gray.
      - Dirt is colored red.
      - Clean cells are colored green.
      - If an agent is present, its location is marked with a black circle.
      
    This function helps demonstrate the modular performance-measuring simulator
    as required by Exercise 2.11.
    """
    grid_colors = np.empty((env.width, env.height), dtype=object)
    # Iterate over each cell in the grid.
    for x in range(env.width):
        for y in range(env.height):
            if env.some_things_at((x, y), Wall):
                grid_colors[x, y] = 'gray'
            elif env.some_things_at((x, y), Dirt):
                grid_colors[x, y] = 'red'
            else:
                grid_colors[x, y] = 'green'
    fig, ax = plt.subplots(figsize=(env.width, env.height))
    for x in range(env.width):
        for y in range(env.height):
            rect = plt.Rectangle((x, y), 1, 1, facecolor=grid_colors[x, y], edgecolor='black')
            ax.add_patch(rect)
    # Mark agent locations, if any.
    for agent in env.agents:
        if hasattr(agent, 'location') and agent.location is not None:
            ax.plot(agent.location[0] + 0.5, agent.location[1] + 0.5, 'ko', markersize=15)
    ax.set_xlim(0, env.width)
    ax.set_ylim(0, env.height)
    ax.set_aspect('equal')
    plt.title(title)
    plt.axis('off')
    if save_filename:
        # Save to 'visualizations/initial_states/'
        outpath = os.path.join("visualizations", "initial_states", save_filename)
        plt.savefig(outpath, bbox_inches='tight')
    plt.show()

# --------------------------------------------------
# Simulation Functions (Parameterized by Environment Factory)
# --------------------------------------------------

def run_simulation(agent_class, env_factory, steps=100, **env_kwargs):
    """
    Run a single simulation trial with the specified agent type and environment settings.
    Returns the final performance score of the agent.
    """
    env = env_factory(**env_kwargs)
    agent = agent_class()
    # Place the agent at a fixed starting position.
    env.add_thing(agent, (1, 1))
    env.run(steps)
    return agent.performance

def compare_agents(env_factory, trials=10, steps=100, **env_kwargs):
    """
    Compare the four agent types over multiple trials using the provided environment factory.
    Returns a dictionary mapping agent name to (average performance, std deviation).
    (Addresses Exercise 2.14 by comparing different agent models.)
    """
    agent_types = {
        "Reflex": ReflexAgent,
        "Random": RandomAgent,
        "Model-Based": ModelAgent,
        "Rational": RationalAgent
    }
    results = {}
    for name, agent_class in agent_types.items():
        scores = [run_simulation(agent_class, env_factory, steps, **env_kwargs) for _ in range(trials)]
        avg = statistics.mean(scores)
        std = statistics.stdev(scores) if len(scores) > 1 else 0
        results[name] = (avg, std)
        print(f"{name}: Avg Performance = {avg:.2f}, Std Dev = {std:.2f}")
    return results

# --------------------------------------------------
# Visualization Functions for Overall Performance
# --------------------------------------------------

def plot_bar_chart(results, env_label="default"):
    """
    Plot a bar chart with error bars (average performance with standard deviation) for the four agent types.
    Saves the plot as "bar_chart_{env_label}.png".
    """
    names = list(results.keys())
    avg_scores = [results[name][0] for name in names]
    std_devs = [results[name][1] for name in names]
    plt.figure(figsize=(8, 5))
    plt.bar(names, avg_scores, yerr=std_devs, capsize=5, color='skyblue')
    plt.xlabel('Agent Type')
    plt.ylabel('Average Performance')
    plt.title(f'Agent Performance Comparison ({env_label.capitalize()} Environment)')
    # Save to 'visualizations/bar_charts/'
    outpath = os.path.join("visualizations", "bar_charts", f"bar_chart_{env_label}.png")
    plt.savefig(outpath, bbox_inches="tight")
    plt.show()

def compare_agents_boxplot(env_factory, trials=10, steps=100, **env_kwargs):
    """
    Run simulations for each agent type and generate a box plot showing the performance distribution.
    Saves the plot as "boxplot_{env_label}.png".
    (This visualization is professional and complements the bar charts.)
    """
    agent_types = {
        "Reflex": ReflexAgent,
        "Random": RandomAgent,
        "Model-Based": ModelAgent,
        "Rational": RationalAgent
    }
    data = {}
    for name, agent_class in agent_types.items():
        scores = [run_simulation(agent_class, env_factory, steps, **env_kwargs) for _ in range(trials)]
        data[name] = scores
    plt.figure(figsize=(8, 5))
    plt.boxplot([data[name] for name in data.keys()], tick_labels=list(data.keys()))
    plt.xlabel('Agent Type')
    plt.ylabel('Performance Score')
    title = f"Performance Distribution per Agent Type ({env_kwargs.get('env_label', 'default').capitalize()} Environment)"
    plt.title(title)
    # Save to 'visualizations/box_plots/'
    outpath = os.path.join("visualizations", "box_plots", f"boxplot_{env_kwargs.get('env_label', 'default')}.png")
    plt.savefig(outpath, bbox_inches="tight")
    plt.show()
    return data

# --------------------------------------------------
# Visualization Functions for Time-Series (Line Charts)
# --------------------------------------------------

def run_simulation_time_series(agent_class, env_factory, steps=100, **env_kwargs):
    """
    Run a simulation step-by-step and record cumulative performance at each step.
    Returns a list of performance values over time.
    (Supports time-series visualization of agent performance evolution.)
    """
    env = env_factory(**env_kwargs)
    for x in range(1, env.width - 1):
        for y in range(1, env.height - 1):
            if random.random() < 0.3:
                env.add_dirt((x, y))
            if random.random() < 0.1:
                env.add_obstacle((x, y))
    agent = agent_class()
    env.add_thing(agent, (1, 1))
    performance_over_time = []
    for _ in range(steps):
        env.step()
        performance_over_time.append(agent.performance)
        if env.is_clean():
            break
    return performance_over_time

def plot_time_series(time_series, agent_name, env_label="default"):
    """
    Plot a line chart showing cumulative performance over simulation steps.
    Saves the plot as "linechart_{agent_name}_{env_label}.png".
    """
    plt.figure(figsize=(8, 5))
    plt.plot(time_series, marker='o')
    plt.xlabel('Simulation Step')
    plt.ylabel('Cumulative Performance')
    plt.title(f'Performance Over Time - {agent_name} ({env_label.capitalize()} Environment)')
    plt.grid(True)
    filename = f"linechart_{agent_name.replace(' ', '_')}_{env_label}.png"
    # Save to 'visualizations/line_charts/'
    outpath = os.path.join("visualizations", "line_charts", filename)
    plt.savefig(outpath, bbox_inches="tight")
    plt.show()

# --------------------------------------------------
# Visualization Functions for Heatmaps
# --------------------------------------------------

def run_simulation_heatmap(agent_class, env_factory, steps=100, **env_kwargs):
    """
    Run a simulation and record the number of visits to each cell.
    Returns a 2D numpy array representing cell visitation frequencies.
    (Supports spatial visualization of agent behavior via a heatmap.)
    """
    env = env_factory(**env_kwargs)
    for x in range(1, env.width - 1):
        for y in range(1, env.height - 1):
            if random.random() < 0.3:
                env.add_dirt((x, y))
            if random.random() < 0.1:
                env.add_obstacle((x, y))
    agent = agent_class()
    env.add_thing(agent, (1, 1))
    visits = np.zeros((env.width, env.height))
    for _ in range(steps):
        env.step()
        x, y = agent.location
        visits[x, y] += 1
        if env.is_clean():
            break
    return visits

def plot_heatmap(data, agent_name, env_label="default"):
    """
    Plot a heatmap of cell visitation frequencies.
    Saves the plot as "heatmap_{agent_name}_{env_label}.png".
    """
    plt.figure(figsize=(6, 6))
    plt.imshow(data.T, cmap='hot', interpolation='nearest')
    plt.title(f'Agent Visit Heatmap - {agent_name} ({env_label.capitalize()} Environment)')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.colorbar(label='Visit Count')
    filename = f"heatmap_{agent_name.replace(' ', '_')}_{env_label}.png"
    # Save to 'visualizations/heatmaps/'
    outpath = os.path.join("visualizations", "heatmaps", filename)
    plt.savefig(outpath, bbox_inches="tight")
    plt.show()

# --------------------------------------------------
# Main Execution: Generate Visualizations for Two Environments
# --------------------------------------------------

if __name__ == "__main__":
    # Visualize the initial state of both environments before simulation.
    # This demonstrates the modular performance-measuring simulator (Exercise 2.11).
    # 1) Default Environment:
    default_env = default_env_factory(env_width=5, env_height=5)
    visualize_environment_state(default_env, title="Initial State: Default Environment", save_filename="initial_default.png")
    
    # 2) Worst-Case Environment:
    worst_env = worst_case_env_factory()
    visualize_environment_state(worst_env, title="Initial State: Worst-Case Environment", save_filename="initial_worst.png")
    
    # Define settings for two environments:
    env_settings = {
        "default": {"env_factory": default_env_factory, "env_kwargs": {"env_width": 5, "env_height": 5, "env_label": "default"}},
        "worst": {"env_factory": worst_case_env_factory, "env_kwargs": {"env_label": "worst"}}
    }
    
    # For each environment, generate:
    # 1 bar chart, 1 box plot, 4 line charts, and 4 heatmaps.
    for label, settings in env_settings.items():
        print(f"\n--- Generating visualizations for {label.capitalize()} Environment ---")
        env_factory = settings["env_factory"]
        env_kwargs = settings["env_kwargs"]
        
        # Bar Chart & Box Plot
        results = compare_agents(env_factory, trials=20, steps=100, **env_kwargs)
        plot_bar_chart(results, env_label=label)
        compare_agents_boxplot(env_factory, trials=20, steps=100, **env_kwargs)
        
        # Agent types for time-series and heatmaps.
        agent_types = {
            "Reflex": ReflexAgent,
            "Random": RandomAgent,
            "Model-Based": ModelAgent,
            "Rational": RationalAgent
        }
        
        # For each agent type, generate a line chart and a heatmap.
        for name, agent_class in agent_types.items():
            ts = run_simulation_time_series(agent_class, env_factory, steps=100, **env_kwargs)
            plot_time_series(ts, name, env_label=label)
            
            hm = run_simulation_heatmap(agent_class, env_factory, steps=100, **env_kwargs)
            plot_heatmap(hm, name, env_label=label)
