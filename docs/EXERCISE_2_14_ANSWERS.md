# Exercise 2.14 – Analysis and Design of Modified Vacuum Environment

## 1. Can a simple reflex agent be perfectly rational for this environment? Explain.

**Answer:**  
No—a simple reflex agent is not perfectly rational in an environment with unknown geography  
(i.e., unknown extent, boundaries, obstacles, and random dirt placement). A simple reflex agent  
makes decisions solely based on its current percept without memory or an internal model of the world.  

In our project, the `ReflexVacuumAgent` (imported from `agents.py`) operates in a purely reactive  
manner. Since it lacks state or planning, it cannot adapt to dynamic conditions such as unexpected  
obstacles or a variable dirt configuration. This is why our simulation logs show that the Reflex agent  
typically performs poorly (average performance around **-50 to -70**) in the modified environments.

---

## 2. Can a simple reflex agent with a randomized agent function outperform a simple reflex agent?  
### Design such an agent and measure its performance on several environments.

**Answer:**  
Yes—a randomized simple reflex agent can outperform a standard simple reflex agent in some cases.  
By adding randomness, the agent may explore areas that a fixed-rule agent would never reach,  
sometimes leading to improved performance.  

In our project, the `RandomVacuumAgent` (imported from `agents.py`)  
uses a randomized decision process when the current location is clean. Our simulation experiments  
demonstrate that the Random agent sometimes achieves positive performance (average scores between  
**~15 and ~67**), although its performance is inconsistent (high standard deviation).

---

## 3. Can you design an environment in which your randomized agent will perform poorly? Show your results.

**Answer:**  
Yes, a worst-case environment can be designed for the randomized agent.  
For example, arranging obstacles in a maze-like pattern with many dead-ends can force the agent  
into inefficient, random movements, leading to many movement penalties.  

In our project, we have a function called `create_worst_case_environment()` (in `simulation.py`)  
that constructs a **5×5 grid** with obstacles placed in a maze-like structure and dirt in the  
hard-to-reach corners. When the Random agent is tested in this environment, its performance  
drops significantly (**e.g., a performance score of around 49**), highlighting its limitations in such settings.

---

## 4. Can a reflex agent with state outperform a simple reflex agent?  
### Design such an agent and measure its performance on several environments.  
### Can you design a rational agent of this type?

**Answer:**  
Yes, a reflex agent with state can significantly outperform a simple reflex agent because it uses memory  
(an internal model) to make more informed decisions.  

In our project, the `RationalVacuumAgent` (implemented in `my_rational_agent.py`)  
is a stateful, model-based agent that employs **BFS (Breadth-First Search)** for planning.  
It maintains an internal model of the environment (tracking visited locations, known obstacles,  
and dirt status), and uses BFS to find the shortest path to dirty cells or unexplored areas.  

Our simulation results consistently show that the Rational agent outperforms the other agents  
(**with average performance scores ranging from ~186 to ~262**), demonstrating that incorporating state  
and planning leads to much more efficient cleaning in a modified, unknown environment.

---

# Final Assessment:

- **Simple reflex agents** lack memory and planning; hence, they cannot be perfectly rational in a dynamic, unknown environment.
- **Randomized reflex agents** can sometimes outperform simple reflex agents by exploring new areas,  
  but they may also perform poorly in maze-like worst-case scenarios.
- **Agents with state** (reflex agents with state or fully rational agents using planning such as our  
  **BFS-based `RationalVacuumAgent`**) can significantly improve performance by using an internal model  
  to guide exploration and cleaning.
- Our **integrated project**—including a **modular performance-measuring environment simulator**,  
  multiple agent types, and comprehensive performance evaluations (**with bar charts, box plots,  
  time-series plots, and heatmaps**)—demonstrates these findings clearly, meeting the requirements  
  of **Exercises 2.11 and 2.14**.
