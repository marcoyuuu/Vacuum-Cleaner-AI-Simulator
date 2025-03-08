# visualize_two_location_step_by_step.py
"""
Demonstrates a step-by-step animation of the two-location vacuum world (Exercise 2.11),
showing both cells dirty at the initial frame. We use an init_func so the agent
doesn't clean immediately before the first draw.

Key points:
  - 2x1 environment (A and B).
  - Both cells forced dirty initially.
  - A ReflexVacuumAgent is placed in A.
  - The environment is shown BEFORE any step is taken (so you see A dirty),
    then each subsequent frame runs one step.
  - The agent's performance is displayed in the title.
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from environment import ModifiedVacuumEnvironment
from agents import ReflexVacuumAgent, Dirt

def visualize_two_location_step_by_step(num_steps=3):
    """
    1. Create a 2x1 environment (A->(0,0), B->(1,0)).
    2. Add dirt to both cells, ensuring they're dirty initially.
    3. Place a ReflexVacuumAgent at location A.
    4. Use FuncAnimation with init_func to show the truly pre-step environment,
       then animate each step, displaying the agent's performance in the title.
    """
    env = ModifiedVacuumEnvironment(width=2, height=1)

    # Force both cells to be dirty
    env.add_dirt((0, 0))
    env.add_dirt((1, 0))

    agent = ReflexVacuumAgent()
    env.add_thing(agent, (0, 0))

    fig, ax = plt.subplots(figsize=(5, 3))

    step_info = {"current_step": 0}  # track steps ourselves

    def draw_environment():
        """
        Draw the environment at the current state:
          - Red if dirty, green if clean
          - Label 'A' and 'B'
          - Black circle for agent location
          - Title shows step count and agent performance
        """
        ax.clear()
        ax.set_xlim(0, 2)
        ax.set_ylim(0, 1)
        ax.set_aspect('equal')
        ax.axis('off')

        # Check dirt in each cell
        cell_status = []
        for x in range(2):
            if env.some_things_at((x, 0), Dirt):
                cell_status.append(0)  # dirty
            else:
                cell_status.append(1)  # clean

        # 0 -> red (dirty), 1 -> green (clean)
        color_map = {0: 'red', 1: 'green'}

        for x in range(2):
            rect = plt.Rectangle((x, 0), 1, 1,
                                 facecolor=color_map[cell_status[x]],
                                 edgecolor='black')
            ax.add_patch(rect)
            label = 'A' if x == 0 else 'B'
            ax.text(x + 0.5, 0.5, label, ha='center', va='center',
                    fontsize=18, color='white')

        # Mark agent
        if agent.location is not None:
            ax.plot(agent.location[0] + 0.5, agent.location[1] + 0.5,
                    'ko', markersize=15)

        ax.set_title(
            f"Two-Location Vacuum World (Step {step_info['current_step']}/{num_steps})\n"
            f"Agent Performance: {agent.performance}",
            fontsize=10
        )

    def init_func():
        """
        Draw the environment before any steps are taken.
        This ensures we see both cells as dirty if we forced them to be dirty.
        """
        draw_environment()

    def animate(_frame):
        """
        Called at each frame. We run one step of the environment, then redraw.
        """
        if step_info['current_step'] < num_steps and not env.is_clean():
            env.step()
            step_info['current_step'] += 1
            draw_environment()

    ani = animation.FuncAnimation(
        fig, animate, frames=num_steps, interval=1000,
        init_func=init_func, repeat=False
    )

    plt.show()

if __name__ == "__main__":
    visualize_two_location_step_by_step(num_steps=3)
